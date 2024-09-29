from fastapi import FastAPI
import pymysql

app = FastAPI()

db_connection = pymysql.connect(
    host='localhost',
    user='root',
    password='dbuserdbuser',
    db='expense_tracker_users'
)

db_cursor = db_connection.cursor()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/select_all")
async def select():
    db_cursor.execute("select * from users")
    return db_cursor.fetchall()
