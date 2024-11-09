## ZeroWaste Project - Real-Time Weight Monitoring System

### Description

The ZeroWaste Project aims to ensure sustainability and efficiency in food production, with a particular focus on real-time weight monitoring throughout the production stages.
This Flask-based application helps manage weight data from the production line, provides real-time feedback to workers, and ensures that products are not underweight or overweight. This will promote efficient resource usage, improve quality control, and reduce food waste.

Screen Interface Example ![Screen Interface](/static/ScreenInterface.png "[Screen Interface") 


### Features
* Real-time weight monitoring: Display weight data for different stages of production (Raw Material, Stage 1, Stage 2, Final Product).
* Real-time communication: Use Socket.IO to communicate weight updates and predictions with workers.
* Weight prediction: A simple algorithm for predicting weight deviations based on the current weight.
* User-friendly interface: Clean and intuitive design with a multilingual-friendly interface for better inclusivity in a diverse workforce.
* API for updating weights: An endpoint for updating weights manually, allowing users to input data when necessary.
* Alerts: The system can alert when products are over or underweight to prevent food waste and production issues.

### Installation
__Prerequisites__
Make sure you have the following software installed:

- Python 3.12 or higher: The project is developed in Python 3.12. If you don’t have it, you can download and install it from the official Python website.
- pip: Python’s package installer (it is usually included with Python).

__Step-by-Step Installation__

Clone the repository (or download the source code):
```
bash

git clone https://github.com/TatianaVeda/ZeroWaste-Project.git

cd ZeroWaste
```
Create and activate a virtual environment (optional but recommended to avoid conflicts with other projects):

```
bash

python3 -m venv venv
source venv/bin/activate  # For Windows use: venv\Scripts\activate
```

Install the required Python packages:

```
bash

pip install -r requirements.txt
```
The requirements.txt file should include the following dependencies:

```
flask
flask-socketio
paho-mqtt
```

Start the MQTT broker: If you're using Mosquitto as your MQTT broker, install it by following these instructions:

```
bash

sudo apt-get install mosquitto
```
After installation, you can run the broker with:

```
bash

mosquitto
```

This will start the broker locally on port 1883. Alternatively, you can use a remote broker like Eclipse Mosquitto by setting the broker URL in your Flask application.

Running the Application
Start the Flask server: Once all dependencies are installed, run the Flask server by executing:

```
bash

python app.py
```

Access the application: Open your browser and go to:

Local: http://127.0.0.1:5000
Remote: If you are running it on a network, use the IP address provided in the console (e.g., http://172.24.33.209:5000).
Functionality
The application provides the following key features:

__1. Weight Data Display__
The main page displays the real-time weight data for various stages of production, including:

Raw Material: Initial weight of raw material before processing.
Stage 1, Stage 2: Weights at different production stages.
Final Product: Weight of the finished product.
These weights are updated in real-time through Socket.IO as the data is received.

__2. Real-Time Monitoring with Socket.IO__
The system uses Socket.IO to establish a real-time communication channel between the backend and the frontend.
Whenever a weight update occurs (either through MQTT or manually), the frontend is notified instantly, and the displayed weights are updated.

__3. Weight Prediction__
A simple algorithm is used to predict potential weight deviations based on the raw material’s weight. The prediction is calculated by introducing slight random variations and can be extended to more complex models if needed.

To request the predicted weight:

Endpoint: ```/predict_weight``` (GET)

Returns: A JSON object with the predicted weight for the raw material.

__4. Update Weight__
Endpoint: /update_weight (POST)
Data format:

```
json

{
  "stage": "raw_material",
  "new_weight": 500.5
}
```

The weight of any stage in the production process can be updated via this API.

__5. Multilingual Interface__
The interface is designed to be simple and easy to translate. You can add new languages by extending the Flask templates with translations.
Multilingual-friendly tools, such as dropdowns and text boxes, are used to ensure inclusivity.

__6. Alerts__
The system sends alerts when the weights deviate from expected thresholds (either underweight or overweight).
Alerts are shown in the "Alerts" section on the interface and can be configured for various stages.
#### Dependencies
This project uses the following libraries:

- Flask: Web framework for building the application.
- Flask-SocketIO: For real-time communication between the server and clients using WebSockets.
- Paho-MQTT: MQTT client for subscribing and publishing weight data to/from the broker.

To install all dependencies, use:

```
bash

pip install -r requirements.txt

or 

pip install flask flask-socketio paho-mqtt
```
7. To resolve the warning: "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead" and use a server suitable for production use, you can use a WSGI server such as Gunicorn or uWSGI.

Install Gunicorn into your virtual environment:

```
Bash

pip install gunicorn
```
Run your Flask application via Gunicorn:

```
Bash
gunicorn -w 4 app:app

```
Here `-w 4` means that 4 worker processes will be launched to handle requests (you can adjust this depending on the load and power of your server). `app:app` tells Gunicorn that your main Flask object is called `app` and it is located in the `app.py` file.

After that, your application will work with the server that is intended to work in a production environment and the warning will disappear.

