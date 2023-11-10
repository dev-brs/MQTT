import json
from paho.mqtt import client as mqtt_client

# Parâmetros de conexão TCP
host = 'test.mosquitto.org'
port = 1883
topic = 'Liberato/iotTro/44xx/data'  # Tópico MQTT utilizado para a comunicação
client_id = '20000298'  # ID do cliente
topic_ack = 'Liberato/iotTro/44xx/rply/20000298'  # Tópico para confirmação de recebimento


def is_json(string):
    try:
        json.loads(string)
    except ValueError as e:
        return False
    return True


# Função para construir a resposta em JSON
def responder(msg):
    if float(msg.get('tempInt').get('valor')) >= float(msg.get('tempExt').get('valor')):
        msg.update({"climatizado": "NAO"})
    else:
        msg.update({"climatizado": "SIM"})

    msg.pop('tempExt')
    msg.pop('tempInt')
    msg.pop('umidade')
    msg.update({"nome": "Bernardo Rodrigues da Silva"})
    msg.update({"turma": "4411"})
    msg.update({"seq": int(msg.get("seq")) + 800_000})

    return json.dumps(msg)


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
        if is_json(msg.payload.decode()):
            print(json.loads(msg.payload.decode()))
            msg_dicpy = json.loads(msg.payload.decode())
            print(f"Matricula recebida é ({msg_dicpy['matricula']})")

            if str(msg_dicpy['matricula']) == client_id:
                parsed_msg = json.loads(msg.payload.decode())
                response = responder(parsed_msg)
                print(f"Minha matricula foi recebida ({msg_dicpy['matricula']})")
                client.publish(topic_ack, response)

    client.subscribe(topic)
    client.on_message = on_message  # Definição do callback a ser utilizado


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
