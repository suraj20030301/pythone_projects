import csv
import os
import emoji
import time
import pandas as pd
def add():
    print("Welcome to the Library add section")
    print(".................................")
    file=open("libary.csv",'a',newline='\r\n')
    ad=csv.writer(file)
    print("Enter Details......")
    print("\n")
    bookid=int(input("Book Id: "))
    bookname=input("Book Name: ")
    bookaut=input("Name of Author: ")
    price=int(input("Price: "))
    copy=int(input("No. of Copies: "))
    rec=[bookid,bookname,bookaut,price,copy]
    ad.writerow(rec)
    file.close()
    print("Book Added Successfully..","\U0001f44d")
    input("Press any key to continue___")
    print("\n"*10)


def modify():
    print("Welcome to the Library Modify section")
    file=open("libary.csv",'r',newline='\r\n')
    file1=open("temp.csv",'w',newline='\r\n')
    file1=open("temp.csv",'a',newline='\r\n')
    mod=csv.reader(file)
    mod1=csv.writer(file1)
    tempRec=int(input("Book Id : "))
    for rec in mod:
        if int(rec[0])==tempRec:
            print("...........................")
            print("Book id: ",rec[0])
            print("Book Name: ",rec[1])
            print("Name of Author: ",rec[2])
            print("Price: ",rec[3])
            print("No of Copies: ",rec[4])
            print("...........................")
            print("\n")
            ch=input("Y for Modify, \n N for Not: ")
            if ch=='Y' or ch=='y':
                bookid=int(input("Book Id: "))
                bookname=input("Book Name: ")
                bookaut=input("Name of Author: ")
                price=int(input("Price: "))
                copy=int(input("No. of Copies: "))
                rec=[bookid,bookname,bookaut,price,copy]
                mod1.writerow(rec)
                print("Book Successfully Modified....","\U0001f44d")
            else:
                mod1.writerow(rec)
        else:
            mod1.writerow(rec)
    file.close()
    file1.close()
    os.remove("libary.csv")
    os.rename("temp.csv","libary.csv")

    input("Press any key to continue___")
    print("\n"*10)

def delete():
    print("Welcome to the Library Delete section")
    file=open("libary.csv",'r',newline='\r\n')
    file1=open("temp.csv",'w',newline='\r\n')
    file1=open("temp.csv",'a',newline='\r\n')
    del1=csv.reader(file)
    del2=csv.writer(file1)
    tempRec=int(input("Book Id : "))
    for rec in del1:
        if int(rec[0])==tempRec:
            print("...........................")
            print("Book id: ",rec[0])
            print("Book Name: ",rec[1])
            print("Name of Author: ",rec[2])
            print("Price: ",rec[3])
            print("No of Copies: ",rec[4])
            print("...........................")
            print("\n")
            ch=input("Y for Delete, \n N for Not: ")
            if ch=='Y' or ch=='y':
                print("Book Successfully Deleted....","\U0001f44d")
            else:
                del2.writerow(rec)
        else:
            del2.writerow(rec)
    file.close()
    file1.close()
    os.remove("libary.csv")
    os.rename("temp.csv","libary.csv")

    input("Press any key to continue___")
    print("\n"*10)

def search():
    print("Welcome to the Library Search section")
    file=open("libary.csv",'r',newline='\r\n')
    sea=csv.reader(file)
    tempRec=int(input("Book Id : "))
    for rec in sea:
        print("Your Searching is ready wait...","\U0001F62C")
        if int(rec[0])==tempRec:
            time.sleep(1)
            print("\n")
            print("Your Searching is ready...","\U0001F62E")
            print("...........................")
            print("Book id: ",rec[0])
            print("Book Name: ",rec[1])
            print("Name of Author: ",rec[2])
            print("Price: ",rec[3])
            print("No of Copies: ",rec[4])
            print("...........................")
            break
    input("Press any key to continue___")
    print("\n"*10)
                
