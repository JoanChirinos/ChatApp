#! /usr/bin/python3

from urllib.parse import parse_qs as pqs

from flask import (Flask, render_template, redirect, url_for,
                   session, request, flash, get_flashed_messages)

from util import db

app = Flask(__name__)
app.secret_key = 'beans'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_messages/<chat>')
def get_messages(chat):
    msgs = db.get_messages(chat)
    out = ''
    for msg in msgs:
        out += '<p>- {}</p>'.format(msg[0])
    return out


@app.route('/send_message/<chat>/<message>')
def send_message(chat, message):
    msg = pqs('msg={}'.format(message))['msg'][0]
    db.add_message(chat, msg)
    return ''


if __name__ == '__main__':
    app.debug = True
    app.run()
