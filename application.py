from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return """<html>
        <body>
            <h1>Лабораторна робота 1</h1>
            <h2>Виконав Корнійчук Віталій ІПЗ-21-5</h2>
        </body>
    </html>"""
