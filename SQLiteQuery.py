import sqlite3 as lite
import pandas as pd

class sqlite_query():
    '''
        A sqlite3 connector and query executor with some additional nice features for showing and describing tables.

        connect:    connect to database
        query:      execute query
        showtables: show all tables in database
        describe:   prints an HTML-formatted pandas DataFrame with column headers and other info
        inspect:    prints an HTML-formatted pandas DataFrame with n sample rows (default 1)
        close:      close database connection

    '''
    def __init__(self):
        pass
    
    def connect(self,db):
        self.conn_db = lite.connect(db)
        
    def query(self, query):
        self.cursor = self.conn_db.cursor()  
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results
    
    def showtables(self):
        return self.query('SELECT name FROM sqlite_master WHERE type="table";')
    
    def describe(self,table):
        rawinfo = self.query('PRAGMA table_info(%s);' % table)
        rawinfo = [x[1:] for x in rawinfo]
        df = pd.DataFrame(rawinfo,columns=['column','type','null','default','primary_key'])
        return df

    def inspect(self,table,n=1):
        describeme = self.describe(table)
        sample_entry = self.query('select * from %s limit %d;' % (table,n))[0]
        header_names = describeme['column']
        df = pd.DataFrame([sample_entry],columns=header_names)
        return df

    def close(self):
        self.conn_db.close()