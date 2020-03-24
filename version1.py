from tkinter import *
import sqlite3

root = Tk()
root.title("Database")
root.iconbitmap()
root.geometry("400x600")

#Databases

#Create a Database or connect to one
conn = sqlite3.connect('STUDENT_DATABASE.db')

#Create Cursor
c=conn.cursor()

#Create Table
'''c.execute("""CREATE TABLE Student_table (
    Student_ID integer PRIMARY KEY ,
    Name text,
    Class integer,
    Mobile integer,
    Email text) """)
''' 

#Create Edit Function to update a record
def update():
    #Create a Database or connect to one
    conn = sqlite3.connect('STUDENT_DATABASE.db')
    #Create Cursor
    c=conn.cursor()

    record_id = delete_box.get()

    c.execute('''UPDATE Student_table SET
        Name = :name,
        Class = :class,
        Mobile = :mobile,
        Email = :email

        WHERE Student_ID = :Student_ID''',
        { 
            "name": Name_editor.get(),
            "class": Class_editor.get(),
            "mobile": Mobile_editor.get(),
            "email": Email_editor.get(),

            "Student_ID": record_id
        })


    #Commit changes
    conn.commit()
    #Close connection
    conn.close()
    

def edit():
    editor = Tk()
    editor.title("Update a record")
    editor.geometry("400x350")
    #Create a Database or connect to one
    conn = sqlite3.connect('STUDENT_DATABASE.db')
    #Create Cursor
    c=conn.cursor()
    
    record_id = delete_box.get() 
    #Query the database
    c.execute("SELECT * FROM Student_table WHERE Student_ID = " + record_id)
    records= c.fetchall()
     
    #Create Global variables for text box names
    global Name_editor
    global Class_editor
    global Mobile_editor
    global Email_editor

    #Create text boxes
    Name_editor = Entry(editor, width = 30)
    Name_editor.grid(row= 1, column = 1, padx = 20)

    Class_editor = Entry(editor, width = 30)
    Class_editor.grid(row= 2, column = 1)

    Mobile_editor = Entry(editor, width = 30)
    Mobile_editor.grid(row= 3, column = 1)

    Email_editor = Entry(editor, width = 30)
    Email_editor.grid(row= 4, column = 1)

    #Create text boxes labels
    Student_ID_label = Label(editor, text = "STUDENT ID " + str(delete_box.get()) )
    Student_ID_label.grid(row = 0, column=0, pady=(10,0) )
    Name_label = Label(editor, text = "NAME")
    Name_label.grid(row = 1, column=0,)
    Class_label = Label(editor, text = "CLASS")
    Class_label.grid(row = 2, column=0)
    Mobile_label = Label(editor, text = "MOBILE")
    Mobile_label.grid(row = 3, column=0)
    Email_label = Label(editor, text = "EMAIL")
    Email_label .grid(row = 4, column=0,)

    #Loop through results
    for record in records:
        Name_editor.insert(0, record[1])
        Class_editor.insert(0, record[2])
        Mobile_editor.insert(0, record[3])
        Email_editor.insert(0, record[4])

   
    #Create a Save Button to save edited record
    edit_btn = Button(editor, text='SAVE Records', command= update)
    edit_btn.grid(row = 5, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

 

#Creat function for delete
def delete():
    #Create a Database or connect to one
    conn = sqlite3.connect('STUDENT_DATABASE.db')
    #Create Cursor
    c=conn.cursor()

    #Delete a record
    c.execute("DELETE from Student_table WHERE Student_ID= " + delete_box.get())

    delete_box.delete(0, END)

    #Commit changes
    conn.commit()
    #Close connection
    conn.close()

#Create submit function for database
def submit():
    #Create a Database or connect to one
    conn = sqlite3.connect('STUDENT_DATABASE.db')
    #Create Cursor
    c=conn.cursor()

    #Insert into table
    c.execute("INSERT INTO Student_table VALUES (:Student_ID, :Name, :Class, :Mobile, :Email)",
             {
                   'Student_ID': Student_ID.get(),
                   'Name': Name.get(),
                   'Class': Class.get(),
                   'Mobile': Mobile.get(),
                   'Email': Email.get(),
             })

    #Commit changes
    conn.commit()

    #Close connection
    conn.close()

    #Clear the text boxes
    Student_ID.delete(0, END)
    Name.delete(0, END)
    Class.delete(0, END)
    Mobile.delete(0, END)
    Email.delete(0, END)

#Create Query function
def query():
    #Create a Database or connect to one
    conn = sqlite3.connect('STUDENT_DATABASE.db')
    #Create Cursor
    c=conn.cursor()

    #Query the database
    c.execute("SELECT * FROM Student_table ")
    records= c.fetchall()
    #print(records)
    
    #Loop through results
    print_records =''
    for record in records:
        print_records += str(record[1]) + '\t' + str(record[0]) +"\n"

    query_label = Label(root, text = print_records)
    query_label.grid(row=12, column= 0, columnspan=2)    


    #Commit changes
    conn.commit()

    #Close connection
    conn.close()


#Create text boxes
Student_ID = Entry(root, width = 30)
Student_ID.grid(row= 0, column = 1, padx = 20)

Name = Entry(root, width = 30)
Name.grid(row= 1, column = 1)

Class = Entry(root, width = 30)
Class.grid(row= 2, column = 1)

Mobile = Entry(root, width = 30)
Mobile.grid(row= 3, column = 1)

Email = Entry(root, width = 30)
Email.grid(row= 4, column = 1)

delete_box = Entry(root, width = 30)
delete_box.grid(row=9, column=1, pady=5)

#Create text boxes labels
Student_ID_label = Label(root, text = "STUDENT ID")
Student_ID_label.grid(row = 0, column=0, pady=(10,0))
Name_label = Label(root, text = "NAME")
Name_label.grid(row = 1, column=0)
Class_label = Label(root, text = "CLASS")
Class_label.grid(row = 2, column=0)
Mobile_label = Label(root, text = "MOBILE")
Mobile_label.grid(row = 3, column=0)
Email_label = Label(root, text = "EMAIL")
Email_label.grid(row = 4, column=0)
delete_box_label = Label(root, text="SELECT ID")
delete_box_label.grid(row=9, column=0, pady=5)

#Create Submit Button
submit_btn = Button(root, text = "ADD Record to Database", command = submit)
submit_btn.grid(row = 6, column = 0, columnspan = 2, pady=10 , padx=10, ipadx=100)

#Create Query Button
query_btn = Button(root, text='SHOW Records', command= query)
query_btn.grid(row = 7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Create a Delete button
delete_btn = Button(root, text='DELETE Records', command= delete)
delete_btn.grid(row = 10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

#Create an Update Button
edit_btn = Button(root, text='UPDATE Records', command= edit)
edit_btn.grid(row = 11, column=0, columnspan=2, pady=10, padx=10, ipadx=136)


#Commit changes
conn.commit()

#Close connection
conn.close()

root.mainloop()
