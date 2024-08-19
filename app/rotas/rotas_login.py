from flask import render_template, redirect, url_for, request , Blueprint
from flask_login import login_user, login_required, logout_user
from app import login_manager
from app.models.models_usuario import User, get_user , get_all_users

blueprint_login = Blueprint('login',__name__)

@login_manager.user_loader
def load_user(user_id):
    return get_user(user_id)

@blueprint_login.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        users_list = get_all_users()
        for user in users_list:
            if user.usuario == usuario: 
                if user.senha == senha:
                    login_user(user)
                    return redirect(url_for('imoveis.home'))
                else:
                    return render_template('login_painel.html' , erro_senha='A senha que você inseriu está incorreta.')
        else:
            return render_template('login_painel.html' , erro_usuario='Usuario não encontrado')
    return render_template('login_painel.html')


@blueprint_login.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.home'))


