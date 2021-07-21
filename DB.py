'''
mysql> 
create table books
(bookcode int (100) primary key,
 bookname varchar(100),
category varchar(100), 
author varchar(100), 
publication varchar(100), 
edition varchar(200),
price int (200)
);

# To add colume of review
ALTER TABLE books ADD review varchar(500);
'''
#Write a program to take input and add new books to the DB table 

import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='anand',database='bookstoredb')
curs=con.cursor()

try:

    # 1}Write a program to take input and add new books to the DB table
    code = int(input("enter the book code "))
    name = input("what is book name ")   
    cat = input("which category book ")
    auth = input("who is author of book ")
    pub = input("which publication book ")
    ed = int(input("what is edition of book "))
    pr = int(input("what is price of book "))

    curs.execute("insert into books values(%d,'%s','%s','%s','%s',%d,%d)" %(code,name,cat,auth,pub,ed,pr))
    con.commit()
    print('book added successfully')

    # Write a program to show list of all books

    
    curs.execute("select bookname from books")
    data = curs.fetchall()
    for i in data:
        print(i)
    con.commit()
    
     
    #Write a program to accept bookcode, search book in the table, show
    #the book details if found else display "not found" message

    a =int(input("enter bookcode"))
    curs.execute("select bookname from books where bookcode = %d" %a)   
    data = curs.fetchone()
    try:
        print("Your Book : %s" %data[0]) 
    except:
        print("Not Found")   
    
    # 6 Write a program to accept category like "romance" and display list of books of that category.


    ct = input("enter the category of book ")
    curs.execute("select * from books where category = '%s'" %ct)  
    b = curs.fetchall()
    print(b)
    

    #Write a program to accept bookcode, display the book data and ask
    #"Do you want to delete?" if "yes" delete the book from the table
    a =int(input("enter bookcode"))
    curs.execute("select bookname from books where bookcode = %d" %a)   
    data = curs.fetchone()
    try:
        print("Your Book : %s" %data[0]) 
        y = input("do you want to delete book(yes/no)")
        if "yes" == y.lower():
            curs.execute("delete from books where bookcode = %d" %a)  
            con.commit()
            print("your data deleted successfully")
    
    except:
        print("Not Found") 

    #Write a program to accept author and publication, display list of
    #books of the author-publication combination  
    a =input("enter author ")
    b = input("enter publication ")
    curs.execute("select bookname from books where author ='%s' and publication = '%s'" %(a,b))   
    data = curs.fetchall()
    try:
        for i in data:
            print(i)    
    except:
        print("Not Found")  

    #Write a program to accept bookcode and review, update the record with the review contents
    a =int(input("enter bookcode "))
    b = input("write review")
    curs.execute("update books set review = '%s' where bookcode = %d" %(b,a))
    print("your review updated successfully")   

except:
    print('please enter correct input')

con.close()

   
