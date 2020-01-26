# DHT22 web service

A small service that allows you to query temperature and humidity readings from a DHT22 sensor running on a Raspberry Pi.

For setup instructions I have used [this tutorial](https://tutorials-raspberrypi.de/raspberry-pi-luftfeuchtigkeit-temperatur-messen-dht11-dht22/) which unfortunately is in German, but you can find setup instructions in other languages online.

The current app is hardcoded to the GPIO pin number used in the tutorial (4).

# Development

1. Clone the repository:
`git clone git@github.com:fschueler/dht22-service.git`

2. Create and activate a new virtual environment
```bash
python3 -m venv venv
. venv/bin/activate
```

3. Install dependencies
`pip install -r requirements.txt`

**Notice:** The Adafruit-DHT library expects to be run on a Raspberry Pi or Beaglebone Black. Installation fails when it doesn't run on one of these. To force installation, execute `pip install Adafruit-DHT --install-option="--force-pi"` separately.

4. Run the app
```bash
export FLASK_APP=app.py
flask run --host=0.0.0.0
```

5. Collect sensor readings
`curl -X GET localhost:5000/api/read`

This will fail if you're not running on a supported platform (Raspberry Pi or Beaglebone Black). Alternatively, test your app with a call to the server: `curl -X GET localhost:5000/`.