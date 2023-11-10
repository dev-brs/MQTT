import json
from paho.mqtt import client as mqtt_client

# Parâmetros de conexão TCP
host = 'test.mosquitto.org'
port = 1883
topic = 'Liberato/iotTro/44xx/ack/20000298'  # Tópico MQTT para confirmação de recebimento
client_id = 'abcdefg'  # ID do cliente


def is_json(string):
    try:
        json.loads(string)
    except ValueError as e:
        return False
    return True


# Função para estabelecer conexão com o broker
def connect_mqtt():
    # Callback para quando a conexão com o broker é estabelecida
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Conexão estabelecida com sucesso!")
        else:
            print(f"FALHA NA CONEXÃO, ERRO: {rc}")

    client = mqtt_client.Client(client_id)  # Criação do objeto do cliente
    client.on_connect = on_connect  # Atribuição do callback ao objeto
    client.connect(host, port)  # Conexão com o broker
    return client


# Função para se inscrever em um tópico no broker
def subscribe(client: mqtt_client):
    # Callback para quando uma mensagem é recebida
    def on_message(client, userdata, msg):
        print(msg.payload.decode())  # Exibe a mensagem recebida
        if is_json(msg.payload.decode()):  # Verifica se a string recebida é um JSON
            print(json.loads(msg.payload.decode()))
            msg_dicpy = json.loads(msg.payload.decode())  # Decode de binário e conversão para dicionário Python

    client.subscribe(topic)  # Efetua a inscrição no tópico
    client.on_message = on_message  # Define o callback a ser utilizado


def run():
    client = connect_mqtt()  # Cria um objeto de cliente
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
