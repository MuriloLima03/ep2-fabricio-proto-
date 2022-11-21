from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("teste.html")
    
@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/projetos")
def quemsomos():
    return render_template("projetos.html")
    
if __name__ == "__main__":
    app.run(debug=True)