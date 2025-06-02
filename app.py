from flask import Flask, jsonify, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/professionals')
def get_professionals():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, profession, city FROM professionals")
    rows = cursor.fetchall()
    conn.close()
    return jsonify([{'name': r[0], 'profession': r[1], 'city': r[2]} for r in rows])

if __name__ == '__main__':
    app.run(port=8081)