from flask import Flask, render_template, request, Blueprint , url_for , redirect
from app.models.models_imoveis import *
from app import app
from flask_dropzone import Dropzone
from flask import jsonify
import os
import logging
import shutil

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Configuração do logging
logging.basicConfig(level=logging.DEBUG)  # Define o nível de log como DEBUG
logger = logging.getLogger(__name__)

basedir = os.path.abspath(os.path.dirname('__main__'))

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'app', 'static', 'imagens' ,'cod_imoveis'),
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=20,
    DROPZONE_UPLOAD_ON_CLICK=True,
    DROPZONE_DEFAULT_MESSAGE = "Arraste os arquivos aqui ou clique para fazer upload"
)

dropzone = Dropzone(app)

blueprint_imoveis = Blueprint('imoveis', __name__)

@blueprint_imoveis.route('/imoveis/')
def home():
    return render_template('painel_imoveis.html')

@blueprint_imoveis.route('/imoveis/new', methods=["POST"])
def criar():
    if request.method == 'POST':
        data = request.get_json()
        tipo = data.get('tipo')
        valor_venda = float(data.get('valor_venda', 0))
        valor_locacao = float(data.get('valor_locacao', 0))
        valor_condominio = float(data.get('valor_condominio', 0))
        informacoes = data.get('informacoes', '')
        descricao = data.get('descricao', '')
        rua = data.get('rua', '')
        bairro = data.get('bairro', '')
        numero = data.get('numero', '')
        cidade = data.get('cidade', '')
        cep = data.get('cep', '')
        uf = data.get('uf', '')
        area = data.get('area', '')
        quartos = data.get('quartos', '')
        banheiros = data.get('banheiros', '')
        vagas = data.get('vagas', '')
        suites = data.get('suites', '')
        codigo = data.get('codigo', '')
        destaque = data.get('destaque') == 'sim'
        classificado = data.get('classificado')
        inativo = data.get('inativo') == 'sim'

        comodidades = {
            "academia": data.get('academia', 'Não'),
            "estacionamento": data.get('estacionamento', 'Não'),
            "elevador": data.get('elevador', 'Não'),
            "areaLazer": data.get('areaLazer', 'Não'),
            "salaoFestas": data.get('salaoFestas', 'Não'),
            "churrasqueira": data.get('churrasqueira', 'Não'),
            "portaria24h": data.get('portaria24h', 'Não'),
            "quadraEsportes": data.get('quadraEsportes', 'Não'),
            "playground": data.get('playground', 'Não'),
            "jardim": data.get('jardim', 'Não'),
            "salaJogos": data.get('salaJogos', 'Não'),
            "espacoGourmet": data.get('espacoGourmet', 'Não'),
            "sauna": data.get('sauna', 'Não'),
            "brinquedoteca": data.get('brinquedoteca', 'Não'),
            "espacoCoworking": data.get('espacoCoworking', 'Não'),
            "petPlace": data.get('petPlace', 'Não'),
            "bicicletario": data.get('bicicletario', 'Não'),
            "lavanderia": data.get('lavanderia', 'Não'),
            "geradorEnergia": data.get('geradorEnergia', 'Não'),
            "sistemaSeguranca": data.get('sistemaSeguranca', 'Não'),
            "wifiAreasComuns": data.get('wifiAreasComuns', 'Não'),
            "aquecimentoCentral": data.get('aquecimentoCentral', 'Não')
        }

        if not codigo:
            codigo = ultimo_codigo()

        imovel = Imovel(
            pk=0, codigo=codigo, descricao=descricao, tipo=tipo, valor_locacao=valor_locacao,
            valor_venda=valor_venda, valor_condominio=valor_condominio, informacoes=informacoes,
            rua=rua, bairro=bairro, numero=numero, cidade=cidade, area=area,
            quartos=quartos, banheiros=banheiros, vagas=vagas, suites=suites,
            destaque=destaque, classificado=classificado, inativo=inativo, cep=cep, uf=uf
        )
        
        retorno = cadastrar_imovel(imovel, comodidades)
        return {'pk': retorno}

