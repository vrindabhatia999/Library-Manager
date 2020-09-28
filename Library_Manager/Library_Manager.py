import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="vrinda",
    passwd="1234"

)
# CREATION OF TABLE AND DTABASE:

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Storeroom2112")
mycursor.execute("USE STORE")
mycursor.execute("CREATE TABLE signup1212(username VARCHAR(20), password VARCHAR(20))")

while True:
    print("""1:SIgnup
    2: Login""")

    ch = int(input("SIGNUP/LOGIN(1,2):"))

    if ch == 1:
        username = input("USERNAME:")
        pw = input("password")

        mycursor.execute("INSERT INTO signup VALUES('" + username + "','" + pw + "')")
        mydb.commit()

    if ch == 2:
        username = input("username:")

        mycursor.execute("SELECT username FROM signup WHERE username='" + username + "'")
        pot = mycursor.fetchone()

        if pot is not None:
            print("valid username")

            print("+++++++++++LOGIN SUCCESS+++++++++++")

            print("++++BOOK STORE++++")

            mycursor.execute(
                "CREATE TABLE AvailableBooks(Bookname VARCHAR(30) PRIMARY KEY,Genre VARCHAR(30), Quantity INT(3), Author VARCHAR(20), Publication VARCHAR(30), Price INT(4))")

            mycursor.execute(
                "CREATE TABLE Sell_rec(Customername VARCHAR(20), Phonenumber char(10) UNIQUE KEY, Bookname VARCHAR(30), Quantity INT(100),Price INT(4), FOREIGN KEY (Bookname) REFERENCES AvailableBooks(BookName))")

            mycursor.execute(
                "CREATE TABLE Staff_details(Name VARCHAR(40), gender VARCHAR(10), age INT(3), phonenumber CHAR(10) UNIQUE KEY, address VARCHAR(40))")
            mydb.commit()

            while True:
                print("""1: ADD BOOKS

                2: SEARCH BOOKS
                3: STAFF DETAILS
                4: SELL RECORD
                5: AVAILABLE BOOKS
                    6: TOTAL INCOME AFTER LATEST RESET
                    7: EXIT""")

                a = int(input("enter choice:"))

                if a == 1:
                    print("all info is mandatory")

                    book = str(input("enter book name:"))
                    genre = str(input("enter book genre:"))
                    quantity = int(input("enter quantity:"))
                    author = str(input("enter author:"))
                    publication = str(input("enter publication name:"))
                    price = int(input("enter price:"))

                    mycursor.execute("SELECT* FROM AvailableBooks WHERE Bookname='" + book + "'")
                    row = mycursor.fetchone()

                    if row is not None:
                        mycursor.execute("UPDATE AvailableBooks SET quantity=quantity+'" + str(
                            quantity) + "' WHERE Bookname='" + book + "'")
                        mydb.commit()

                        print("+++SUCCESSFULLY ADDED+++")

                    else:
                        mycursor.execute(
                            "INSERT INTO AvailableBooks(Bookname, genre, quantity, author, publication, price) VALUES('" + book + "','" + genre + "','" + str(
                                quantity) + "','" + author + "','" + publication + "','" + str(price) + "')")
                        mydb.commit()

                        print("+++successfulyy added+++")




                elif a == 2:
                    print("""1:search books by name
                        2:search by author
                        3:bye""")

                    l = int(input("enter choice:"))

                    if l == 1:
                        o = int(input("enter book to choose:"))

                        mycursor.execute("SELECT Bookname from AvailableBooks WHERE Bookname='" + o + "'")
                        tree = mycursor.fetchone()

                        if tree is not None:
                            print("book in stock")

                        else:
                            print("book out of stock")

                    elif l == 2:
                        p = int(input("enter author name:"))

                        mycursor.execute("SELECT Author FROM AvailableBooks WHERE Author='" + p + "'")
                        home = mycursor.fetchone()

                        if home is not None:
                            print("book available")

                            mycursor.execute("SELECT * FROM AvailableBooks WHERE Author='" + p + "'")

                            for z in mycursor:
                                print(z)

                        else:
                            print("book not available")
                            mydb.commit()





                elif a == 3:
                    print("""1: new staff entry:
                         2: existing staff details:
                         3:exit""")

                    ch = int(input("enter choice:"))

                    if ch == 1:

                        fname = str(input("enter first name:"))
                        gender = str(input("enter gender:"))
                        age = int(input("enter age:"))
                        phno = int(input("enter phone no:"))
                        add = str(input("enter address:"))

                        mycursor.execute(
                            "INSERT INTO Staff_details(Name,gender,age,phonenumber, address) VALUES('" + fname + "','" + gender + "','" + str(
                                age) + "','" + str(phno) + "','" + add + "')")
                        print("+++successfully added+++")
                        mydb.commit()
                    elif ch == 2:
                        mycursor.execute("SELECT* FROM Staff_details")
                        run = mycursor.fetchone()
                        for t in mycursor:
                            print(t)
                        if run is not None:
                            print("existing staff details:")
                            for t in mycursor:
                                print(t)
                        else:
                            print("no staff exists")
                        mydb.commit()
                    else:
                        print("byeee")

                elif a == 4:
                    print("sell history details")
                    mycursor.execute("SELECT * FROM Sell_rec")

                    for u in mycursor:
                        print(u)

                elif a == 5:
                    print("these are the avaialble books")
                    mycursor.execute("SELECT* FROM AvailableBooks")
                    for a in mycursor:
                        print(a)

                elif a == 6:
                    print("sell record")

                    mycursor.execute("SELECT SUM(price) FROM Sell_rec")

                    for v in mycursor:
                        print(v)

                elif a == 7:
                    break

            else:
                print("byee")

        else:
            print("bye2")


    else:
        break

