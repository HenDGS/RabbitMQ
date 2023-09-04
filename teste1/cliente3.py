import pika
import sys
import os


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # channel.queue_bind(exchange='pc', queue='cliente_3', routing_key='cpu')
    # channel.queue_bind(exchange='pc', queue='cliente_3', routing_key='ram')

    def callback(ch, method, properties, body):
        body = str(body, 'utf-8')
        print(f"Recebido: {body}")

    channel.basic_consume(queue='cliente_3', on_message_callback=callback, auto_ack=True)

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
