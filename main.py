#!/usr/bin/env python3

import flask
import requests

app = flask.Flask(__name__)


@app.route("/")
def main():
    j = requests.get("https://at.hs-ldz.pl/api/v1/users?online=true").json()
    is_open = bool(j)
    return {}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
