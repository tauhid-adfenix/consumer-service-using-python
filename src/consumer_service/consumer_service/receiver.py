import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='127.0.0.1'))
channel = connection.channel()


channel.queue_declare(queue='rabittmq.test.queue')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()