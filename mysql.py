import mysql.connector
from mysql.connector import errorcode
cfg = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'box'
}

db = mysql.connector.connect(**cfg)
cursor = db.cursor()

DB_NAME = 'box'
TABLES = {}
TABLES['chocolates'] = (
    "CREATE TABLE `chocolates` ("
    " `id` int(11) NOT NULL AUTO_INCREMENT,"
    " `text` varchar(100) NOT NULL,"
    " `user` varchar(100) NOT NULL,"
    " `purchased` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    " PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)

def create_db():
    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Database {} created!".format(DB_NAME))

def create_tables():
    cursor.execute("USE {}".format(DB_NAME))

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table ({}) ".format(table_name), end="")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Table already available")
            else:
                print(err.msg)

create_db()
create_tables()

def get_chocolates():
    query = ("SELECT * FROM chocolates ORDER BY purchased DESC")
    cursor.execute(query)
    result = cursor.fetchAll()

    for row in result:
        print(row[1])

def get_chocolate(id):
    query = ("SELECT * from chocolates where id = %s")
    cursor.execute(query, (id,))
    result = cursor.fetchOne()

    for row in result:
        print(row)

def update_chocolate(id, text):
    query = ("UPDATE chocolates SET text = %s WHERE id = %s")
    cursor.execute(query, (text, id))
    db.commit()

def delete_chocolate(id):
    query = ("DELETE FROM chocolates WHERE id = %s")
    cursor.execute(query, (id,))
    db.commit()
    

