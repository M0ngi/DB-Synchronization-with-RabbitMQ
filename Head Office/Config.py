import pika


class Config:
    RMQ_CONNECTION = pika.ConnectionParameters("localhost", heartbeat=0)

