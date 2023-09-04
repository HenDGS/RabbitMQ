import time

import pika
import psutil

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='pc', exchange_type='topic', durable=True)

while True:
    ram_usage = psutil.virtual_memory().percent
    ram_usage = f'Uso de RAM: {str(ram_usage)}'
    channel.basic_publish(exchange='pc', routing_key='ram', body=ram_usage)
    print(f"Enviado: {ram_usage}")
    time.sleep(10)

connection.close()
