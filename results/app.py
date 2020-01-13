import database as db
from time import sleep
from flask import *
app = Flask(__name__)




@app.route("/")
def show_tables():
    i = 0
    while True:
        try:
            db.init_connection()
            break
        except Exception as e:
            if i >= 5:
                raise Exception("Could not connect to database")
            i += 1
            print('Got the exception ==> wait for 15s until retry')
            print(e)
            sleep(15)

    db.cursor.execute("select * from Results")
    data = db.cursor.fetchall()  # data from database
    print(data)
    return render_template("results.html", value=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='4000')
