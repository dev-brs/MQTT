This project involves three Python scripts working together to establish an IoT system using MQTT (Message Queuing Telemetry Transport). The MQTT Subscriber Script (mqtt_subscriber.py) connects to an MQTT broker, subscribes to specific topics, and processes incoming JSON messages. The MQTT Publisher and Responder Script (mqtt_publisher_responder.py) also connects to the MQTT broker, subscribes to a different topic, generates responses to incoming messages, and publishes them to a designated acknowledgment topic. Additionally, there's a Flask Web Application (mqtt_web_app.py) that allows users to input a nickname, MQTT topic, and message. This information is then sent to the MQTT broker, enabling manual interaction with the MQTT system through a user-friendly web interface. Together, these scripts form a cohesive system for MQTT communication in an IoT environment.
The development of this project originated from my electronics course. The professor, instructing the Microcontroller discipline, tasked us with responding to roll call. This roll call was published in a designated MQTT-Topic. To fulfill the assignment, we had to receive the message sent by the professor, fill in specific blanks, and send it back for verification. If the message we sent was correct, we received a new message with the acknowledgment: OK.
