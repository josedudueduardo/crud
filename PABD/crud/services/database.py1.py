import psycopg2

#Fazendo a conexão com o banco de dados
con = psycopg2.connect(
    host='localhost',
    database='gostory',
    user='postgres',
    password='pabd'
)

#Curso da conexão
cur = con.cursor()