import mysql.connector
def conectar_banco():
    return mysql.connector.connect(
        host = "paparella.com.br",
        user = "paparell_aluno_1",
        password = "@Senai2025",
        database = "paparell_python"
    )

def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor(buffered=True)
    cursor.execute("""CREATE TABLE IF NOT EXISTS dht (id INT AUTO_INCREMENT PRIMARY KEY,
                  aluno VARCHAR(255) NOT NULL, dht INT NOT NULL, umidade INT NOT NULL, 
                  temperatura INT NOT NULL) """)
    conexao.commit()
    conexao.close()

def inserir_ou_atualizar_estado(aluno,led,estado):
    conexao = conectar_banco()
    cursor = conexao.cursor(buffered=True)
    cursor.execute(''' SELECT id FROM leds WHERE aluno = %s''',(aluno,))
    id = cursor.fetchone()
    if id:
        cursor.execute(''' UPDATE leds SET estado = %s WHERE id = %s''',(estado,id[0]))
        print(f"Estado do LED do Aluno: {aluno }, atualizado com sucesso")
    else:    
        cursor.execute(''' INSERT INTO leds (aluno,led,estado) VALUES (%s,%s,%s)''',(aluno,led,estado))
        print(f"Estado do LED do Aluno: {aluno }, atualizado com sucesso")
    conexao.commit()
    cursor.close()
    conexao.close()
    
def pegar_ultrassom():
    conexao = conectar_banco()
    cursor = conexao.cursor(buffered=True)
    cursor.execute("""SELECT distancia FROM ultrassom WHERE aluno=%s """,("Rafael Italiano",))
    return cursor.fetchone()

def teste():
    conexao = conectar_banco()
    cursor = conexao.cursor(buffered=True)
    cursor.execute ("""INSERT INTO dht (aluno,dht,umidade,temperatura) values ('giovani',2,40,20)""")
    cursor.execute('SELECT * FROM dht')
    variavel=cursor.fetchall()
    print(variavel)


if __name__ == "__main__":
    criar_tabela()
    teste()