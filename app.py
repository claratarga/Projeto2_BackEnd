from flask import Flask, render_template
from routes.usuario_routes import usuario_routes
from routes.auth_routes import auth_routes
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def inicio():
    return render_template("users.html")


@app.route("/profile/<int:usuario_id>")
def pagina_perfil(usuario_id):
    return render_template("profile.html")


@app.route("/login")
def pagina_login():
    return render_template("login.html")


app.register_blueprint(usuario_routes)
app.register_blueprint(auth_routes)


if __name__ == "__main__":
    app.run(debug=True)