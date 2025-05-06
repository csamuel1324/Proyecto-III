from flask import Blueprint, render_template, redirect, url_for, session, request, flash

main = Blueprint('main', __name__,template_folder="templates",static_url_path='/static')

@main.route('/')
def index():
    return render_template("index.html")


@main.route('/usuario')
def usuario():
    return render_template("usuario.html")


@main.route('/administrador')
def administrador():
    return render_template("administrador.html")

@main.route('/login_usuario', methods=["GET","POST"])
def login_usuario():
    username = request.form.get("username")
    password = request.form.get("password")
    print(username,",",password)
    return redirect(url_for("main.usuario"))

@main.route('/login_administrador', methods=["GET","POST"])
def login_administrador():
    flash(' python estuvo aqui')
    print("cumplido")
    username = request.form.get("username")
    password = request.form.get("password")
    print(username,",",password)
    return redirect(url_for("main.administrador"))

# @main.route('/administrador')
# def administrador():
#     return render_template("administrador.html")