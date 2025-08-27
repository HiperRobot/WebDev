import sqlite3


def criaTabela():
    try:
        conn = sqlite3.connect(banco)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE contatos (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            salario REAL
            )
            """)
        print("Tabela criada")
    except sqlite3.Error as e:
        print("Erro ao criar tabela: ", e)
        return

def cadastrar():
    print("Cadastrar")
    nome = input("Entre com o nome (str): ")
    idade = int(input("Entre com a idade (int): "))
    salario = float(input("Entre com o salário (float): "))

    try:
        conn = sqlite3.connect(banco)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contatos (nome, idade, salario) VALUES (?,?,?)",
        (nome, idade, salario))
        conn.commit()
        conn.close()
        print("Dados inseridos com sucesso")
    except sqlite3.Error as e:
        print("Erro ao inserir dados")
    return

def editar():
    print("Editar")
    idReg = int(input("Entre com o id do registro a ser editado: "))
    nome = input("Entre com o nome (str): ")
    idade = int(input("Entre com a idade (int): "))
    salario = float(input("Entre com o salário (float): "))

    try:
        conn = sqlite3.connect(banco)
        cursor = conn.cursor()
        cursor.execute("UPDATE contatos SET nome=?, idade=?, salario=? WHERE id=?",
        (nome, idade, salario, idReg))
        cursor.close()
        print("Registro editado")
    except sqlite3.Error as e:
        print("Erro ao editar registro")
    return

def apagar():
    print("Apagar")
    idReg = int(input("Entre com o id do registro a ser apagado: "))

    try:
        conn = sqlite3.connect(banco)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contatos WHERE id=?", (idReg))
        conn.close()
        print("Registro %d apagado" & idReg)
    except sqlite3.Error as e:
        print("Erro ao apagar registro")
    return

def listar():
    print("Listar")

    try:
        conn = sqlite3.connect(banco)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contatos")
        for linha in cursor.fetchall():
            print(linha)
        conn.close()
    except sqlite3.Error as e:
        print("Erro ao acessar registro")
    return

def sair():
    print("Terminado")
    sys.exit()
    return

def main():
    ''' DocString: Tentar fazer para toda função do trabalho'''
    if input("Criar tabela (y/N)? ").upper() == 'Y':
        criaTabela()
    else:
        print("Não foi necessário criar a tabela")
    switcher = {
        'A': cadastrar,
        'B': editar,
        'C': apagar,
        'D': listar,
        'Z': sair,
    }
    while True:
        print("(A) Cadastrar contato\n(B) Editar contato\n(C) Apagar contato\n\
            (D) Listar contato\n(Z) Terminar")
        opcao = input("Entre com a opção: ").upper()
        switcher.get(opcao, lambda: print("Opção inválida"))()
    return