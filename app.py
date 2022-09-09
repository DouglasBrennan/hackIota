from flask import Flask, request, jsonify, render_template
from interface import IotaClient
from message import Message
import json


app = Flask(__name__)


@app.route('/get_message', methods=['GET', 'POST'])
def get_message():
    if request.method == 'POST':
        message_id = request.form['message-id-input']
        return verify_message(message_id)
    return render_template('get_message.html')


@app.route('/verify_message', methods=['GET', 'POST'])
def verify_message(message_id):
    if request.method == 'POST':
        message: Message = Message.from_id(request.form)
    return render_template('verify_message.html', message=message)


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
    timestamp = request.args.get('timestamp')

    client = IotaClient()
    message = client.send_message(
        index=uuid,
        value=json.dumps({
            'sensor_id': str(uuid),
            'lux': str(lux),
            'proximity': str(proximity),
            'pressure': str(pressure),
            'temperature': str(temperature),
            'humidity': str(humidity),
            'longitude': str(longitude),
            'latitude': str(latitude),
            'altitude': str(altitude),
            'timestamp': str(timestamp)
        })
    )
    return jsonify(message)



if __name__ == '__main__':
    app.run()
