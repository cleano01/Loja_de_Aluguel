import sqlite3
conn = sqlite3.connect('../base.bd')
cursor = conn.cursor()


def create_table():
    conn.execute('PRAGMA Foreign_keys = ON;')
    
    cursor.execute('CREATE TABLE IF NOT EXISTS Cliente (\
    cpf VARCHAR(11) UNIQUE NOT NULL PRIMARY KEY,\
    nome TEXT NOT NULL)' )

    
    cursor.execute('CREATE TABLE IF NOT EXISTS TipoItem (\
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
        tipo TEXT UNIQUE NOT NULL \
        )') 


    cursor.execute('CREATE TABLE IF NOT EXISTS Item (\
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
        item TEXT UNIQUE NOT NULL, \
        id_tipo INTEGER NOT NULL , \
        FOREIGN KEY(id_tipo) REFERENCES TipoItem(id) )') 


    cursor.execute('CREATE TABLE IF NOT EXISTS ReservaItem ( \
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
        data_reserva TEXT NOT NULL,\
        data_devolucao TEXT ,\
        entrega BOOLEAN DEFAULT False,\
        cancelamento BOOLEAN DEFAULT False,\
        cpf VARCHAR(11) NOT NULL,  \
        id_item  INTEGER NOT NULL ,\
        FOREIGN KEY(cpf)   REFERENCES Cliente(cpf),\
        FOREIGN KEY(id_item)  REFERENCES Item(id))' )        


    cursor.execute('CREATE TABLE IF NOT EXISTS AlugaItem ( \
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
        data_aluguel TEXT NOT NULL,\
        data_devolucao TEXT ,\
        entrega BOOLEAN DEFAULT False,\
        cancelamento BOOLEAN DEFAULT False,\
        cpf VARCHAR(11) NOT NULL,  \
        id_item  INTEGER NOT NULL ,\
        FOREIGN KEY(cpf)   REFERENCES Cliente(cpf),\
        FOREIGN KEY(id_item)  REFERENCES Item(id))' ) 
    
   

create_table()













