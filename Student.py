import sqlite3
from prettytable import PrettyTable
connection = sqlite3.connect("Student.db")

if len(connection.execute("SELECT name from sqlite_master WHERE type='table' AND name='STUDENT_DATA'").fetchall()) != 0:
    print("Table already exist")
else:
    connection.execute(''' CREATE TABLE STUDENT_DATA(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAME TEXT,
                    ROLL_NUMBER INTEGER,
                    ADMISSION_NUMBER INTEGER,
                    EXAM_NAME TEXT,
                    ENG_MARK INTEGER,
                    MATHS_MARK INTEGER,
                    PHY_MARK INTEGER,
                    CHEM_MARK INTEGER,
                    BIO_MARK INTEGER
    ) ''')
    print("Table created Successfully")

while True:
    print("Select an option from the menu")
    print("1.Add a Student ")
    print("2.View All Students ")
    print("3.Search a Student using Partial name ")
    print("4.Search a Student using either admission number or roll number ")
    print("5.Update a Student data with admission number ")
    print("6.Delete a Student data with admission number ")
    print("7.Display physics topper details ")
    print("8.Display count of total number of students ")
    print("9.Display average mark of students in english ")
    print("10.Display student details who scored less than average in maths ")
    print("11.Display student details who scored more than average in chemistry ")
    print("12.Exit ")

    choice = int(input("Enter a choice: "))


    if choice == 1:
        getname = input("Enter Student Name: ")
        getRno = input("Enter Roll Number: ")
        getAno = input("Enter Admission Number: ")
        getExamname = input("Enter Exam Name: ")
        getEng = input("Enter English Mark: ")
        getMath = input("Enter Maths Mark ")
        getPhy = input("Enter Physics Mark: ")
        getChem = input("Enter Chemistry Mark: ")
        getBio = input("Enter Biology Mark: ")

        connection.execute(" INSERT INTO STUDENT_DATA(NAME, ROLL_NUMBER, ADMISSION_NUMBER, EXAM_NAME, \
                ENG_MARK, MATHS_MARK, PHY_MARK, CHEM_MARK, BIO_MARK) VALUES('" + getname + "'," + getRno + ",\
                " + getAno + ",'" + getExamname + "'," + getEng + "," + getMath + "," + getPhy + "," + getChem + "," + getBio + ")")
        connection.commit()
        print("Inserted Successfully")


    elif choice == 2:
        result = connection.execute("SELECT * FROM STUDENT_DATA ORDER BY ROLL_NUMBER")
        table = PrettyTable(
            ["ID", "Student Name", "Roll Number", "Admission Number", "Exam Name", "English ",
             "Maths", "Physics", "Chemistry", "Biology"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
        print(table)

    elif choice == 3:
        getname = input("Enter Student Name (Single Letter or multiple letters): ")

        result = connection.execute("SELECT * FROM STUDENT_DATA WHERE NAME LIKE '%" + getname + "%'")
        table = PrettyTable(
            ["ID", "Student Name", "Roll Number", "Admission Number", "Exam Name", "English ",
             "Maths", "Physics", "Chemistry", "Biology"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
        print(table)

    elif choice == 4:
        getAno = input("Enter Admission number or Roll number: ")

        result = connection.execute("SELECT * FROM STUDENT_DATA WHERE ADMISSION_NUMBER="+getAno+" OR ROLL_NUMBER="+getAno)
        table = PrettyTable(
            ["ID", "Student Name", "Roll Number", "Admission Number", "Exam Name", "English ",
             "Maths", "Physics", "Chemistry", "Biology"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
        print(table)

    elif choice == 5:
        getAno = input("Enter Admission Number ")

        getname = input("Enter New Student Name: ")
        getrno = input("Enter New Roll Number: ")
        getexamname = input("Enter New Exam Name: ")
        geteng = input("Enter New English Mark: ")
        getmath = input("Enter New Maths Mark ")
        getphy = input("Enter New Physics Mark: ")
        getchem = input("Enter New Chemistry Mark: ")
        getbio = input("Enter New Biology Mark: ")

        connection.execute(" UPDATE STUDENT_DATA SET NAME='" + getname + "', ROLL_NUMBER=" + getrno + ", \
                EXAM_NAME='" + getexamname + "', ENG_MARK=" + geteng + ",\
                MATHS_MARK=" + getmath + ",PHY_MARK=" + getphy + ",CHEM_MARK=" + getchem + ",\
                BIO_MARK=" + getbio + " WHERE ADMISSION_NUMBER=" + getAno)
        connection.commit()
        print("Updated Successfully")
        result = connection.execute(
            "SELECT * FROM STUDENT_DATA WHERE ADMISSION_NUMBER=" + getAno)
        table = PrettyTable(
            ["ID", "Student Name", "Roll Number", "Admission Number", "Exam Name", "English ",
             "Maths", "Physics", "Chemistry", "Biology"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
        print(table)


    elif choice == 6:
        getAno = input("Enter Admission Number ")
        result = connection.execute("DELETE FROM STUDENT_DATA WHERE ADMISSION_NUMBER=" + getAno)
        connection.commit()

        print("Deleted Successfully")
        result = connection.execute("SELECT NAME,ADMISSION_NUMBER FROM STUDENT_DATA ORDER BY ADMISSION_NUMBER")
        table = PrettyTable(
            ["Student Name", "Admission Number"])

        for i in result:
            table.add_row([i[0], i[1]])
        print(table)

    elif choice == 7:
        result = connection.execute("SELECT * FROM STUDENT_DATA WHERE PHY_MARK=\
        (SELECT MAX(PHY_MARK) as physics FROM STUDENT_DATA )")
        table = PrettyTable(
            ["ID", "Student Name", "Roll Number", "Admission Number", "Exam Name", "English ",
             "Maths", "Physics", "Chemistry", "Biology"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
        print(table)

    elif choice == 8:
        result = connection.execute("SELECT COUNT(*) as count FROM STUDENT_DATA ")
        table = PrettyTable(
            ["Count"])
        for i in result:
            table.add_row([i[0]])
        print(table)

    elif choice == 9:
        result = connection.execute("SELECT AVG(ENG_MARK) as engmark FROM STUDENT_DATA ")
        table = PrettyTable(
            ["Average English Mark"])
        for i in result:
            table.add_row([i[0]])
        print(table)

    elif choice == 10:
        result = connection.execute(
            "SELECT * FROM STUDENT_DATA WHERE MATHS_MARK<(SELECT AVG(MATHS_MARK) as mmark FROM STUDENT_DATA )")
        table = PrettyTable(
            ["ID", "Student Name", "Roll Number", "Admission Number", "Exam Name", "English ",
             "Maths", "Physics", "Chemistry", "Biology"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
        print(table)

    elif choice == 11:
        result = connection.execute(
            "SELECT * FROM STUDENT_DATA WHERE CHEM_MARK>(SELECT AVG(CHEM_MARK) as cmark FROM STUDENT_DATA )")
        table = PrettyTable(
            ["ID", "Student Name", "Roll Number", "Admission Number", "Exam Name", "English ",
             "Maths", "Physics", "Chemistry", "Biology"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
        print(table)

    elif choice == 12:
        connection.close()
        print("successfully closed the application1")
        break

    else:
        print("Invalid Option")