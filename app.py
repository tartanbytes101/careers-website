from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello World!\n "+ "Today's date is : "+datetime.now().strftime("%d/%m/%Y")


#__start the app
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)