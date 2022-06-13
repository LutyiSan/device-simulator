FROM   python:latest

ADD    /MQTT_SIMULATION /MQTT_SIMULATION

#RUN    apt install python3-pip

RUN    pip3 install -r /pyserver/requirements.txt

CMD    python3 /main.py