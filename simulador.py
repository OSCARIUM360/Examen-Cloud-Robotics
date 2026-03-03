import requests
import time
import random
from datetime import datetime

URL = "https://examen-cloud-robotics.onrender.com/telemetry"

print(f"Iniciando simulación hacia {URL}...")

try:
    while True:
        payload = {
            "robot_id": "robot-01",
            "battery": random.randint(20, 100),
            "position": {
                "x": round(random.uniform(0, 10), 2),
                "y": round(random.uniform(0, 10), 2)
            },
            "status": "active"
        }

        response = requests.post(URL, json=payload)
        
        if response.status_code == 200:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Datos enviados: {payload}")
        else:
            print(f"Error: {response.status_code}")

        time.sleep(3)

except KeyboardInterrupt:
    print("\nSimulación detenida por el usuario.")