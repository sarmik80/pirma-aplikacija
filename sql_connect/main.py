import mysql.connector


try :
# Connect to server
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        databse= "countrydata")
    
    # Get a cursor
    cur = cnx.cursor()

    # Execute a query
    cur.execute("SELECT * FROM country_data")

    # Fetch one result
    row = cur.fetchone()
    print("select country_name FROM country_data where income > 15001 and gdpp < 8300")


except ConnectionError as e :
    # print(e)
    print("Prisijungimo klaida")


