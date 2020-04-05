import sqlite3
from flask_restful import Resource
from flask import Flask, request
import datetime
import time


class Aluga (Resource):
    
    def __init__(self):
        self.conn = sqlite3.connect('base.bd')
        self.cursor = self.conn.cursor()
        self.conn.execute('PRAGMA Foreign_keys = ON;')


    def post(self):
        try:
            
            cursor = self.conn.cursor()            
            dados_requisicao = request.json


            data_aluguel = str(datetime.datetime.fromtimestamp\
            (int(time.time())).strftime('%Y-%m-%d'))
            data_devolucao = ''
            entrega = True
            cancelamento = False
            cpf = dados_requisicao.get('cpf')
            id_item = dados_requisicao.get('id_item')                 
            lista = [(data_aluguel, data_devolucao, entrega, 
            cancelamento, cpf,  id_item)]


            self.conn.executemany('INSERT INTO AlugaItem \
            (data_aluguel, data_devolucao, entrega, \
            cancelamento, cpf, id_item )\
            VALUES (?, ?, ?, ?, ?, ?)',lista)


            self.conn.commit()
            cursor.close()
        
            return {'Status':'Dados inseridos'}
        
        except Exception as exception:            
            return {'Error': f"Não foi possivél alugar um item: {exception}"}
            
       
    


        

      
        
