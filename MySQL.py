import mysql.connector
from tkinter import messagebox

def Save_Data_MySQL(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R):
    try:
        mydb = mysql.connector.connect(host='localhost',user='root',password='4503Cham.')
        mycursor = mydb.cursor()
        print("Connection Established !!")
    except:
        messagebox.showerror("Connectio","Database connection not established !!")

    try:
        # print(B)
        # print(C)
        # print(D)
        # print(E)
        # print(F)
        # print(G)
        # print(H)
        # print(I)
        # print(J)
        # print(K)
        # print(L)
        # print(M)
        # print(N)
        # print(O)
        # print(P)
        # print(Q)
        # print(R)
        command="create database Heart_Data"
        mycursor.execute(command)

        command="use Heart_Data"
        mycursor.execute(command)

        command="create table data(user int auto_increment key not null, Name varchar(50), Data varchar(100), DOB varchar(100), age varchar(100), sex varchar(100), Cp archar(100), trestbps varchar(100), chol varchar(100), fbs varchar(100), restecg varchar(100), thalach varchar(100), exang varchar(100), oldpeak varchar(100), slope varchar(100), ca varchar(100), thal varchar(100), result varchar(100))"
        mycursor.execute(command)

        command="insert into data(Name,Data,DOB,age,sex,Cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,result) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    except:
        pass



Save_Data_MySQL('mr unknown','08/08/2023','1979','44','1','1','1','1','1','1','1','1','1','1','1','1','1')