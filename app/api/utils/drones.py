import requests
from app.core.esp import esp_controller
from datetime import datetime


def execute_drone_command(command: str, value: int):
    command_map = {
        "ARM": 4,
        "THROTTLE": 0,
        "ROLL": 1,
        "PITCH": 2,
        "YAW": 3
    }

    if command in command_map:
        channel = command_map[command]
        print(f"{command}: {value}")
        timestamp_str = datetime.now().strftime("%H:%M:%S")
        print(timestamp_str)

        if value > 1900:
            value = 1900
        elif value < 1050:
            value = 1050

        if command == "ARM":
            esp_controller.update_channel(0, 600)

        esp_controller.update_channel(channel, value)

    if command == "HOVER":
        print(f"{command}: {value}")
        esp_controller.update_channel(0, 1200)  # THROTTLE
        esp_controller.update_channel(1, 1200)  # ROLL
        esp_controller.update_channel(2, 1200)  # PITCH
        esp_controller.update_channel(3, 1200)  # YAW
    # else:
    #     print("❌ Unknown command received. Please check input.")

    return None, None