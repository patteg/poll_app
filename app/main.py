from flask import Flask
from aqi_newspaper import poll_check

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to the pollution polling app! Tagged as latest."
    #return check_poll()

@app.route("/chow")
def call_poll():
    #return "it works"
    poll_value, poll_time = poll_check()
    return "poll value = " + poll_value + " poll_time = " + poll_time

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3035)
