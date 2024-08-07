from flask import Flask

app = Flask(__name__)


from app.rotas.rotas_home import blueprint_home
app.register_blueprint(blueprint_home)

from app.rotas.rotas_imoveis import blueprint_imoveis
app.register_blueprint(blueprint_imoveis)






#from app.rotas import rotas_login
