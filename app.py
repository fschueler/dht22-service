from flask import Flask
import Adafruit_DHT
import json
app = Flask(__name__)

sensor = Adafruit_DHT.DHT22
pin = 4

@app.route('/')
def index():
  return 'DHT Sensor App v0.1'

@app.route('/api/read')
def temp():
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
  obj = {"humiditiy": humidity, "temperature": temperature } 
  return json.dumps(obj)
