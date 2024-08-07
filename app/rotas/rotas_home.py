from flask import render_template, redirect, url_for, request , Blueprint
from app.models.models_imoveis import get_all_imoveis

blueprint_home = Blueprint('home',__name__)


@blueprint_home.route('/')
def home():
    return render_template('base.html')

@blueprint_home.route('/header')
def header():
    return render_template('menu.html')


@blueprint_home.route('/imoveis')
def imoveis():
    imoveis = [imovel for imovel in get_all_imoveis() if imovel.inativo != 'True']
    return render_template('lista_imoveis.html' , imoveis=imoveis)


@blueprint_home.route('/footer')
def footer():
    return render_template('footer.html' )