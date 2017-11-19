#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sqlite3
import tkMessageBox
#from ler import *

class Banco_Sqlite():
    def __init__(self):
        #conectando...
        self.conn = sqlite3.connect('database.db')
        #definindo o cursor
        self.cursor = self.conn.cursor()

        #self.execs = Execs()
        #self.destr = Actions() 

    def criar_Novo_Usuario(self, nome, senha, email, funcao):
        
        self.nome = nome
        self.email = email
        self.senha = senha
        self.funcao = funcao

        self.criar_Tabela = self.cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL,
            email TEXT NOT NULL,
            funcao TEXT NOT NULL
        );
        """)

        self.verificar = self.cursor.execute("SELECT nome FROM usuarios WHERE nome = '%s'" % self.nome)
        self.verify    = self.cursor.fetchone()

        if self.verify:
            tkMessageBox.showerror("Aviso", "Usuário existente")
            return False
        else:
            #self.criar_Tabela = self.cursor.execute("""
            #INSERT INTO usuarios (nome, senha, email, funcao)
            #VALUES (?, ?, ?, ?)
            #""", (self.nome, self.senha, self.email, self.funcao))
            tkMessageBox.showinfo("Aviso", "Usuário cadastrado com sucesso!")
            return True

        #self.conn.commit()
    
    def criar_Novo_Cliente(self, nome, sobrenome, cidade, estado, bairro, rua):
        
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

    def add_Novo_Produto(self, prod_nome, prod_numero, prod_categoria, prod_barras):
        
        self.prod_nome = prod_nome
        self.numero = prod_numero
        self.categoria = prod_categoria
        self.cod_barras = prod_barras

        self.criar_Tabela = self.cursor.execute("""CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            numero INT NUMERIC,
            categoria TEXT NOT NULL,
            cod_barras INT NUMERIC
        );
        """)

        self.criar_Produto = self.cursor.execute("""
        INSERT INTO produtos (nome, numero, categoria, cod_barras)
        VALUES (?, ?, ?, ?)
        """, (self.prod_nome, self.numero, self.categoria, self.cod_barras))

        self.conn.commit()

