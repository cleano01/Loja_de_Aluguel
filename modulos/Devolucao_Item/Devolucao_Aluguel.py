import sqlite3
from flask_restful import Resource
from flask import Flask, request
import datetime
import time

class Devolucao_Aluguel(Resource):
    
    def __init__(self):
        self.conn = sqlite3.connect('base.bd')
        self.cursor = self.conn.cursor()
        self.conn.execute('PRAGMA Foreign_keys = ON;')

    
    def put(self):
        
        cursor = self.conn.cursor()            
        dados_requisicao = request.json


        cpf = dados_requisicao.get('cpf')
        id_item = dados_requisicao.get('id_item')
        id_aluguel = dados_requisicao.get('id_aluguel')
        data_atual = str(datetime.datetime.fromtimestamp\
            (int(time.time())).strftime('%Y-%m-%d'))


        cursor.execute(f'UPDATE  AlugaItem  SET data_devolucao = "{data_atual}"\
             WHERE exists (select * from Cliente,\
             Item where AlugaItem.cpf = {cpf} and\
			 Cliente.cpf = {cpf} and\
			 AlugaItem.id = {id_aluguel} and\
			 Item.id_tipo =  {id_item} )')


        self.conn.commit()
        cursor.close()
        
        if(cursor.rowcount > 0):
            return {'Status':f'Dados atualizados {cursor.rowcount}'}
 
        return {'Status':f'Nenhum dados foi atualizados {cursor.rowcount}'}

    
