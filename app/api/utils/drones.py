
def execute_drone_command(command: str, speed: int):
    command = command.upper()

    if command == "TAKEOFF":
        print(f"🚁 Drone is taking off with throttle at {speed}% power.")
        return None, None

    elif command == "LAND":
        print(f"🛬 Drone is landing with throttle reduction at {speed}%.")
        return None, None

    elif command == "MOVE_FWD":
        print(f"➡️ Moving forward at {speed}% speed.")
        return None, None

    elif command == "MOVE_BWD":
        print(f"⬅️ Moving backward at {speed}% speed.")
        return None, None

    elif command == "MOVE_LEFT":
        print(f"⬅️ Strafing left at {speed}% speed.")
        return None, None

    elif command == "MOVE_RIGHT":
        print(f"➡️ Strafing right at {speed}% speed.")
        return None, None

    elif command == "TURN_LEFT":
        print(f"↩️ Rotating left (yaw) at {speed}% speed.")
        return None, None

    elif command == "TURN_RIGHT":
        print(f"↪️ Rotating right (yaw) at {speed}% speed.")
        return None, None

    elif command == "HOVER":
        print(f"🛑 Drone is hovering in place with stabilization at {speed}%.")
        return None, None

    else:
        print("❌ Unknown command received. Please check input.")
        return None, "Unknown command received. Please check input."


