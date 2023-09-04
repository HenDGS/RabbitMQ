import psutil
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='pc', exchange_type='topic', durable=True)

while True:
    cpu_usage = psutil.cpu_percent(interval=10)
    cpu_usage = f'Uso de CPU: {str(cpu_usage)}'
    channel.basic_publish(exchange='pc', routing_key='cpu', body=cpu_usage)
    print(f"Enviado: {cpu_usage}")

connection.close()