def listall():
    print("Welcome to the Library Search section")
    file=open("libary.csv",'r',newline='\r\n')
    li=csv.reader(file)
    print("Please wait...","\U0001F62C")
    time.sleep(1)
    print("...........................")
    print("Your List is ready...","\U0001F62E")
    print("\n")
    print("Book id     Book Name     Name of Author     Price     No of Copies")
    print("\n")
    for rec in li:
        print(rec[0],"  ",rec[1],"  ",rec[2],"  ",rec[3],"  ",rec[4])
    input("Press any key to continue___")
    print("\n"*10)

def bill():
    amt=0
    print("Welcome to the Library Bill section")
    print("...................................")
    file=open("libary.csv",'r',newline='\r\n')
    file1=open("bill.csv",'a',newline='\r\n')
    file2=open("temp.csv",'w',newline='\r\n')
    file2=open("temp.csv",'a',newline='\r\n')
    lib=csv.reader(file)
    bil=csv.writer(file1)
    mod=csv.writer(file2)
    print("\n")
    custName=input("Customer Name: ")
    contact=int(input("Contact No.: "))
    add=input("Address: ")
    tempRec=int(input("Book Id : "))
    qty=int(input("Quantity: "))
    x=[custName,contact,add,qty]
    print("\n")
    print("Please wait...","\U0001F62C")
    time.sleep(1)
    for rec in lib:
        if int(rec[0])==tempRec:
            '''part of program where quantity is reduced'''
            bookid=rec[0]
            bookname=rec[1]
            bookaut=rec[2]
            price=rec[3]
            copy=int(rec[4])-qty
            r=[bookid,bookname,bookaut,price,copy]
            mod.writerow(r)
            
            '''part of program where bill is generated'''
            amt=x[3]*int(rec[3])
            print("\n")
            print("Customer Name: ",x[0])
            print("Contact No.: ",x[1])
            print("Address: ",x[2])
            print("\n")
            print("Book id     Book Name     Price    Quantity     T.Amt")
            print(rec[0],"  ",rec[1],"  ",rec[3],"  ",x[3],"  ",amt)
            x.append(rec[1])
        else:
            mod.writerow(rec)
    x.append(amt)
    print("\n")
    print(x[0],",Your bill is created successfully...","\U0000263A")
    bil.writerow(x)
    file.close()
    file1.close()
    file2.close()
    os.remove("libary.csv")
    os.rename("temp.csv","libary.csv")
    print("\n")
    input("Press any key to continue___")
    print("\n"*10)
    
def showHis():
    print("Welcome to the Library Bill History")
    print("...................................")
    file1=open("bill.csv",'r',newline='\r\n')
    bil=csv.reader(file1)
    print("\n")
    print("Please wait...","\U0001F62C")
    time.sleep(1)
    
    print("CustName","\t","Contact","\t","Address","\t","Quantity","\t","BookName","\t","Amount")
    for rec in bil:
        print(rec)
    file1.close()
    input("Press any key to continue___")
    print("\n"*10)
   
def mainmenu():
    choice=0
    while choice !=8:
        print("\n")
        print("This software is developed By","\n","\t"," Suraj Kr. Gupta")
        print("\n")
        print("|-----------------------------|")
        print("|  LIBRARY MANAGEMENT SYSTEM  |")
        print("|-----------------------------|")
        print("\n")
        print("..............................")
        print("          MAIN MENU           ")
        print("..............................")
        print("1: Add a new book record")
        print("2: Modify existing book record")
        print("3: Delete existing book record")
        print("4: Search a book")
        print("5: List all record")
        print("6: Bill")
        print("7: Show Sale History")
        print("8: Exit")
        choice=int(input("Choose one : "))
        if choice==1:
            add()
        elif choice==2:
            modify()
        elif choice==3:
            delete()
        elif choice==4:
            search()
        elif choice==5:
            listall()
        elif choice==6:
            bill()
        elif choice==7:
            showHis()
        elif choice==8:
            print("\n"*10)
            print("Thank you browse again.....","\U0000263A")
            time.sleep(1)
            break  
mainmenu()
                   
