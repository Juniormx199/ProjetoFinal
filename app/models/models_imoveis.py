import sqlite3

db = sqlite3.connect("app/db/contalcred.db" , check_same_thread=False)

class Imovel:
    def __init__(self, pk, codigo, destaque, classificado, inativo, descricao, valor_locacao, valor_venda, valor_condominio, informacoes, tipo, cep, rua, numero, bairro, cidade, uf, area, banheiros, vagas, quartos, suites):
        self.pk = pk
        self.codigo = codigo
        self.destaque = destaque
        self.classificado = classificado
        self.inativo = inativo
        self.descricao = descricao
        self.valor_locacao = valor_locacao
        self.valor_venda = valor_venda
        self.valor_condominio = valor_condominio
        self.informacoes = informacoes
        self.tipo = tipo
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.area = area
        self.banheiros = banheiros
        self.vagas = vagas
        self.quartos = quartos
        self.suites = suites

def get_all_imoveis():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM imoveis')
    resultado = cursor.fetchall()
    lista_imoveis = [
        Imovel(
            pk, codigo, destaque, classificado, inativo, descricao, valor_locacao, valor_venda,
            valor_condominio, informacoes, tipo, cep, rua, numero, bairro, cidade, uf, area, 
            banheiros, vagas, quartos, suites
        )
        for (
            pk, codigo, destaque, classificado, inativo, descricao, valor_locacao, valor_venda, 
            valor_condominio, informacoes, tipo, cep, rua, numero, bairro, cidade, uf, area, 
            banheiros, vagas, quartos, suites
        ) in resultado
    ]

    return lista_imoveis


def cadastrar_imovel(imovel,comodidades):
    cursor = db.cursor()
    insert_sql = """
    INSERT INTO imoveis (
        codigo, destaque, classificado, inativo, descricao, valor_locacao, 
        valor_venda, valor_condominio, informacoes, tipo, cep, rua, numero, 
        bairro, cidade, uf, area, banheiros, vagas, quartos, suites
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """

    cursor.execute(insert_sql, (
        imovel.codigo, imovel.destaque, imovel.classificado, imovel.inativo, 
        imovel.descricao, imovel.valor_locacao, imovel.valor_venda, 
        imovel.valor_condominio, imovel.informacoes, imovel.tipo, imovel.cep, 
        imovel.rua, imovel.numero, imovel.bairro, imovel.cidade, imovel.uf, 
        imovel.area, imovel.banheiros, imovel.vagas, imovel.quartos, 
        imovel.suites
    ))

    imovel_id = cursor.lastrowid
    
    cria_comodidades(imovel_id , comodidades)

    db.commit()
    cursor.close()
    return imovel_id


def cria_comodidades(imovel_id , comodidades):
    cursor = db.cursor()

    insert_comodidades_sql = """
    INSERT INTO comodidades (
        fk_imovel, academia, estacionamento, elevador, areaLazer, salaoFestas, 
        churrasqueira, portaria24h, quadraEsportes, playground, jardim, salaJogos, 
        espacoGourmet, sauna, brinquedoteca, espacoCoworking, petPlace, bicicletario, 
        lavanderia, geradorEnergia, sistemaSeguranca, wifiAreasComuns, aquecimentoCentral
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?);
    """
    
    cursor.execute(insert_comodidades_sql, (
        imovel_id, comodidades["academia"], comodidades["estacionamento"], comodidades["elevador"], 
        comodidades["areaLazer"], comodidades["salaoFestas"], comodidades["churrasqueira"], 
        comodidades["portaria24h"], comodidades["quadraEsportes"], comodidades["playground"], 
        comodidades["jardim"], comodidades["salaJogos"], comodidades["espacoGourmet"], 
        comodidades["sauna"], comodidades["brinquedoteca"], comodidades["espacoCoworking"], 
        comodidades["petPlace"], comodidades["bicicletario"], comodidades["lavanderia"], 
        comodidades["geradorEnergia"], comodidades["sistemaSeguranca"], 
        comodidades["wifiAreasComuns"], comodidades["aquecimentoCentral"]
    ))

    db.commit()
    cursor.close()


