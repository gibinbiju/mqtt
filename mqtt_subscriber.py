import json
import paho.mqtt.client as mqtt 
import sys,time

#Global Variable declaration
connected = False

def mqtt_conn(params):
    assert params is not None, "param mqtt_conn_info missing"
    broker    = params.get("broker")
    topic     = params.get("topic")
    port      = params.get("port")
    qos       = params.get("qos")
    keepalive = params.get("keepalive")
    return broker,topic,port,qos,keepalive


def on_connect(client, userdata, flags, rc):
    global connected 
    if rc==0:
        connected = True

    else:
        connected = False

def on_publish(client, userdata, mid):
    # print(client,userdata,mid)
    pass

def on_disconnect(client, userdata, rc):
    connected = False
    print("disconnected from broker")

def on_subscribe(client, userdata, mid):
    print(client,userdata,mid)

def on_message(client,userdata,msg):
    print(msg.payload.decode(),"from topic {}".format(msg.topic))

def main():
    if client_info:
        cid = client_info.get("client_id")
        protocol = client_info.get("protocol")
    else:
        cid = topic
        protocol = 3

    
    mqtt_client = mqtt.Client(client_id=cid,protocol=protocol,clean_session=False)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_disconnect = on_disconnect
    mqtt_client.on_subscribe = on_subscribe
    mqtt_client.on_message = on_message
    # mqtt_client.on_log = on_log

    try:
        mqtt_client.connect(broker,port,keepalive)
    except Exception as e:
        print(e)
        pass
    try:
        mqtt_client.loop_start()
        sub_topic = params.get("subscribe_topic")[0]
        while True:
            mqtt_client.subscribe(sub_topic,qos)
            time.sleep(1)
    except Exception as e:
        print(e)
        pass
    except KeyboardInterrupt:
        mqtt_client.loop_stop()
        mqtt_client.disconnect()
        sys.exit()
if __name__ == "__main__":
    try:
        with open(sys.argv[1],"r+") as fp:
            params   = json.load(fp)
    except Exception as e:
        print("exception in loading conf file- {}".format(repr(e)))
        pass
    broker,topic,port,qos,keepalive = mqtt_conn(params.get("mqtt_conn_info"))
    client_info = params.get("mqtt_client")
    main()