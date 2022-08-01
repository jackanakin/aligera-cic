import sqlite3
import traceback

def create_tables():
    try:
        con = sqlite3.connect('example.db')
        cur = con.cursor()
        
        cur.execute('''CREATE TABLE IF NOT EXISTS stocks
                (date text, trans text, symbol text, qty real, price real)''')

        con.commit()
    except Exception:
        print(traceback.format_exc())
        exit()
    finally:
        con.close()
