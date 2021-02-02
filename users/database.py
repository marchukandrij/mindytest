import mysql.connector
from datetime import date

# ----------- common -----------

config = {
  'user': 'mindy',
  'password': 'mindy',
  'host': 'localhost',
  'database': 'mindy',
  'raise_on_warnings': True
}

def check_connection():
    try:
        cnx = mysql.connector.connect(**config)
        cnx.close()
        return True
    except:
        return False

def execute_sql(sql, variables = ()):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute(sql, variables)
    cursor.close()
    cnx.commit()
    cnx.close()

def execute_select_sql(sql, variables = ()):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute(sql, variables)
    column_names = cursor.column_names
    column_count = len(column_names)
    result = []
    for line in cursor:
        item = {}
        for column_index in range(column_count):
            item[column_names[column_index]] = line[column_index]
        result.append(item)
    cursor.close()
    cnx.close()
    return result

# ----------- users -----------

def users_create_table():
    try:
        execute_sql("""
            CREATE TABLE IF NOT EXISTS `users` (
                `id` INT NOT NULL AUTO_INCREMENT,
                `login` VARCHAR(50) NULL,
                `name` VARCHAR(50) NULL,
                `surname` VARCHAR(50) NULL,
                `date_of_birth` DATE NULL,
                PRIMARY KEY (`id`)
            );
        """)
    except:
        print("Table 'users' already exists")

def users_read_all():
    return execute_select_sql("""
        SELECT * FROM `users`;
    """)

def users_create(login, name, surname, date_of_birth):
    execute_sql("""
        INSERT INTO `users`
        (login, name, surname, date_of_birth)
        VALUES (%s, %s, %s, %s);
    """, (login, name, surname, date_of_birth))

def users_update(id, login, name, surname, date_of_birth):
    execute_sql("""
        UPDATE `users`
        SET login = %s, name = %s, surname = %s, date_of_birth = %s
        WHERE id = %s;
    """, (login, name, surname, date_of_birth, id))

def users_delete(id):
    execute_sql("""
        DELETE FROM `users` WHERE `id` = %s;
    """, (id,))

