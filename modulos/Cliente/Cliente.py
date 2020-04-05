import sqlite3
from flask_restful import Resource
from flask import Flask, request


class Cliente (Resource):
    
    def __init__(self):
        self.conn = sqlite3.connect('base.bd')
        self.cursor = self.conn.cursor()

    def post(self):
        try:
            cursor = self.conn.cursor()
            print('####')
            dados_requisicao = request.json
            dados_requisicao = tuple( list(dados_requisicao.values()))
                      
            lista = [dados_requisicao]
            
            self.conn.executemany('INSERT INTO Cliente \
            (cpf, nome)\
            VALUES (?, ?)', lista)

            self.conn.commit()
            cursor.close()
        
            return {'Status':'Dados inseridos'}
        
        except Exception as exception:
            
            return {'Error': f"Não foi possivél inserir um novo cliente: {exception}"}
            
       
    


        

      
        
