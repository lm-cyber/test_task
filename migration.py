import psycopg2
from setting import DatabaseConnection


def create_tables():
    commands = (
        """
        CREATE TABLE executions (
            id SERIAL PRIMARY KEY,
            run_date TIMESTAMP NOT NULL,
            function_name VARCHAR(255) NOT NULL,
            arguments TEXT NOT NULL,
            success BOOLEAN NOT NULL
        )
        """,
        """
        CREATE TABLE results (
            id SERIAL PRIMARY KEY,
            execution_id INTEGER,
            params TEXT,
            prediction TEXT,
            error_message TEXT,
            FOREIGN KEY(execution_id) REFERENCES executions(id)
        )
        """)

    conn = None
    try:
        conn = DatabaseConnection.get_connection()
        cur = conn.cursor()

        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            DatabaseConnection.close_connection()


create_tables()
