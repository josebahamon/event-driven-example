import redis

def handle_message(message):
    print(f"[Servicio de Logística] Procesando pedido: {message['data'].decode('utf-8')}")

r = redis.Redis(host='redis', port=6379)
pubsub = r.pubsub()
pubsub.subscribe(**{'eventos_pedidos': handle_message})

print("[Servicio de Logística] Escuchando eventos...")
pubsub.run_in_thread(sleep_time=0.001)
