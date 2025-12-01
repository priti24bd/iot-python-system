from sensor_reader import SensorReader
from device_controller import DeviceController
from mqtt_client import MQTTClient
import time

def main():
    sensor = SensorReader()
    device = DeviceController()
    mqtt_client = MQTTClient()

    print("🚀 IoT Python System Started...")

    while True:
        temperature = sensor.read_temperature()
        humidity = sensor.read_humidity()

        data = {
            "temperature": temperature,
            "humidity": humidity
        }

        print("Sensor Data:", data)

        mqtt_client.publish("iot/data", str(data))

        # Example automation:
        if temperature > 30:
            device.turn_fan_on()
        else:
            device.turn_fan_off()

        time.sleep(2)

if _name_ == "_main_":
    main()
