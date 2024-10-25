from flask import Flask
from azure.storage.blob import BlobServiceClient

import os

app = Flask(__name__)


def init_client(service_client, container, blob):
    client = service_client.get_blob_client(container=container, blob=blob)
    return client


def get_value(client):
    if not client.exists():
        client.upload_blob("0")
    value = client.download_blob().readall().decode("utf-8")
    return value


def set_value(client, value):
    client.upload_blob(str(value), overwrite=True)
    return value


connection_string = os.getenv("CONNECTION_STRING")
container = os.getenv("CONTAINER_NAME")
filename = os.getenv("COUNTER_FILENAME")

service_client = BlobServiceClient.from_connection_string(connection_string)
client = init_client(service_client, container, filename)


@app.route("/stats")
def stats():
    value = get_value(client)
    return f"""<html>
        <body>
            <h1>Лабораторна робота 1, 3</h1>
            <h2>Виконав Корнійчук Віталій ІПЗ-21-5</h2>
            <p>Значення "числа": {value}</p>
        </body>
    </html>"""


@app.route("/increment")
def increment():
    value = get_value(client)
    new_value = int(value) + 1
    set_value(client, new_value)
    return """<html>
        <body>
            <h1>Лабораторна робота 1, 3</h1>
            <h2>Виконав Корнійчук Віталій ІПЗ-21-5</h2>
            <p>Ти збільшив "число" на 1!</p>
        </body>
    </html>"""