@blueprint_imoveis.route('/imoveis/update', methods=["PUT"])
def atualizar():
     if request.method == 'PUT':
        data = request.json
        pk = data.get('pk')
        tipo = data.get('tipo')
        valor_locacao = data.get('valor_locacao')
        valor_venda = data.get('valor_venda')
        valor_condominio = data.get('valor_condominio')
        informacoes = data.get('informacoes')
        descricao = data.get('descricao')
        rua = data.get('rua')
        bairro = data.get('bairro')
        numero = data.get('numero')
        cidade = data.get('cidade')
        area = data.get('area')
        quartos = data.get('quartos')
        banheiros = data.get('banheiros')
        vagas = data.get('vagas')
        suites = data.get('suites')
        codigo = data.get('codigo')
        destaque = data.get('destaque' , 'Não')
        classificado = data.get('classificado', 'ambos')
        inativo = data.get('inativo')
        uf = data.get('uf')
        cep = data.get('cep')
        
        comodidades = {
            "academia": data.get('academia', 'Não'),
            "estacionamento": data.get('estacionamento', 'Não'),
            "elevador":  data.get('elevador', 'Não'),
            "areaLazer":  data.get('areaLazer', 'Não'),
            "salaoFestas":  data.get('salaoFestas', 'Não'),
            "churrasqueira":  data.get('churrasqueira', 'Não'),
            "portaria24h":  data.get('portaria24h', 'Não'),
            "quadraEsportes":  data.get('quadraEsportes', 'Não'),
            "playground":  data.get('playground', 'Não'),
            "jardim":  data.get('jardim', 'Não'),
            "salaJogos":  data.get('salaJogos', 'Não'),
            "espacoGourmet":  data.get('espacoGourmet', 'Não'),
            "sauna":  data.get('sauna', 'Não'),
            "brinquedoteca":  data.get('brinquedoteca', 'Não'),
            "espacoCoworking":  data.get('espacoCoworking', 'Não'),
            "petPlace":  data.get('petPlace', 'Não'),
            "bicicletario":  data.get('bicicletario', 'Não'),
            "lavanderia":  data.get('lavanderia', 'Não'),
            "geradorEnergia":  data.get('geradorEnergia', 'Não'),
            "sistemaSeguranca":  data.get('sistemaSeguranca', 'Não'),
            "wifiAreasComuns":  data.get('wifiAreasComuns', 'Não'),
            "aquecimentoCentral":  data.get('aquecimentoCentral', 'Não')
    }
        
        imovel = Imovel(
            pk=pk, codigo=codigo, descricao=descricao, tipo=tipo, valor_locacao=valor_locacao,
            valor_venda=valor_venda, valor_condominio=valor_condominio, informacoes=informacoes,
            rua=rua, bairro=bairro, numero=numero, cidade=cidade, area=area,
            quartos=quartos, banheiros=banheiros, vagas=vagas, suites=suites,
            destaque=destaque, classificado=classificado, inativo=inativo, cep=cep, uf=uf
        )

        #logging.debug(f"Dados recebidos - tipo: {imovel.pk}, codigo: {imovel.codigo}, valor_locacao: {imovel.valor_locacao}, valor_venda: {imovel.valor_venda}, valor_condominio: {imovel.valor_condominio}, informacoes: {imovel.informacoes}, descricao: {imovel.descricao}, rua: {imovel.rua}, bairro: {imovel.bairro}, numero: {imovel.numero}, cidade: {imovel.cidade}, area: {imovel.area}, quartos: {imovel.quartos}, banheiros: {imovel.banheiros}, vagas: {imovel.vagas}, suites: {imovel.suites}, destaque: {imovel.destaque}, classificado: {imovel.classificado}, inativo: {imovel.inativo}, cep: {imovel.cep}, uf: {imovel.uf}")
        
        update_imovel(imovel , comodidades)
        return {'pk': pk}

@blueprint_imoveis.route('/imoveis/upload/', methods=["POST"])
def imagem_upload():
    if request.method == 'POST':
        pk_imovel = request.form.get('pk_imovel')
        caminho_pasta = os.path.join(app.config['UPLOADED_PATH'], str(pk_imovel))

        if not os.path.isdir(caminho_pasta):
            os.makedirs(caminho_pasta)

        for key, f in request.files.items():
                if key.startswith('file'):
                    f.save(os.path.join(caminho_pasta, f.filename))
                    
    jsonify({'Result': 'imagem salvada com sucesso!!!'})
    


@blueprint_imoveis.route('/imoveis/delete/<int:pk_imovel>' ,methods= ['DELETE'] )
def deletar(pk_imovel):
    deletar_imovel(pk_imovel)

    caminho_pasta = os.path.join(app.config['UPLOADED_PATH'], str(pk_imovel))

    if os.path.exists(caminho_pasta):
        shutil.rmtree(caminho_pasta)


    return redirect(url_for('imoveis.home' , pagina=1))

@blueprint_imoveis.route('/imagem/delete/<int:pk_imovel>/<file>' ,methods= ['DELETE'] )
def deletar_imagem(pk_imovel , file):
    
    caminho_pasta = os.path.join(app.config['UPLOADED_PATH'], str(pk_imovel))
    path = os.path.join(caminho_pasta, file) 
    os.remove(path) 

    jsonify({'Result': 'imagem removida com sucesso!!!'})



@blueprint_imoveis.route('/imoveis/edit/<pk_imovel>')
def form_edit_imoveis(pk_imovel):
    imoveis = get_all_imoveis()
    caminho_pasta = os.path.join(app.config['UPLOADED_PATH'], str(pk_imovel))
    files = [( f) for f in os.listdir(caminho_pasta) if os.path.isfile(os.path.join(caminho_pasta, f))]

    for i , item in enumerate(imoveis):
        if str(item.pk) == str(pk_imovel):
            imovel = item
    return render_template('form_imoveis.html' , imovel=imovel , files=files)

    
