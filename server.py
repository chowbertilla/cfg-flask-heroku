from flask import Flask, render_template, request
from send_message import send_message

app = Flask("Email sender")

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
  form_data = request.form

  send_message(form_data["email"], form_data["message"])

  return "Greeting sent!"

# app.run(debug=True) Reason this needs to be removed is because Heroku already has a way to run it - app.run is local - we don't want it to run locally as this wil confuse Heroku
