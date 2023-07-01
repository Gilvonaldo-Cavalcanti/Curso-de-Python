import sqlite3

banco = sqlite3.connect('primeiro-bd.bd')

cursor = banco.cursor()

cursor.execute('''
    CREATE TABLE Clientes (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT,
        Email TEXT
    )
''')

cursor.execute('''
    CREATE TABLE Pedidos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        ClienteID INTEGER,
        Descricao TEXT,
        FOREIGN KEY (ClienteID) REFERENCES Clientes(ID)
    )
''')

banco.commit()

banco.close()