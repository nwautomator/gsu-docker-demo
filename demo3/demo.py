import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

def get_sql_connection():
    connection = mysql.connector.connect(
        host="db", port=3306, user="demo3",
        passwd="demo3", database="demo3",
        auth_plugin='mysql_native_password')
    return connection

def get_sql_data(sql_query):
    connection = get_sql_connection()
    cursor = connection.cursor()
    cursor.execute(sql_query)
    return list(cursor.fetchall())

def write_sql_data(sql_query):
    connection = get_sql_connection()
    cursor = connection.cursor()
    cursor.execute(sql_query)
    connection.commit()
    cursor.close()
    connection.close()

@app.route("/result", methods=['POST'])
def result():
    if request.method == 'POST':
        data = request.form
        fname = data['fname']
        lname = data['lname']
        message = data['message']
        sql_query = "INSERT INTO messages (first_name, last_name, message) " +\
                    "VALUES ('{}', '{}', '{}');".format(fname, lname, message)
        write_sql_data(sql_query)
        sql_query = r"SELECT first_name, last_name, message FROM messages ORDER BY last_name;"
        return render_template('users.html', users=get_sql_data(sql_query))

@app.route("/")
def hello():
    sql_query = r"SELECT first_name, last_name, message FROM messages ORDER BY last_name;"
    return render_template('users.html', users=get_sql_data(sql_query))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=True)
