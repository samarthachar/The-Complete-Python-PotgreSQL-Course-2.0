import psycopg2

url = "postgresql://neondb_owner:npg_Kchro7zDamZ8@ep-snowy-wind-abx8yt61-pooler.eu-west-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
connection = psycopg2.connect(url)

cursor = connection.cursor()
cursor.execute("SELECT * FROM users;")
first_user = cursor.fetchall()
print(first_user)



connection.close()