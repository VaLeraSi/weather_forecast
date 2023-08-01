import psycopg2
import requests
import json


def save_weather_data():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="postgres",
        password="postgres"
    )

    cursor = conn.cursor()

    with open('weather_data.json', 'r') as file:
        weather_data = json.load(file)

    sql = "INSERT INTO weather (city, temperature, description) VALUES (%s, %s, %s)"

    try:
        city = weather_data['name']
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']

        cursor.execute(sql, (city, temperature, description))

        conn.commit()

        print("Данные успешно записаны в базу данных")
    except (Exception, psycopg2.Error) as error:
        print(error)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


save_weather_data()

def get_weather_from_db():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="postgres",
        password="postgres"
    )

    cursor = conn.cursor()

    sql = "SELECT temperature, description FROM weather WHERE city = %s"

    try:
        city = (input("Your city: "))

        cursor.execute(sql, (city,))

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except (Exception, psycopg2.Error) as error:
        print(error)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


get_weather_from_db()
#

