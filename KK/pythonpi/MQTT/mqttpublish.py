import paho.mqtt.publish as publish

# publish a message then disconnect.
host = "localhost"
topic = "tw/rocksaying"
payload = "hello mqtt"

# If broker asks user/password.
auth = {'username': "", 'password': ""}

# If broker asks client ID.
client_id = ""

publish.single(topic, payload, qos=1, hostname=host)

#publish.single(topic, payload, qos=1, host=host,
#    auth=auth, client_id=client_id)