from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "h1>bem-vindo à página inicial !!</h1>"

@app.route('/sobre')
def sobre():
    return "h1>a página é sobre o curso de python pro , com o professor tio leo</h1>"

@app.route("/secret")
def secret():
    return """
    <h1>🔒 página Secreta</h1>
    <p>você descobriu um lugar escondido do meu site!</p>
    <p>obrigado por visitar !</p>
    """
app.run(debug=True)
