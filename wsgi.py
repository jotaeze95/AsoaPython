from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Contador de numeros Python"

def contar():
    for i in range(1, 1000001):
        return (i)

start_time = time()
contar()
end_time = time() - start_time
def resul(end_time):
    return ("Tiempo de ejecucion: %.10f seconds." % end_time)
    

if __name__ == "__main__":
    application.run()
