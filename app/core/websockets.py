from starlette.websockets import WebSocket, WebSocketDisconnect
from app.api.utils.drones import execute_drone_command
from app.core.esp import esp_controller


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls in cls._instances:
            return cls._instances[cls]
        cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ConnectionManager(metaclass=SingletonMeta):
    def __init__(self):
        self.active_connections = {}

    async def connect(self, websocket: WebSocket, user_id: str):
        await websocket.accept()
        self.active_connections[user_id] = websocket

        await self.listen_for_messages(user_id, websocket)

    async def disconnect(self, user_id: str):
        self.active_connections.pop(user_id, None)

        # Close the ESP session when the WebSocket disconnects
        if not self.active_connections:  # If no active connections left
            esp_controller.close()  # Close the ESP session

    async def broadcast_message(self, user_id, message):
        connection = self.active_connections.get(user_id)
        if connection:
            await connection.send_json(message)

    async def listen_for_messages(self, user_id: str, websocket: WebSocket):
        try:
            print("LISTENS")
            while True:
                data = await websocket.receive_json()
                print(data)
                command = data["command"]
                value = data["value"] - 300

                _, error = execute_drone_command(command, value)
                error = None
                if error:
                    await self.broadcast_message(user_id, error)
        except WebSocketDisconnect:
            print(f"User {user_id} disconnected")
            await self.disconnect(user_id)
        except Exception as e:
            print(f"WebSocket Error for {user_id}: {e}")
            await self.disconnect(user_id)