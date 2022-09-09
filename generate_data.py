import datetime
import json
import uuid
import random

import tqdm

from interface import IotaClient


class Parameter:
    """Represents a parameter"""

    def __init__(self, minimum: float, maximum: float):
        self.minimum = minimum
        self.maximum = maximum
        self.values: list[float] = []

    def set_representative_values(self, length: int) -> None:
        """Returns representative values of a given length within the specified range."""
        values = []
        fluctuation = (self.maximum - self.minimum) * 0.1
        previous_value = random.uniform(self.minimum, self.maximum)
        for _ in range(length):
            lower_boundary = previous_value - fluctuation if previous_value - fluctuation > self.minimum else self.minimum
            upper_boundary = previous_value + fluctuation if previous_value + fluctuation < self.maximum else self.maximum
            value = random.uniform(lower_boundary, upper_boundary)
            values.append(value)
            previous_value = value
        self.values = values


class Sensor:
    """Represents a sensor"""

    def __init__(self, length: int, parameters: dict[str, Parameter], id: str = None):
        self.id = str(uuid.uuid4()) if id is None else id
        self.longitude = random.uniform(8.49768, 8.54104)
        self.latitude = random.uniform(47.36362, 47.37809)
        self.observation_length = length
        self.parameters = parameters
        self.timestamps: list[int] = self.set_timestamps()

    def set_representative_values(self):
        """Sets representative values for each parameter."""
        for parameter in self.parameters.values():
            parameter.set_representative_values(self.observation_length)

    def set_timestamps(self) -> list[int]:
        """Sets timestamps from now - length*minutes to now"""
        base = datetime.datetime.now()
        datetimes = [base - datetime.timedelta(minutes=x) for x in range(self.observation_length)]
        return [int(date.timestamp()) for date in datetimes]

    def write_to_tangle(self, client: IotaClient):
        """Writes each observation to the tangle as a message with the sensor id as index."""
        for i in tqdm.trange(self.observation_length):
            observation = {}
            for parameter in self.parameters.keys():
                observation[parameter] = self.parameters[parameter].values[i]
            observation['longitude'] = self.longitude
            observation['latitude'] = self.latitude
            observation['timestamp'] = self.timestamps[i]
            observation['sensor_id'] = self.id
            observation_str = json.dumps(observation)
            client.send_message(self.id, observation_str)


def fabricate_sensors(count: int):
    """fabricates sensor instances"""
    return [Sensor(length=100, parameters=DEFAULT_PARAMETERS) for _ in range(count)]


# Default sensor parameters
DEFAULT_PARAMETERS = {
    'temperature': Parameter(minimum=15, maximum=25),
    'humidity': Parameter(minimum=30, maximum=50),
    'lux': Parameter(minimum=0, maximum=50),
    'proximity': Parameter(minimum=0, maximum=50),
    'pressure': Parameter(minimum=900, maximum=1010),
}


def generate_data(sensor_count: int):
    """generates data for a given amount of sensors"""
    client = IotaClient()
    sensors = [Sensor(length=10, parameters=DEFAULT_PARAMETERS, id='5d4d6c49-9969-47dd-8f95-f6eb1a412939')]
    # sensors = fabricate_sensors(count=sensor_count)
    for sensor in sensors:
        sensor.set_representative_values()
        sensor.write_to_tangle(client)
    print(f'sensor ids: \n {[sensor.id for sensor in sensors]}')


if __name__ == '__main__':
    generate_data(sensor_count=5)
