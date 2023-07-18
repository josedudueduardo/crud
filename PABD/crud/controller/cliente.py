#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir(id, nome,desc, preco, data):
    db.cur.execute("""
                   INSERT into public.acessorios (id,nome,descricao,preco,data)
                   VALUES ('%s','%s','%s','%s','%s')
                   """ % (id,nome, desc, preco,data))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT * FROM acessorios
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows


def Excluir(id):
    db.cur.execute(
        """ DELETE FROM acessorios WHERE id = '%s' """ % (id))
    db.con.commit()