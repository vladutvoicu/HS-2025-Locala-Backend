import requests

# Replace with the actual IP address of your ESP8266
ESP_IP = "http://192.168.0.118"  # Use the IP address printed by your ESP8266 after connection

# Command mapping (0 = THROTTLE, 1 = ROLL, 2 = PITCH, 3 = YAW, 4 = ARM)
COMMAND_MAP = {
    0: "THROTTLE",
    1: "ROLL",
    2: "PITCH",
    3: "YAW",
    4: "ARM"
}


def update_esp_channel(channel: int, value: int):
    """Sends a GET request to the ESP8266 API to update a channel."""
    try:
        response = requests.get(f"{ESP_IP}/set?ch={channel}&val={value}", timeout=3)

        if response.status_code == 200:
            print(f"✅ Successfully updated channel {channel} with value {value}")
        else:
            print(f"❌ Failed to update channel {channel}")
            print("Error:", response.text)

    except requests.RequestException as e:
        print(f"⚠️ Connection error: {e}")


# Continuous loop to read user input
while True:
    try:
        # Read numeric command from user
        print("Enter command by number:")
        print("0 - THROTTLE")
        print("1 - ROLL")
        print("2 - PITCH")
        print("3 - YAW")
        print("4 - ARM")
        print("'exit' to quit the program")

        command_input = input("Enter command (0, 1, 2, 3, 4): ").strip()

        # Exit condition
        if command_input.lower() == "exit":
            print("🚪 Exiting the program.")
            break

        # Check if the command input is a valid number
        if not command_input.isdigit():
            print("❌ Invalid input! Please enter a number between 0 and 4.")
            continue

        command = int(command_input)

        if command not in COMMAND_MAP:
            print("❌ Invalid command! Please enter a number between 0 and 4.")
            continue

        # Read value from user
        value_input = input("Enter value (e.g., 1000-2000): ").strip()

        if not value_input.isdigit():
            print("❌ Invalid value! Enter a number between 1000-2000.")
            continue

        value = int(value_input)
        if not (1000 <= value <= 2000):
            print("❌ Value out of range! Enter a number between 1000-2000.")
            continue

        # Send command to ESP8266
        print(f"Command: {COMMAND_MAP[command]}, Value: {value}")
        update_esp_channel(command, value)

    except KeyboardInterrupt:
        print("\n🚪 Exiting due to keyboard interrupt.")
        break
