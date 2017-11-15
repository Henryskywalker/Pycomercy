import sqlite3

class Banco_Sqlite():
    def __init__(self):
        #conectando...
        self.conn = sqlite3.connect('database.db')
        #definindo o cursor
        self.cursor = self.conn.cursor()

        print(self.conn)
    
    def criar_Tabela(self, nome, sobrenome, cidade, estado, bairro, rua):
        
        self.nome = nome
        self.sobrenome = sobrenome 
        self.cidade = cidade 
        self.estado = estado 
        self.bairro = bairro 
        self.rua = rua
 
        self.criar_Tabela = self.cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            sobrenome TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL,
            bairro TEXT NOT NULL,
            rua TEXT NOT NULL
        );
        """)

        self.criar_Cliente = self.cursor.execute("""
        INSERT INTO clientes (nome, sobrenome, cidade, estado, bairro, rua)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (self.nome, self.sobrenome, self.cidade, self.estado, self.bairro, self.rua))

        self.conn.commit()
