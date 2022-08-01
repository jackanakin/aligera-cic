import app.util.DBConnector as DBConnector

def run():
    print("testdb started")
    
    res = DBConnector.create_tables()
    print('Result from main')
    #print(res)

    print("testdb finished")