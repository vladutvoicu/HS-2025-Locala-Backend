from fastapi import APIRouter, WebSocket, WebSocketDisconnect, HTTPException
from app.core.websockets import ConnectionManager

websockets_router = APIRouter(tags=["WebSockets"], prefix="/ws")
connection_manager = ConnectionManager()


@websockets_router.websocket("/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    try:
        await connection_manager.connect(websocket, user_id)
        print(f"Client connected: {user_id}")

    except WebSocketDisconnect:
        print(f"Client disconnected: {user_id}")
        await connection_manager.disconnect(user_id)
    except Exception as e:
        print(f"Error: {e}")
        await connection_manager.disconnect(user_id)
        raise HTTPException(status_code=400, detail=str(e))
