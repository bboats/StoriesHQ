import psycopg2

con = psycopg2.connect(
    host = "rajje.db.elephantsql.com",
    database = "iijodcxj",
    user = "iijodcxj",
    password = 'dUF2jkkfv4eMrltoKQy8EF7aZsyBbAwE',
    port = '5432'
)

cursor = con.cursor()

cursor.execute()


# """
# CREATE TABLE empregados
# (
# nome VARCHAR (50) NOT NULL,
# idade INT NOT NULL
# )
#"""

con.commit()

con.close()