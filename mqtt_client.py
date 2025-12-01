import paho.mqtt.client as mqtt

class MQTTClient:
    def _init_(self):
        self.client = mqtt.Client()
        self.client.connect("broker.hivemq.com", 1883, 60)

    def publish(self, topic, message):
        self.client.publish(topic, message)
        print(f"📡 Sent to {topic}: {message}")
