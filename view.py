import psycopg2

def view_data():
    try:
        conn = psycopg2.connect(host="localhost", database="test", user="yt", password="yt")
        cur = conn.cursor()

        cur.execute("SELECT * FROM executions;")
        executions = cur.fetchall()

        cur.execute("SELECT * FROM results;")
        results = cur.fetchall()

        print("Executions:")
        for execution in executions:
            print(execution)

        print("Results:")
        for result in results:
            print(result)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

view_data()