@blueprint_imoveis.route('/imoveis/form/')
def form_imoveis():
    return render_template('form_imoveis.html')


@blueprint_imoveis.route('/imoveis/lista/')
def lista_imoveis():
    codigo_imovel = request.args.get('codigo_imovel','')

    if codigo_imovel != '':
        imovel = busca_imovel(codigo_imovel)
        if imovel != None:
            return render_template('painel_lista_imoveis.html' , imoveis_pagina=[imovel] , total_paginas=1 , pagina=1)


    imoveis = get_all_imoveis()
    pagina = request.args.get('pagina',1,type=int)
    quantidade_pagina = 5
    inicio = (pagina - 1) * quantidade_pagina
    final = inicio + quantidade_pagina
    total_paginas = (len(imoveis) + quantidade_pagina - 1) // quantidade_pagina
    imoveis_pagina = imoveis[inicio:final]

    return render_template('painel_lista_imoveis.html' , imoveis_pagina=imoveis_pagina , total_paginas=total_paginas , pagina=pagina)



@blueprint_imoveis.route('/imoveis/imagens/<int:pk_imovel>')
def lista_imagens(pk_imovel):
    caminho_pasta = os.path.join(app.config['UPLOADED_PATH'], str(pk_imovel))
    files = [( f) for f in os.listdir(caminho_pasta) if os.path.isfile(os.path.join(caminho_pasta, f))]
    return render_template('carrousel_painel.html' , pk_imovel=pk_imovel , files=files)


@blueprint_imoveis.route('/imoveis/form_comodidades')
def form_comodidades():
    pk_imovel = request.args.get('pk_imovel', '')
    
    if pk_imovel == '':
         return render_template('comodidades_painel.html')
    
    comodidades = busca_comodidades(pk_imovel)
    return render_template('comodidades_painel.html' ,comodidades=comodidades)



@blueprint_imoveis.route('/imoveis/quantidade_imagens')
def quantidade_imagens():
    pk_imovel = request.args.get('pk_imovel', '')
    if pk_imovel != '':
        caminho_pasta = os.path.join(app.config['UPLOADED_PATH'], str(pk_imovel))
        if os.path.isdir(caminho_pasta):
            files = [f for f in os.listdir(caminho_pasta) if os.path.isfile(os.path.join(caminho_pasta, f))]
            quantidade = len(files)
            return jsonify({'quantidade': quantidade})
        else:
            return jsonify({'quantidade': 0})
    return jsonify({'Result': 'sem pk_imovel'})



@blueprint_imoveis.route('/imoveis/filtros')
def form_filtro():
    return render_template('form_filtro.html')


@blueprint_imoveis.route('/imoveis/filtro')
def buscar_imoveis():
    codigo_imovel = request.args.get('codigo_imovel', '')

    if codigo_imovel:
        imovel = busca_imovel(codigo_imovel)
        if imovel:
            return render_template('lista_imoveis_filtro.html', imoveis_pagina=[imovel], total_paginas=1, pagina=1)

    classificado = request.args.get('classificado', 'locacao')
    tipo_filtro = request.args.getlist('tipo_filtro')
    quartos = request.args.get('quartos', '')
    banheiros = request.args.get('banheiros', '')
    vagas = request.args.get('vagas', '')
    suites = request.args.get('suites', '')
    valor_min = request.args.get('valor_min', '')
    valor_max = request.args.get('valor_max', '')

    filtros = {
        'classificado': classificado,
        'tipo': tipo_filtro,
        'quartos': quartos,
        'banheiros': banheiros,
        'vagas': vagas,
        'suites': suites,
        'valor_min': valor_min,
        'valor_max': valor_max
    }

    filtros = {key: valor for key, valor in filtros.items() if valor}

    logging.debug(f"filtro nao vazios : {filtros} ")
    
    imoveis = busca_imoveis_filtro(**filtros)

    pagina = request.args.get('pagina', 1, type=int)
    quantidade_pagina = 5
    inicio = (pagina - 1) * quantidade_pagina
    final = inicio + quantidade_pagina
    total_paginas = (len(imoveis) + quantidade_pagina - 1) // quantidade_pagina
    imoveis_pagina = imoveis[inicio:final]


    return render_template('lista_imoveis_filtro.html', imoveis_pagina=imoveis_pagina, total_paginas=total_paginas, pagina=pagina)



@blueprint_imoveis.route('/imoveis/buscar')
def detalhe_imovel():
    codigo = request.args.get('codigo')
    imovel = busca_imovel(codigo)
    return render_template('detalhe_imovel.html' , imovel=imovel)\
    

@blueprint_imoveis.route('/imoveis/comodidades')
def detalhe_imovel_comodidades():
    pk_imovel = request.args.get('pk_imovel')
    comodidades = obter_comodidades_sim(pk_imovel)
    return render_template('comodidades_detalhe.html' , comodidades=comodidades)