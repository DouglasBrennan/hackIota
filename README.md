# hackIota

## Functionalities:
1. Generate artificial data for further processing
2. Contains a Flask application that hosts an API writing messages from the RaspberryPi to the Iota Ledger
3. Interface methods to communicate with the Iota Ledger

## Installation
run `pip install -r requirements.txt` from the project root to install dependencies.

1. To generate artificial data, run `python generate_data.py` (change values within if you want to adapt how many sensors are created).

2. If you want to host the communicator, host this repo on your favorite Flask-hosting framework.
We used [heroku](https://www.heroku.com ) to host it.
(The necessary files are included, follow their [tutorial](https://devcenter.heroku.com/articles/getting-started-with-python) to get it running.)

3. The interface can be used where necessary. It connects to the [dev-net](http://wiki.iota.org/introduction/reference/networks/devnet) ledger.