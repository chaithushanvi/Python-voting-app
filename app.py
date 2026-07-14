from flask import Flask, render_template, request
import mysql.connector
import time
import os

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "db")
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "root123")
DB_NAME = os.environ.get("DB_NAME", "votingdb")


def get_connection():
    while True:
        try:
            conn = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
            )

            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS votes(
                id INT AUTO_INCREMENT PRIMARY KEY,
                candidate VARCHAR(50)
            )
            """)

            conn.commit()
            return conn

        except Exception:
            time.sleep(5)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/vote", methods=["POST"])
def vote():

    candidate = request.form["candidate"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO votes(candidate) VALUES(%s)",
        (candidate,)
    )

    conn.commit()

    cursor.execute("""
    SELECT candidate, COUNT(*) FROM votes
    GROUP BY candidate
    """)

    result = cursor.fetchall()

    conn.close()

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
