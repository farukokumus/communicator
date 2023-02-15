from flask import Flask, jsonify, request
from flask_basicauth import BasicAuth
import random


app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'droneport'
app.config['BASIC_AUTH_PASSWORD'] = 'password'

basic_auth = BasicAuth(app)

def generate_status():
    # Generate random values for each field
    unique_id = random.randint(0, 99999)
    latitude = round(random.uniform(-90, 90), 6)
    longitude = round(random.uniform(-180, 180), 6)
    altitude = round(random.uniform(0, 1000), 1)
    num_slots = random.randint(1, 3)
    drones = ["TRINITY", "VECTOR", "SCORPION", "EMPTY"]
    drone_slots = random.sample(drones, num_slots)
    state = random.choice(["AVAILABLE", "BUSY", "FAULTY"])

    # Create the status dictionary
    status = {
        "Unique ID": unique_id,
        "Latitude": latitude,
        "Longitude": longitude,
        "Altitude": altitude,
        "Number of slots": num_slots,
        "Drones in slots 1-3": drone_slots,
        "State": state
    }

    # Convert the status dictionary to a JSON string
    #status_json = json.dumps(status)

    return status

@app.route('/get_status', methods=['GET'])
@basic_auth.required
def get_status():
    return jsonify(generate_status())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
