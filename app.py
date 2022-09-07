from flask import Flask, request, jsonify
from interface import IotaClient
import json

app = Flask(__name__)


@app.route('/conditions')
def write_to_tangle():  # put application's code here
    uuid = request.args.get('uuid')
    lux = request.args.get('lux')
    proximity = request.args.get('proximity')
    pressure = request.args.get('pressure')
    temperature = request.args.get('temperature')
    humidity = request.args.get('humidity')
    longitude = request.args.get('longitude')
    latitude = request.args.get('latitude')
    altitude = request.args.get('altitude')

    client = IotaClient()
    message = client.send_message(
        index=uuid,
        value=json.dumps({
            'lux': str(lux),
            'proximity': str(proximity),
            'pressure': str(pressure),
            'temperature': str(temperature),
            'humidity': str(humidity),
            'longitude': str(longitude),
            'latitude': str(latitude),
            'altitude': str(altitude),
        })
    )
    return jsonify(message)


if __name__ == '__main__':
    app.run()
