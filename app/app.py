
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

@app.route('/task2selector')
def task2selector():

    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT `Region`.`id`, `Region`.`name` as r_name, `Country`.`name` as c_name FROM `Region` JOIN `Country` ON `Country`.`id`=`Region`.`country_id`;')   
    fetched = cursor.fetchall()
    cursor.close()
    return jsonify(fetched)

@app.route('/task2')
def task2():
    height = request.args.get('height',type=int)
    name = request.args.get('name')
    region_id = request.args.get('region_id',type=int)
    try:
        cursor =  mysql.connection.cursor(named_tuple=True)
        cursor.execute('INSERT INTO `Mountain`(`name`, `height`, `region_id`) VALUES (%s, %s, %s)', (name, height, region_id,))
        mysql.connection.commit()
        cursor.close()
        return jsonify('ok')
    except:
        return jsonify('not ok')

@app.route('/searchmtn')
def searchmtn():
    mtn_id = request.args.get('id',type=int)
    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT * FROM `Mountain` WHERE id=%s;',(mtn_id,))   
    fetched = cursor.fetchone()
    cursor.close()
    return jsonify(fetched)
@app.route('/task3')
def task3():
    height = request.args.get('height',type=int)
    name = request.args.get('name')
    region_id = request.args.get('region_id',type=int)
    id=request.args.get('id',type=int)
    cursor = mysql.connection.cursor(named_tuple=True)
    cursor.execute("SELECT * FROM `Climbing` WHERE mountain_id=%s;",(id,))
    fetched = cursor.fetchall()
    cursor.close()
    if len(fetched)==0:
        cursor = mysql.connection.cursor(named_tuple=True)
        cursor.execute("UPDATE `Mountain` SET `name`=%s, `height`=%s, `region_id`=%s WHERE id=%s;",(name,height,region_id,id,))
        mysql.connection.commit()
        cursor.close()
        return jsonify("ok")
    return jsonify('not ok')

@app.route('/task4')
def task4():
    start = request.args.get('start')
    end = request.args.get('end')
    print(start)
    print(end)
    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT DISTINCT `Human`.`first_name`, `Human`.`last_name` FROM `Climbing` JOIN `Human in Group` ON `Climbing`.`group_id` = `Human in Group`.`group_id` JOIN `Human` ON `Human`.`id`= `Human in Group`.`human_id` WHERE `start`>%s AND `end`<%s;',(start,end,))  
    fetched = cursor.fetchall()
    cursor.close()
    return jsonify(fetched)
# def load_roles():
#     cursor =  mysql.connection.cursor(named_tuple=True)
#     cursor.execute('SELECT id, name FROM roles;')
#     roles = cursor.fetchall()
#     cursor.close()
#     return roles
@app.route('/getgroups')
def getgroups():
    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT * FROM `Group`',)  
    fetched = cursor.fetchall()
    cursor.close()
    return jsonify(fetched)

@app.route('/getaddresses')
def getaddresses():
    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT * FROM `Address`',)  
    fetched = cursor.fetchall()
    cursor.close()
    return jsonify(fetched)
@app.route('/addhumaningroup')
def addhumaningroup():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    address_id = request.args.get('address_id',type=int)
    group_id = request.args.get('group_id',type=int)
    print(first_name,last_name, address_id, group_id)
    try:
        cursor =  mysql.connection.cursor(named_tuple=True)
        cursor.execute('INSERT INTO `Human`(`first_name`, `last_name`, `address_id`) VALUES (%s, %s, %s)', (first_name, last_name, address_id,))
        mysql.connection.commit()
        cursor.close()
        cursor =  mysql.connection.cursor(named_tuple=True)
        cursor.execute('SELECT id FROM `Human` WHERE id=LAST_INSERT_ID();',)  
        fetched = cursor.fetchone()
        cursor.close()
        print(fetched)
        cursor =  mysql.connection.cursor(named_tuple=True)
        cursor.execute('INSERT INTO `Human in Group`(`group_id`, `human_id`) VALUES (%s, %s)', (group_id, fetched[0],))
        mysql.connection.commit()
        cursor.close()
        return jsonify('ok')
    except:
        return jsonify('not ok')

@app.route('/task7')
def task7():
    start = request.args.get('start')
    end = request.args.get('end')
    cursor =  mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT `Group`.`name` as g_name, `Mountain`.`name` as m_name, `start`, `end` FROM `Climbing` JOIN `Mountain` ON `Mountain`.`id`=`mountain_id` JOIN `Group` ON `Group`.`id`=`group_id` WHERE `start`>%s AND `end`<%s;',(start,end,))  
    fetched = cursor.fetchall()
    cursor.close()
    return jsonify(fetched)