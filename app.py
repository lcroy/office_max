from flask import Flask, abort, request, jsonify, render_template, send_file, send_from_directory, redirect, url_for
import json
import os
from playsound import playsound
from configure import Config
from dboperation import *

app = Flask(__name__)
app.add_url_rule('/photos/<path:filename>', ...)
cfg = Config()

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

content = ''

@app.route('/get_conv/', methods=['GET'])
def get_conv():
    global content

    # get max response
    reply_result = res_max(cfg.dataset_path_db, 'read', "does_not_matter")
    for reply in reply_result:
        max_reply = reply[0]

    # check the service status
    rows = status(cfg.dataset_path_db, "check", "no_one_care", "no_one_care")
    for row in rows:
        status_results = row[0]
        user = row[1]
    # get all the un-read messages
    unread_message = {'Ole':0, 'Simon':0, 'Dimi':0, 'Morten':0, 'Casper':0, 'Chen':0, 'Status': status_results, 'user': user, 'Max': max_reply}
    operation = "check"
    sender = ""
    receiver = ""
    record_file_path = ""
    id = 0
    rows = save_record_to_db(cfg.dataset_path_db, id, sender, receiver, record_file_path, operation)
    if rows == "null":
        pass
    else:
        for row in rows:
            unread_message[row[0]] = row[1]

    print(unread_message)

    return jsonify(unread_message)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
