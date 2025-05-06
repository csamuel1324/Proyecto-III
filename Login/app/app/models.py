import pymysql

def getconn():
    return pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        db="data base"
        )

class leer:
    def __init__(self,conn,comand):
        self.data=[]
        try:
            with conn.cursor() as cursor:
                cursor.execute(comand)
                self.data = cursor.fetchall()
            conn.close()
        except Exception as e:
            print(e)
            self.data = None

class commit:
    def __init__(self,conn,comand):
        self.data=[]
        try:
            with conn.cursor() as cursor:
                cursor.execute(comand)
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)

# tabla = leer(getconn(),"comando para executar mysql")

# print(tabla.data) # extrae la informacion de la db para su uso