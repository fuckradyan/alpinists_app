import mysql.connector as connector
from flask import g

class MySQL:
    def __init__(self, app):
        self.app = app
        self.app.teardown_request(self.teardown_request)

    @property  
    def connection(self):
        if 'db' not in g:
            g.db = self.connect()
        return g.db

    def connect(self):
        return connector.connect(**self.config)
    
    @property    
    def config(self):
        return {
            'user': 'std_1230',
            'password': '12345678',
            'host': '172.20.128.5',
            'database': 'std_1230'
 
        }
    
    def teardown_request(self, exception=None):
        db= g.pop('db', None)
        if db is not None:
            db.close()