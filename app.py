from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = "minha-chave-secreta"
usuarios = {
    "admin": {"senha": "1234", "nome": "Administrador", "email": "admin@email.com"}
}
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/login", methods=["GET", "POST"])
def login():
    erro = None
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]
        if usuario in usuarios and usuarios[usuario]["senha"] == senha:
            session["usuario"] = usuario
            return redirect(url_for("dashboard"))
        else:
            erro = "Usuário ou senha inválido"
    return render_template("login.html", erro=erro)
@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]
        nome = request.form["nome"]
        email = request.form["email"]
        usuarios[usuario] = {"senha": senha, "nome": nome, "email": email}
        return redirect(url_for("login"))
    return render_template("registro.html")
@app.route("/dashboard")
def dashboard():
    if "usuario" not in session:
        return redirect(url_for("login"))
    usuario = session["usuario"]
    dados = usuarios[usuario]
    return render_template("dashboard.html", nome=dados["nome"], email=dados["email"])
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(debug=True)
