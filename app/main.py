import logging

from flask import Flask, jsonify

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok"), 200


@app.get("/add/<int:a>/<int:b>")
def add(a, b):
    log.info("add called with a=%s b=%s", a, b)
    return jsonify(result=a + b)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
    