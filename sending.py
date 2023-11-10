from flask import Flask, render_template, request
import paho.mqtt.publish as publish

app = Flask(__name__)

# Parâmetros de conexão TCP
host = 'test.mosquitto.org'
port = 1883


def send_mqtt_message(nickname, topic, payload):
    # Envia uma mensagem para o broker MQTT
    final_message = f"{nickname}: {payload}"
    publish.single(topic, final_message, hostname=host, port=port)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nickname = request.form['nickname']
        topic = request.form['topic']
        message = request.form['message']
        send_mqtt_message(nickname, topic, message)
        return render_template('index.html', message_sent=True)
    return render_template('index.html', message_sent=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
