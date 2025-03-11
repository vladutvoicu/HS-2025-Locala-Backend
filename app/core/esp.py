import requests


class ESPController:
    def __init__(self, esp_ip: str):
        self.esp_ip = esp_ip
        self.session = requests.Session()  # Persistent session

    def update_channel(self, channel: int, value: int):
        try:
            response = self.session.get(f"{self.esp_ip}/set?ch={channel}&val={value}", timeout=3)
            if response.status_code == 200:
                print(f"✅ Successfully updated channel {channel} with value {value}")
            else:
                print(f"❌ Failed to update channel {channel}: {response.text}")
        except requests.RequestException as e:
            print(f"⚠️ Connection error: {e}")

    def close(self):
        self.session.close()
        print("🔌 ESP session closed.")


# ✅ Singleton instance of ESPController
ESP_IP = "http://192.168.194.250"  # Replace with actual IP
esp_controller = ESPController(ESP_IP)
