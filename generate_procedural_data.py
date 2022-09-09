import datetime

from generate_data import Sensor, DEFAULT_PARAMETERS
from interface import IotaClient

SENSOR_INDICES = [
    '44d1e2d2-0e8a-4c23-a370-608a440490d0',
    '46fbfa01-c40d-45dc-973f-192973fdbe0b',
    '32dc1582-dd63-4332-871e-f664f87ce3a1',
]


def generate_procedural_data():
    """generates data for a given amount of sensors"""
    client = IotaClient()
    sensors = [Sensor(length=1, parameters=DEFAULT_PARAMETERS, id=sensor_id) for sensor_id in SENSOR_INDICES]
    while True:
        start_time = datetime.datetime.now()
        for sensor in sensors:
            sensor.set_representative_values()
        end_time = datetime.timedelta(seconds=1)
        while datetime.timedelta(seconds=1):
            time.sleep(0.5)


if __name__ == '__main__':
    generate_procedural_data()
