from interface import IotaClient


class Message:
    def __init__(self, message_id, lux, proximity, pressure, temperature, humidity, longitude, latitude,
                 timestamp):
        self.message_id = message_id
        self.lux = lux
        self.proximity = proximity
        self.pressure = pressure
        self.temperature = temperature
        self.humidity = humidity
        self.longitude = longitude
        self.latitude = latitude
        self.timestamp = timestamp

    @classmethod
    def from_response(cls, response):
        print(response)
        return cls(
            message_id=response['message_id'],
            lux=response['lux'],
            proximity=response['proximity'],
            pressure=response['pressure'],
            temperature=response['temperature'],
            humidity=response['humidity'],
            longitude=response['longitude'],
            latitude=response['latitude'],
            timestamp=response['timestamp'],
        )

    @classmethod
    def from_id(cls, response):
        message_id = response['message-id-input']
        print(message_id)
        client = IotaClient()
        message = client.get_message_by_id(message_id)
        payload = client.get_message_payload(message)
        print(payload)
        return cls(
            message_id=message_id,
            lux=payload['lux'],
            proximity=payload['proximity'],
            pressure=payload['pressure'],
            temperature=payload['temperature'],
            humidity=payload['humidity'],
            longitude=payload['longitude'],
            latitude=payload['latitude'],
            timestamp=payload['timestamp'],
        )