def update_imovel(imovel , comodidades):
    cursor = db.cursor()
    update_sql = """
    UPDATE imoveis
    SET descricao = ?, valor_locacao = ?, valor_venda = ?, valor_condominio = ?, informacoes = ?, 
        tipo = ?, cep = ?, rua = ?, numero = ?, bairro = ?, cidade = ?, uf = ?, destaque = ?, 
        classificado = ?, inativo = ?, area = ?, banheiros = ?, vagas = ?, quartos = ?, suites = ?
    WHERE pk = ?;
    """

    cursor.execute(update_sql, (
        imovel.descricao, imovel.valor_locacao, imovel.valor_venda, imovel.valor_condominio, imovel.informacoes,
        imovel.tipo, imovel.cep, imovel.rua, imovel.numero, imovel.bairro, imovel.cidade, imovel.uf, 
        imovel.destaque, imovel.classificado, imovel.inativo, imovel.area, imovel.banheiros, imovel.vagas, 
        imovel.quartos, imovel.suites, imovel.pk
    ))

    update_comodidades(imovel.pk , comodidades)

    db.commit()
    cursor.close()

def update_comodidades(pk , comodidades):
    cursor = db.cursor()

    update_comodidades_sql = """
    UPDATE comodidades SET 
        academia = ?, estacionamento = ?, elevador = ?, areaLazer = ?, salaoFestas = ?, 
        churrasqueira = ?, portaria24h = ?, quadraEsportes = ?, playground = ?, jardim = ?, 
        salaJogos = ?, espacoGourmet = ?, sauna = ?, brinquedoteca = ?, espacoCoworking = ?, 
        petPlace = ?, bicicletario = ?, lavanderia = ?, geradorEnergia = ?, sistemaSeguranca = ?, 
        wifiAreasComuns = ?, aquecimentoCentral = ?
    WHERE fk_imovel = ?;
    """

    cursor.execute(update_comodidades_sql, (
        comodidades["academia"], comodidades["estacionamento"], comodidades["elevador"], 
        comodidades["areaLazer"], comodidades["salaoFestas"], comodidades["churrasqueira"], 
        comodidades["portaria24h"], comodidades["quadraEsportes"], comodidades["playground"], 
        comodidades["jardim"], comodidades["salaJogos"], comodidades["espacoGourmet"], 
        comodidades["sauna"], comodidades["brinquedoteca"], comodidades["espacoCoworking"], 
        comodidades["petPlace"], comodidades["bicicletario"], comodidades["lavanderia"], 
        comodidades["geradorEnergia"], comodidades["sistemaSeguranca"], 
        comodidades["wifiAreasComuns"], comodidades["aquecimentoCentral"], pk
    ))
        
    db.commit()
    cursor.close()

def deletar_imovel(pk_imovel):
    cursor = db.cursor()
    delete_sql = f"""
    delete from imoveis where pk = {str(pk_imovel)}
    """
    cursor.execute(delete_sql)
    db.commit()
    cursor.close()
    deletar_comodidade(pk_imovel)

def deletar_comodidade(pk_imovel):
    cursor = db.cursor()
    delete_sql = f"""
    delete from comodidades where fk_imovel = {str(pk_imovel)}
    """
    cursor.execute(delete_sql)
    db.commit()
    cursor.close()    

def ultimo_codigo():
    cursor = db.cursor()
    cursor.execute("SELECT codigo FROM imoveis ORDER BY codigo DESC LIMIT 1")
    resultado = cursor.fetchall()

    if (len(resultado) > 0):
        return(resultado[0][0] + 1)
    else:
        return 1


