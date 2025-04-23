from flask import Flask,request,render_template,redirect
import database
app = Flask(__name__)
app.secret_key = "lol"
ALUNO = "Rafael Italiano"
LED = 1 

@app.route("/")
def led():
    if request.method == "GET":
        ultrassom = database.pegar_ultrassom()
        return render_template("led.html",ultrassom=ultrassom)
    
@app.route("/ligar")
def ligar_led():
    database.inserir_ou_atualizar_estado(ALUNO,LED,"Ligado")
    return redirect("/")

@app.route("/desligar")
def desligar_led():
    database.inserir_ou_atualizar_estado(ALUNO,LED,"Desligado")
    return redirect("/")
    
if __name__== "__main__":
    app.run(debug=True)