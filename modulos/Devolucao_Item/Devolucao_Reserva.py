import sqlite3
from flask_restful import Resource
from flask import Flask, request
import datetime
import time

class Devolucao_Reserva(Resource):
    
    def __init__(self):
        self.conn = sqlite3.connect('base.bd')
        self.cursor = self.conn.cursor()
        self.conn.execute('PRAGMA Foreign_keys = ON;')

    
    def put(self):
        
        cursor = self.conn.cursor()            
        dados_requisicao = request.json


        cpf = dados_requisicao.get('cpf')
        id_item = dados_requisicao.get('id_item')
        id_reserva = dados_requisicao.get('id_reserva')
        data_atual = str(datetime.datetime.fromtimestamp\
            (int(time.time())).strftime('%Y-%m-%d'))


        cursor.execute(f'UPDATE  ReservaItem  SET data_devolucao = "{data_atual}"\
             WHERE exists (select * from Cliente,\
             Item where ReservaItem.cpf = {cpf} and\
			 Cliente.cpf = {cpf} and\
			 ReservaItem.id = {id_reserva} and\
			 Item.id_tipo =  {id_item} and\
             ReservaItem.cancelamento != {1} and\
             "{data_atual}" >= ReservaItem.data_reserva)and\
             ReservaItem.entrega = {1}')


        self.conn.commit()
        cursor.close()
        
        if(cursor.rowcount > 0):
            return {'Status':f'Dados atualizados {cursor.rowcount}'}
 
        return {'Status':f'Nenhum dados foi atualizados {cursor.rowcount}'}

    