def busca_imovel(codigo_imovel):
    cursor = db.cursor()
    select_sql = f"""
    SELECT * FROM imoveis where codigo = {codigo_imovel}
    """
    cursor.execute(select_sql)
    resultado = cursor.fetchone()
    
    if resultado:
        (pk, codigo, destaque, classificado, inativo, descricao, valor_locacao, valor_venda,
         valor_condominio, informacoes, tipo, cep, rua, numero, bairro, cidade, uf, area,
         banheiros, vagas, quartos, suites) = resultado
        
        try:
            imovel = Imovel(
                pk, codigo, destaque, classificado, inativo, descricao, valor_locacao, valor_venda,
                valor_condominio, informacoes, tipo, cep, rua, numero, bairro, cidade, uf, area,
                banheiros, vagas, quartos, suites
            )
            return imovel
        except Exception as e:
            print(f"Erro ao criar o objeto Imovel: {e}")
            return None
    else:
        return None  # Retor
    


def busca_comodidades(pk_imovel):
    cursor = db.cursor()
    select_sql = f"""
    SELECT * FROM comodidades where fk_imovel = {pk_imovel}
    """
    cursor.execute(select_sql)
    resultado = cursor.fetchone()
    colunas = [desc[0] for desc in cursor.description]

    resultado_dict = dict(zip(colunas, resultado))

    return resultado_dict


def busca_imoveis_filtro(**filtros):
    cursor = db.cursor()

    query = 'SELECT * FROM imoveis'
    condicoes = []
    parametros = []

    if 'classificado' in filtros:
        condicoes.append('classificado = ?')
        parametros.append(filtros['classificado'])  


    if 'tipo' in filtros:
        placeholders = ', '.join(['?'] * len(filtros['tipo']))
        condicoes.append(f'tipo IN ({placeholders})')
        parametros.extend(filtros['tipo'])

    if 'quartos' in filtros:
        condicoes.append('quartos = ?')
        parametros.append(filtros['quartos'])

    if 'banheiros' in filtros:
        condicoes.append('banheiros = ?')
        parametros.append(filtros['banheiros'])

    if 'vagas' in filtros:
        condicoes.append('vagas = ?')
        parametros.append(filtros['vagas'])

    if 'suites' in filtros:
        condicoes.append('suites = ?')
        parametros.append(filtros['suites'])

    if 'classificado' in filtros:
        if filtros['classificado'] == 'locacao':
            valor_campo = 'valor_locacao'
        else:
            valor_campo = 'valor_venda'

    if 'valor_min' in filtros:
        condicoes.append(f'{valor_campo} >= ?')
        parametros.append(filtros['valor_min'])

    if 'valor_max' in filtros:
        condicoes.append(f'{valor_campo} <= ?')
        parametros.append(filtros['valor_max'])


    if condicoes:
        query += ' WHERE ' + ' AND '.join(condicoes)

    cursor.execute(query, tuple(parametros))

    resultado = cursor.fetchall()

    lista_imoveis = [
        Imovel(
            pk, codigo, destaque, classificado, inativo, descricao, valor_locacao, valor_venda,
            valor_condominio, informacoes, tipo, cep, rua, numero, bairro, cidade, uf, area, 
            banheiros, vagas, quartos, suites
        )
        for (
            pk, codigo, destaque, classificado, inativo, descricao, valor_locacao, valor_venda, 
            valor_condominio, informacoes, tipo, cep, rua, numero, bairro, cidade, uf, area, 
            banheiros, vagas, quartos, suites
        ) in resultado
    ]

    return lista_imoveis



def obter_comodidades_sim(pk_imovel):
    cursor = db.cursor()

    query = """
    SELECT pk, fk_imovel, academia, estacionamento, elevador, areaLazer,
           salaoFestas, churrasqueira, portaria24h, quadraEsportes, playground,
           jardim, salaJogos, espacoGourmet, sauna, brinquedoteca, espacoCoworking,
           petPlace, bicicletario, lavanderia, geradorEnergia, sistemaSeguranca,
           wifiAreasComuns, aquecimentoCentral
    FROM comodidades
    WHERE fk_imovel = ?
    """
    cursor.execute(query, (pk_imovel,))
    resultados = cursor.fetchone()
    
    if resultados:

        colunas = [desc[0] for desc in cursor.description]

        comodidades_dict = dict(zip(colunas, resultados))
        
        comodidades_sim = [k for k, v in comodidades_dict.items() if v == 'Sim']
        
        return comodidades_sim
    else:
        return []

