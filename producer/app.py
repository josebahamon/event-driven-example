import redis
import time

r = redis.Redis(host='redis', port=6379)

while True:
    order_id = int(time.time())  # Simula un ID único
    message = f"Nuevo pedido recibido:{order_id}"
    r.publish('eventos_pedidos', message)
    print(f"Publicado: {message}")
    time.sleep(5)  # Publica un nuevo evento cada 5 segundos

