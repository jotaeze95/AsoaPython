from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

for i in range(1, 1000001):
    return(i) 

if __name__ == "__main__":
    application.run()
