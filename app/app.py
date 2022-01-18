
from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify
from mysql_db import MySQL
import mysql.connector as connector
app = Flask(__name__)
app.config.from_pyfile('config.py')
mysql = MySQL(app)

@app.route('/')
def index():
    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute(""" SELECT
                   TABLE_NAME
           COLUMN_KEY,
           COLUMN_NAME,
           DATA_TYPE,
           IS_NULLABLE
   FROM INFORMATION_SCHEMA.COLUMNS
   WHERE table_name='Climbing' """)
    climbings = cursor.fetchall()
    cursor.close()
    
    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute(""" SELECT
                   TABLE_NAME
           COLUMN_KEY,
           COLUMN_NAME,
           DATA_TYPE,
           IS_NULLABLE
   FROM INFORMATION_SCHEMA.COLUMNS
   WHERE table_name='Group' """)
    groups = cursor.fetchall()
    cursor.close()
    
    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute(""" SELECT
                   TABLE_NAME
           COLUMN_KEY,
           COLUMN_NAME,
           DATA_TYPE,
           IS_NULLABLE
   FROM INFORMATION_SCHEMA.COLUMNS
   WHERE table_name='Human' """)
    human = cursor.fetchall()
    cursor.close()
    
    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute(""" SELECT
                   TABLE_NAME
           COLUMN_KEY,
           COLUMN_NAME,
           DATA_TYPE,
           IS_NULLABLE
   FROM INFORMATION_SCHEMA.COLUMNS
   WHERE table_name='Address' """)
    addresses = cursor.fetchall()
    cursor.close()
    
    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute(""" SELECT
                   TABLE_NAME
           COLUMN_KEY,
           COLUMN_NAME,
           DATA_TYPE,
           IS_NULLABLE
   FROM INFORMATION_SCHEMA.COLUMNS
   WHERE table_name='Human in Group' """)
    hig = cursor.fetchall()
    cursor.close()
    
    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute(""" SELECT
                   TABLE_NAME
           COLUMN_KEY,
           COLUMN_NAME,
           DATA_TYPE,
           IS_NULLABLE
   FROM INFORMATION_SCHEMA.COLUMNS
   WHERE table_name='Mountain' """)
    mountains = cursor.fetchall()
    cursor.close()
    
    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute(""" SELECT
                   TABLE_NAME
           COLUMN_KEY,
           COLUMN_NAME,
           DATA_TYPE,
           IS_NULLABLE
   FROM INFORMATION_SCHEMA.COLUMNS
   WHERE table_name='Country' """)
    countries = cursor.fetchall()
    cursor.close()
    
    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute(""" SELECT
            TABLE_NAME,
           COLUMN_KEY,
           COLUMN_NAME,
           DATA_TYPE,
           IS_NULLABLE
   FROM INFORMATION_SCHEMA.COLUMNS
   WHERE table_name='Region' """)
    regions = cursor.fetchall()
    cursor.close()
    
    return render_template('index.html',climbings=climbings,regions=regions,countries=countries, mountains=mountains, hig=hig, addresses=addresses, human=human, groups=groups)


@app.route('/table/<tablename>')
def eachtable(tablename):

    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT * FROM '+ '`' + tablename + '`;')   
    fetched = cursor.fetchall()
    cursor.close()
    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT TABLE_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name=%s',(tablename,))
    tablename = cursor.fetchall()
    cursor.close()

    return render_template('eachtable.html',fetched=fetched,tablename=tablename[0][0])

@app.route('/task1')
def task1():

    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT `Mountain`.`name` as mountain, `Group`.`name` as group_name, `Climbing`.`start`, `Climbing`.`end` FROM `Climbing` JOIN `Mountain` ON `Mountain`.id=`Climbing`.`mountain_id` JOIN `Group` ON `Group`.`id` = `Climbing`.`group_id`;')   
    fetched = cursor.fetchall()
    cursor.close()

    return jsonify(fetched)
# def load_roles():
#     cursor =  mysql.connection.cursor(named_tuple=True)
#     cursor.execute('SELECT id, name FROM roles;')
#     roles = cursor.fetchall()
#     cursor.close()
#     return roles