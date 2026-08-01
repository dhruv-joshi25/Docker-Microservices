from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

@app.route('/api/health')
def health():
    return jsonify({"status": "backend is running"})

def get_db():
    return psycopg2.connect(
        host="database",
        port=5432,
        database=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD")
    )
@app.route('/api/dbtest')
def dbtest():
    try:
        conn = get_db()
        conn.close()
        return jsonify({"database": "connected successfully"})
    except Exception as e:
        return jsonify({"database": "connection failed", "error": str(e)})


@app.route('/api/message')
def message():
    return jsonify({"message": "Hello from the backend service!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
