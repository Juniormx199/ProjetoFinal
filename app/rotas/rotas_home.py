from flask import render_template, redirect, url_for, request , Blueprint
from app.models.models_imoveis import get_all_imoveis

blueprint_home = Blueprint('home',__name__)


@blueprint_home.route('/')
def home():
    imoveis_venda = [imovel for imovel in get_all_imoveis() 
            if (imovel.inativo != 'Sim' 
                and imovel.classificado == 'venda'
                and imovel.destaque == 'Sim'
            )]
    imoveis_locacao = [imovel for imovel in get_all_imoveis() 
            if (imovel.inativo != 'Sim' 
                and imovel.classificado == 'locacao'
                and imovel.destaque == 'Sim'
            )]
    return render_template('base.html', imoveis_venda=imoveis_venda , imoveis_locacao=imoveis_locacao)

@blueprint_home.route('/header')
def header():
    return render_template('menu.html')



@blueprint_home.route('/footer')
def footer():
    return render_template('footer.html' )