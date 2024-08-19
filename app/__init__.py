from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'senhadificil' 
login_manager = LoginManager(app)
login_manager.login_view = 'login.login'  


from app.rotas.rotas_home import blueprint_home
app.register_blueprint(blueprint_home)

from app.rotas.rotas_imoveis import blueprint_imoveis
app.register_blueprint(blueprint_imoveis)

from app.rotas.rotas_login import blueprint_login
app.register_blueprint(blueprint_login)

