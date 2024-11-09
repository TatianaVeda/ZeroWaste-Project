from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import random
import time
import paho.mqtt.client as mqtt

app = Flask(__name__)
socketio = SocketIO(app)

# MQTT setup
mqtt_broker = "test.mosquitto.org"
mqtt_topic = "production/stage_1/weight"

# Example data (can be replaced with real measurements)
weights = {
    'raw_material': 1000,  # starting raw weight
    'stage_1': 500,        # stage 1 weight
    'stage_2': 200,        # stage 2 weight
    'final_product': 100   # final product weight
}

# Simple machine learning model (for demonstration)
def predict_weight(current_weight):
    # A simple algorithm that just returns weight deviation (can be replaced with more complex ML)
    predicted_weight = current_weight + random.uniform(-5, 5)  # Predicting deviations
    return predicted_weight

# Main page
@app.route('/')
def index():
    return render_template('index.html')

# API to get current weights
@app.route('/get_weights', methods=['GET'])
def get_weights():
    return jsonify(weights)

# API to update weight
@app.route('/update_weight', methods=['POST'])
def update_weight():
    stage = request.json.get('stage')
    new_weight = request.json.get('new_weight')
    
    if stage in weights:
        weights[stage] = new_weight
        return jsonify({"status": "success", "message": "Weight updated"})
    return jsonify({"status": "error", "message": "Invalid stage"})

# Real-time data sending using SocketIO
@socketio.on('connect')
def handle_connect():
    print("Client connected")
    emit('weights_update', weights, broadcast=True)

# Handler for predicting weight
@app.route('/predict_weight', methods=['GET'])
def predict():
    current_weight = weights['raw_material']  # Using initial raw material weight
    predicted_weight = predict_weight(current_weight)
    return jsonify({"predicted_weight": predicted_weight})

# MQTT client message handler
def on_message(client, userdata, msg):
    weight = msg.payload.decode()
    print(f"Received weight: {weight} kg")
    # Send data to frontend using SocketIO
    socketio.emit('new_weight', {'weight': weight})

# MQTT client setup
mqtt_client = mqtt.Client()
mqtt_client.on_connect = lambda client, userdata, flags, rc: client.subscribe(mqtt_topic)
mqtt_client.on_message = on_message

mqtt_client.connect(mqtt_broker, 1883, 60)
mqtt_client.loop_start()

# Running the application
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
