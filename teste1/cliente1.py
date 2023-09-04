import os
import pika
import sys


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    def callback(ch, method, properties, body):
        body = str(body, 'utf-8')
        print(f"Recebido: {body}")

    channel.basic_consume(queue='cliente_1', on_message_callback=callback, auto_ack=True)

    print('Esperando por mensagens. Pressione CTRL+C para sair')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
