from flask import Flask
from time import time
application = Flask(__name__)

@application.route("/")
def hello():
   print )"Contador de numeros Python"=

    start_time = time()
    for i in range(1, 1000001):
        print (i)
    end_time = time() - start_time
    return ("Tiempo de ejecucion: %.10f seconds." % end_time)
    

if __name__ == "__main__":
    application.run()
