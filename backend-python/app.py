from flask import Flask, jsonify
from flaskext.mysql import MySQL
# from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()
# For docker compose
# app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_HOST'] = 'backend-mysql'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mysecret'
app.config['MYSQL_DATABASE_DB'] = 'mydb'
mysql.init_app(app)

conn = mysql.connect()
cur =conn.cursor()
#cur = mysql.connect()

@app.route('/hello')
def hello():
    greeting = "Hello world!"
    return greeting

@app.route('/instructors', methods=["GET"])
def getInstructors():
    # cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM instructors''')
    rv = cur.fetchall()
    instructors = []
    content = {}
    for result in rv:
        content = {'id': result[0], 'firstName': result[1], 'lastName': result[2]}
        instructors.append(content)
        content = {}
    return jsonify(instructors)

@app.route('/students', methods=["GET"])
def getStudents():
    # cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM students''')
    rv = cur.fetchall()
    students = []
    content = {}
    for result in rv:
        content = {'id': result[0], 'firstName': result[1], 'lastName': result[2]}
        students.append(content)
        content = {}
    return jsonify(students)

@app.route('/instructor/<id>', methods=["GET"])
def getInstructor(id):
    id = int(id) - 1
    # cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM instructors''')
    rv = cur.fetchall()
    instructors = []
    content = {}
    for result in rv:
        content = {'id': result[0], 'firstName': result[1], 'lastName': result[2]}
        instructors.append(content)
        content = {}
    return jsonify(instructors[id])

@app.route('/student/<id>', methods=["GET"])
def getStudent(id):
    id = int(id) - 1
    # cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM students''')
    rv = cur.fetchall()
    students = []
    content = {}
    for result in rv:
        content = {'id': result[0], 'firstName': result[1], 'lastName': result[2]}
        students.append(content)
        content = {}
    return jsonify(students[id])

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)