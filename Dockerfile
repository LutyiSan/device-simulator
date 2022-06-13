FROM   python:latest

ADD    /simulator /simulator

#RUN    apt install python3-pip

RUN    pip3 install -r /pyserver/requirements.txt

CMD    python3 /main.py