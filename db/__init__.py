import psycopg2
import json
from datetime import datetime
from functools import wraps


def db_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        conn = psycopg2.connect(host="localhost", database="test", user="yt",
                                password="yt")
        cur = conn.cursor()

        try:
            result = func(*args, **kwargs)

            cur.execute("""
                INSERT INTO executions (run_date, function_name, arguments, success)
                VALUES (%s, %s, %s, %s) RETURNING id
            """, (datetime.now(), func.__name__, json.dumps({'args': args, 'kwargs': kwargs}), True))
            execution_id = cur.fetchone()[0]
            cur.execute("""
                INSERT INTO results (execution_id, params, prediction)
                VALUES (%s, %s, %s)
            """, (execution_id, json.dumps(result[1]), json.dumps(list(result[0]))))

        except Exception as e:
            cur.execute("""
                INSERT INTO executions (run_date, function_name, arguments, success)
                VALUES (%s, %s, %s, %s) RETURNING id
            """, (datetime.now(), func.__name__, json.dumps({'args': args, 'kwargs': kwargs}), False))
            execution_id = cur.fetchone()[0]
            cur.execute("""
                INSERT INTO results (execution_id, error_message)
                VALUES (%s, %s)
            """, (execution_id, str(e)))

        finally:
            conn.commit()
            cur.close()
            conn.close()

        return result

    return wrapper
