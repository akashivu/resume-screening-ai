import sqlite3


def connect_db():

    connection = sqlite3.connect(
        "resume_screening.db"
    )

    return connection


def create_table():

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS resume_analysis (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            resume_name TEXT,

            score REAL,

            skills TEXT,

            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP

        )

    """)

    connection.commit()

    connection.close()


def save_resume_analysis(
    resume_name,
    score,
    skills
):

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""

        INSERT INTO resume_analysis (
            resume_name,
            score,
            skills
        )

        VALUES (?, ?, ?)

    """, (

        resume_name,
        score,
        skills

    ))

    connection.commit()

    connection.close()