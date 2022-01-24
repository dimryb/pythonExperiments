from client2 import Client


client = Client("127.0.0.1", 8889, timeout=15)

print(client.get("*"))
print(client.get("palm.cpu"))
print(client.get("super.cpu"))
# print(client.get("geta palm.cpu"))
print(client.get("eardrum.cpu"))


# client = Client("127.0.0.1", 8888, timeout=15)
client.put("palm.cpu", 0.5, timestamp=1150864247)
client.put("palm.cpu", 2.0, timestamp=1150864248)
client.put("palm.cpu", 0.5, timestamp=1150864248)
client.put("eardrum.cpu", 3, timestamp=1150864250)
client.put("eardrum.cpu", 4, timestamp=1150864251)
client.put("eardrum.memory", 4200000)
print(client.get("*"))
client.put(metric='palm.cpu', value=0.5, timestamp=1150864247)
client.put(metric='temperature', value=79.3, timestamp=1604844181)

