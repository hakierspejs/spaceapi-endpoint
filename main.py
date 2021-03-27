#!/usr/bin/env python3

import json

import flask
import requests

app = flask.Flask(__name__)


@app.route("/")
def main():
    j = requests.get("https://at.hs-ldz.pl/api/v1/users?online=true").json()
    is_open = bool(j)
    response_json = {
        "api_compatibility": ["14"],
        "contact": {
            "email": "hakierspejs [ ^ AT ^ ] d33.pl",
            "irc": "irc://irc.freenode.net/hakierspejs",
        },
        "issue_report_channels": ["email"],
        "location": {
            "address": "Zielona 30 l.u. 1, Łódź, Poland",
            "lat": 51.769522,
            "lon": 19.4451394,
        },
        "logo": (
            "https://raw.githubusercontent.com/hakierspejs/"
            "wiki/master/media-w-wiki/hakierspejs.png"
        ),
        "projects": ["https://code.hs-ldz.pl", "https://wiki.hs-ldz.pl"],
        "space": "Hakierspejs Łódź",
        "state": {"open": is_open},
        "url": "https://hs-ldz.pl",
    }
    resp = flask.Response(
        json.dumps(response_json), mimetype="application/json"
    )
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0")
