import sqlite3
conn = sqlite3.connect('test1.db')
cursor=conn.cursor()
print("database opened")
cursor.execute("""CREATE TABLE IF NOT EXISTS MOVIES(
         NAME VARCHAR  NOT NULL,
         ACTOR     TEXT NOT NULL,
         ACTRESS     TEXT NOT NULL,
         DIRECTOR TEXT NOT NULL,
         YEAROFRELEASE INT NOT NULL)""")
print("table created succesfully")

records=[('83','ranbir','deepika','kabir',2021),('singam','suriya','anuska','rohit',2011)]

conn.executemany(""" INSERT INTO MOVIES
                    (
                    NAME,
                    ACTOR,
                    ACTRESS,
                    DIRECTOR,
                    YEAROFRELEASE)
                    
                VALUES  
                (?,?,?,?,?)""",records)


                
print("values inserted")

cursor.execute("SELECT  NAME, ACTOR,ACTRESS,DIRECTOR,YEAROFRELEASE from MOVIES")


print ("Operation done successfully");


conn.commit()
conn.close()