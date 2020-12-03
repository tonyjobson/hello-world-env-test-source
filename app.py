import os
from flask import Flask
app = Flask(__name__)

envuser = os.environ.get('USER')
envpass = os.environ.get('PASS')

if not envuser:
    envuser = "Lazy_dev_did_not_set_USER_default_DevUser"

if not envpass:
    envpass = "Lazy_dev_did_not_set_PASS_default_DevPass"

@app.route("/")
def main():
    return "Welcome! I was started with a Username of " + envuser + " and i was started with a password of: " + envpass + " thanks for stoping by. T."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)