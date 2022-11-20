import mysql.connector as mc
con=mc.connect(host='localhost',user='root',passwd='password')
cur=con.cursor()


# CREATION OF DATABASE 'BESTOW'
'''cur.execute('create database BESTOW')
if con.is_connected():
    print('done')
else:
    print('some issues')'''


# CREATION OF TABLE DONOR AND PATIENT
'''try:
    cur.execute('use BESTOW')
    cur.execute('create table PATIENT (P_ID varchar(30) primary key , P_NAME varchar(30) ,P_BG varchar(30),P_BT varchar(20), P_CONTACT varchar(30), P_ADDRESS varchar(30))')
    cur.execute ('create table DONOR (D_ID varchar(30) primary key , D_NAME varchar(30),D_BG varchar(30), D_BT varchar(20),D_CONTACT varchar(30), D_ADDRESS varchar(30) ,QTY varchar(30), DOD date)')
    print('tables created')
except:
    pass'''

# TO INSERT DONOR DETAILS
con=mc.connect(host='localhost',user='root',passwd='password',database='BESTOW')
cur=con.cursor()
def d_insert():
    print('-'*20,'PROVIDE THE REQUIRED INFORMATIONS','-'*20)
    did=input('enter the id of the donor: ')
    dname=input('enter the name of the donor: ')
    dbg=input('enter the blood group of the donor (A/B/AB/O): ')
    dbtype = input("enter the blood type of the donor(P/N): ")
    dcon=int(input('enter the contact of the donor: '))
    dadd=input('enter the address of the donor: ')
    bq=input('enter the amount of blood (ml) given by the donor: ')
    dod=input('enter the date of donation of blood [IN YYYY/MM/DD FORMAT]: ')
    qry=('insert into DONOR(D_ID,D_NAME,D_BG,D_BT,D_CONTACT,D_ADDRESS,QTY,DOD)values(%s,%s,%s,%s,%s,%s,%s,%s)')
    values=(did,dname,dbg,dbtype,dcon,dadd,bq,dod)
    cur.execute(qry,values)
    con.commit()
    print('Details of',dname,'successfully added')



#TO INSERT PATIENT DETAILS
con=mc.connect(host='localhost',user='root',passwd='password',database='BESTOW')
cur=con.cursor()
def p_insert():
    print('-'*20,'PROVIDE THE REQUIRED INFORMATION','-'*20)
    pid=input('enter the id of the patient: ')
    pname=input('enter the name of the patient: ')
    pbg=input('enter the blood group of the patient (A/B/AB/O): ')
    ptype=input('enter the blood type og the patient (P/N): ')
    pcon=int(input('enter the contact of the patient: '))
    padd=input('enter the address of the patient: ')
    qry=('insert into PATIENT(P_ID,P_NAME,P_BG,P_BT,P_CONTACT,P_ADDRESS)values(%s,%s,%s,%s,%s,%s)')
    values=(pid,pname,pbg,ptype,pcon,padd)
    cur.execute(qry,values)
    con.commit()
    print('Details of',pname,'successfully added')



#TO SEARCH FOR A DONOR DETAILS

#TO SEARCH WITH BLOOD GROUP
con=mc.connect(host='localhost',user='root',passwd='password',database='BESTOW')
cur=con.cursor()
def dbg_search():
    bg=input('enter the required blood group (A/B/AB/O): ')
    bt=input('enter the required blood type (P/N): ')
    stmt = ("select*from DONOR where D_BG = '{}' and D_BT = '{}'".format(bg,bt))
    cur.execute(stmt)
    data=cur.fetchall()
    print('D_ID        ','D_NAME        ','D_BG          ','D_BT         ','D_CONTACT        ','D_ADDRESS        ','BLOOD QTY(ml)        ','DATE OF DONATION')
    print('='*150)
    n=len(data)
    for i in range(0,n):
        print(data[i][0],'        ',data[i][1],'        ',data[i][2],'        ',data[i][3],'        ',data[i][4],'        ',data[i][5],'        ',data[i][6],'        ',data[i][7])



# TO SEARCH WITH DONOR NAME
con=mc.connect(host='localhost',user='root',passwd='password',database='BESTOW')
cur=con.cursor()
def dname_search():
    try:
        dname=input('enter the name of the donor: ')
        cur.execute('select D_NAME from DONOR')
        data=cur.fetchall()
        l=[]
        for row in data:
            l.append(row[0])
        if dname in l:
            command = ("select * from DONOR where D_Name = '{}'".format(dname))
            cur.execute(command)
            data=cur.fetchall()
            print('D_ID        ','D_NAME        ','D_BG          ','D_BT         ','D_CONTACT        ','D_ADDRESS        ','BLOOD QTY(ml)        ','DATE OF DONATION')
            print('='*150)
            n=len(data)
            for i in range(0,n):
                print(data[i][0],'        ',data[i][1],'        ',data[i][2],'        ',data[i][3],'        ',data[i][4],'        ',data[i][5],'        ',data[i][6],'        ',data[i][7])
        else:
            print('INVALID NAME')
    except:
        print('SOME ISSUES...')        

# TO SEARCH WITH DONOR ID
con=mc.connect(host='localhost',user='root',passwd='password',database='BESTOW')
cur=con.cursor()
def did_search():
    try:
        did=input('enter the id of the donor: ')
        command = ("select * from DONOR where D_ID = '{}'".format(did))
        cur.execute(command)
        datas=cur.fetchone()
        print('D_ID        ','D_NAME        ','D_BG          ','D_BT         ','D_CONTACT        ','D_ADDRESS        ','BLOOD QTY(ml)        ','DATE OF DONATION')
        print('='*150)
        print(datas[0],'         ',datas[1],'        ',datas[2],'        ',datas[3],'        ',datas[4],'        ',datas[5],'        ',datas[6],'        ',datas[7])
    except:
        print('INVALID ID')        


# TO SEARCH FOR A PATIENT DETAILS

# TO SEARCH WITH BLOOD GROUP
con=mc.connect(host='localhost',user='root',passwd='password',database='BESTOW')
cur=con.cursor()
def pbg_search():
    try:
        bg=input('enter the required blood group (A/B/AB/O): ')
        bt=input('enter the required blood type (P/N): ')
        stmt = ("select*from PATIENT where P_BG = '{}' and P_BT = '{}'".format(bg,bt))
        cur.execute(stmt)
        data=cur.fetchall()
        print('P_ID        ','P_NAME        ','P_BG        ','P_BT        ','P_CONTACT        ','P_ADDRESS')
        print('='*100)
        n=len(data)
        for i in range(0,n):
            print(data[i][0],'        ',data[i][1],'        ',data[i][2],'        ',data[i][3],'        ',data[i][4],'        ',data[i][5])
    except:
        print('SOME ISSUES...TRY AGAIN.....')
        


# TO SEARCH WITH PATIENT NAME
con=mc.connect(host='localhost',user='root',passwd='password',database='BESTOW')
cur=con.cursor()
def pname_search():
    try:
        pname=input('enter the name of the patient :')
        cur.execute('select P_NAME from PATIENT')
        data=cur.fetchall()
        l=[]
        for row in data:
            l.append(row[0])
        if pname in l:
            stmt=("select*from PATIENT where P_Name='{}'".format(pname))
            cur.execute(stmt)
            data=cur.fetchall()
            print('P_ID        ','P_NAME        ','P_BG        ','P_BT        ','P_CONTACT      ','P_ADDRESS')
            print('='*100)
            n=len(data)
            for i in range(0,n):
                print(data[i][0],'        ',data[i][1],'        ',data[i][2],'        ',data[i][3],'        ',data[i][4],'        ',data[i][5])
        else:
            print('INVALID NAME')
    except:
        print('SOME ISSUES....')
                
# TO SEARCH WITH PATIENT ID

con=mc.connect(host='localhost',user='root',passwd='password',database='BESTOW')
cur=con.cursor()
def pid_search():
    try:
        pid=input('enter the id of the patient :')
        stmt=("select*from PATIENT where P_ID='{}'".format(pid))
        cur.execute(stmt)
        data=cur.fetchone()
        print('P_ID        ','P_NAME        ','P_BG        ','P_BT        ','P_CONTACT        ','P_ADDRESS')
        print('='*100)
        print(data[0],'        ',data[1],'      ',data[2],'           ',data[3],'        ',data[4],'     ',data[5])
       
    except:
        print("INVALID ID")


# TO UPDATE DONOR DETAILS
con=mc.connect(host='localhost',user='root',passwd='password',database='BESTOW')
cur=con.cursor()
def d_update():
    att=input('Enter the attribute that you want to update :  ')
    if att in['Name','name','NAME']:
        cur.execute('select D_ID from DONOR')
        data=cur.fetchall()
        l=[]
        for row in data:
            l.append(row[0])
        did=input('ENTER THE ID OF THE DONOR :')
        if did in l:
            name=input('ENTER THE NEW NAME :  ')
            stmt=("update DONOR set D_NAME='{}' where D_ID='{}'".format(name,did))
            try:
                cur.execute(stmt)
                con.commit()
                print('..........SUCCESSFULLY UPDATED..........')
            except:
                pass
        else:
            print('ID IS INVALID')
    elif att in ['Blood group','Blood Group','BLOOD GROUP','blood group','BLOODGROUP','bloodgroup']:
        cur.execute('select D_ID from DONOR')
        data=cur.fetchall()
        l=[]
        for row in data:
            l.append(row[0])
        did=input('ENTER THE ID OF THE DONOR :')
        if did in l:
            dbg=input('ENTER THE NEW BLOOD GROUP :  ')
            stmt=("update DONOR set D_BG='{}' where D_ID='{}'".format(dbg,did))
            try:
                cur.execute(stmt)
                con.commit()
                print('..........SUCCESSFULLY UPDATED..........')
            except:
                pass
        else:
            print('ID IS INAVLID')

    elif att in ['blood type','Blood Type','Blood type','BLOOD TYPE','BLOODTYPE','bloodtype']:
        cur.execute('select D_ID from DONOR')
        data=cur.fetchall()
        l=[]
        for row in data:
            l.append(row[0])
        did=input('ENTER THE ID OF THE DONOR :')
        if did in l:
            dbt=input('ENTER THE NEW BLOOD TYPE :  ')
            stmt=("update DONOR set D_BT='{}' where D_ID='{}'".format(dbt,did))
            try:
                cur.execute(stmt)
                con.commit()
                print('..........SUCCESSFULLY UPDATED..........')
            except:
                pass
        else:
            print('ID ID INVALID')
        
    elif att in ['CONTACT','contact','Contact']:
        cur.execute('select D_ID from DONOR')
        data=cur.fetchall()
        l=[]
        for row in data:
            l.append(row[0])
        did=input('ENTER THE ID OF THE DONOR :')
        if did in l:
            dcon=input('ENTER THE NEW CONTACT :  ')
            stmt=("update DONOR set D_CONTACT='{}' where D_ID='{}'".format(dcon,did))
            try:
                cur.execute(stmt)
                con.commit()
                print('..........SUCCESSFULLY UPDATED..........')
            except:
                pass
        else:
            print('ID ID INVALID')
        
    elif att in ['address','Address','ADDRESS']:
        cur.execute('select D_ID from DONOR')
        data=cur.fetchall()
        l=[]
        for row in data:
            l.append(row[0])
        did=input('ENTER THE ID OF THE DONOR :')
        if did in l:
            dadd=input('ENTER THE NEW ADDRESS :  ')
            stmt=("update DONOR set D_ADDRESS='{}' where D_ID='{}'".format(dadd,did))
            try:
                cur.execute(stmt)
                con.commit()
                print('..........SUCCESSFULLY UPDATED..........')
            except:
                pass
        else:
            print('ID ID INVALID')
        
    elif att in ['Quantity','QUANTITY','quantity','qty','QTY','blood quantity','Blood quantity','BLOOD QUANTITY','bloodquantity','BLOODQUANTITY']:
        cur.execute('select D_ID from DONOR')
        data=cur.fetchall()
        l=[]
        for row in data:
            l.append(row[0])
        did=input('ENTER THE ID OF THE DONOR :')
        if did in l:
            qty=input('ENTER THE NEW QUANTITY :  ')
            stmt=("update DONOR set QTY='{}' where D_ID='{}'".format(qty,did))
            try:
                cur.execute(stmt)
                con.commit()
                print('..........SUCCESSFULLY UPDATED..........')
            except:
                pass
        else:
            print('ID ID INVALID')
        
    elif att in['date of donation','Date od donation','DATE OF DONATION','DOD','dod']:
        cur.execute('select D_ID from DONOR')
        data=cur.fetchall()
        l=[]
        for row in data:
            l.append(row[0])
        did=input('ENTER THE ID OF THE DONOR :')
        if did in l:
            dod=input('ENTER THE NEW DATE OF DONATION [YYYY/MM/DD] :  ')
            stmt=("update DONOR set DOD='{}' where D_ID='{}'".format(dod,did))
            try:
                cur.execute(stmt)
                con.commit()
                print('..........SUCCESSFULLY UPDATED..........')
            except:
                pass
        else:
            print('ID ID INVALID')
            
    else:
        print('*****ENTER THE CORRECT ATTRIBUTE*****')



# TO DISPLAY THE FULL TABLE DONOR
con=mc.connect(host='localhost',user='root',passwd='password',database='BESTOW')
cur=con.cursor()
def show_donor():
    try:
        print('D_ID','          ','D_NAME','          ','D_BG','          ','D_BT','          ','D_CONTACT','          ','D_ADDRESS','          ','QUANTITY','          ','DATE OF DONATION')
        print('='*160)
        command='select * from DONOR'
        cur.execute(command)
        data=cur.fetchall()
        n=len(data)
        for i in range(n):
            print(data[i][0],'          ',data[i][1],'          ',data[i][2],'          ',data[i][3],'          ',data[i][4],'          ',data[i][5],'          ',data[i][6],'          ',data[i][7])
    except:
        print('SOME ISSUES...')
    
        
            
#TO UPDATE PATIENT DETAILS

con=mc.connect(host='localhost',user='root',passwd='password',database='BESTOW')
cur=con.cursor()
def p_update():
    att=input('ENTER THE ATTRIBUTE THAT YOU WANT TO UPDATE  : ')
    if att in ['NAME','name','Name']:
        cur.execute('select P_ID from PATIENT')
        data=cur.fetchall()
        l=[]
        for row in data:
            l.append(row[0])
        pid=input('ENTER THE ID OF THE PATIENT :')
        if pid in l:
            pname=input('ENTER THE NEW NAME : ')
            stmt=("update PATIENT set P_NAME='{}' where P_ID='{}'".format(pname,pid))
            try:
                cur.execute(stmt)
                con.commit()
                print('..........SUCCESSFULLY UPDATED..........')
            except:
                pass
        else:
            print('ID IS INVALID')
    elif att in ['Blood group','Blood Group','BLOOD GROUP','blood group','bloodgroup','BLOODGROUP']:
        cur.execute('select P_ID from PATIENT ')
        data=cur.fetchall()
        l=[]
        for row in data:
            l.append(row[0])
        pid=input('ENTER THE ID OF THE PATIENT :')
        if pid in l:
            pbg=input('ENTER THE NEW BLOOD GROUP : ')
            stmt=("update PATIENT set P_BG='{}' where P_ID='{}'".format(pbg,pid))
            try:
                cur.execute(stmt)
                con.commit()
                print('..........SUCCESSFULLY UPDATED..........')
            except:
                    pass
        else:
            print('ID IS INVALID')        
    elif att in  ['blood type','Blood Type','Blood type','BLOOD TYPE','bloodtype','BLOODTYPE']:
         cur.execute('select P_ID from PATIENT ')
         data=cur.fetchall()
         l=[]
         for row in data:
             l.append(row[0])
         pid=input('ENTER THE ID OF THE PATIENT :')
         if pid in l:
             pbt=input('ENTER THE NEW BLOOD TYPE  :')
             stmt=("update PATIENT set P_BT='{}' where P_ID='{}'".format(pbt,pid))
             try:
                 cur.execute(stmt)
                 con.commit()
                 print('..........SUCCESSFULLY UPDATED..........')
             except:
                 pass
         else:
             print('ID IS INVALID')
    elif att in ['CONTACT','contact','Contact']:
         cur.execute('select P_ID from PATIENT')
         data=cur.fetchall()
         l=[]
         for row in data:
             l.append(row[0])
         pid=input('ENTER THE ID OF THE PATIENT :')
         if pid in l:
             pcon=input('ENTER THE NEW CONTACT :')
             stmt=("update PATIENT set P_CONTACT='{}' where P_ID='{}'".format(pcon,pid))
             try:
                 cur.execute(stmt)
                 con.commit()
                 print('..........SUCCESSFULLY UPDATED..........')
             except:
                 pass
         else:
             print('ID IS INVALID')
    elif att in ['address','Address','ADDRESS']:
         cur.execute('select P_ID from PATIENT ')
         data=cur.fetchall()
         l=[]
         for row in data:
             l.append(row[0])
         pid = input('ENTER THE PATIENT ID : ')
         if pid in l:
                 padd=input('ENTER THE NEW ADDRESS :')
                 stmt=("update PATIENT set P_ADDRESS='{}' where P_ID='{}'".format(padd,pid))
                 try:
                     cur.execute(stmt)
                     con.commit()
                     print('..........SUCCESSFULLY UPDATED..........')
                 except:
                     pass
         else:
             print('ID IS INVALID')
        
    else:
        print('*****ENTER THE CORRECT ATTRIBUTE*****')
             
          

# TO DISPLAY THE FULL TABLE PATIENT

con=mc.connect(host='localhost',user='root',passwd='password',database='BESTOW')
cur=con.cursor()
def show_patient():
    try:
        print('P_ID','          ','P_NAME','          ','P_BG','          ','P_BT','          ','P_CONTACT','          ','P_ADDRESS')
        print('='*160)
        command='select * from PATIENT'
        cur.execute(command)
        data=cur.fetchall()
        n=len(data)
        for i in range(n):
            print(data[i][0],'          ',data[i][1],'          ',data[i][2],'          ',data[i][3],'          ',data[i][4],'          ',data[i][5])
    except:
        print('SOME ISSUES...')


# TO DELETE THE RECORD OF A DONOR

con=mc.connect(host='localhost',user='root',passwd='password',database='BESTOW')
cur=con.cursor()
def del_from_donor():
    did=input('ENTER THE ID OF THE DONOR TO BE DELETED : ')
    cur.execute('select D_ID from DONOR ')
    data=cur.fetchall()
    l=[]
    for row in data:
        l.append(row[0])
    if did in l:
        stmt=("delete from DONOR where D_ID ='{}'".format(did))
        try:
            cur.execute(stmt)
            con.commit()
            print('........SUCCESSFULLY DELETED.........')
        except:
            pass
    else:
        print('ID DOES NOT EXIST')        

# TO DELETE THE RECORD OF A PATIENT

con=mc.connect(host='localhost',user='root',passwd='password',database='BESTOW')
cur=con.cursor()
def del_from_patient():
    pid=input('ENTER THE ID OF THE PATIENT TO BE DELETED : ')
    cur.execute('select P_ID from PATIENT ')
    data=cur.fetchall()
    l=[]
    for row in data:
        l.append(row[0])
    if pid in l:
        stmt=("delete from PATIENT where P_ID ='{}'".format(pid))
        try:
            cur.execute(stmt)
            con.commit()
            print('........SUCCESSFULLY DELETED.........')
        except:
            pass
    else:
        print('ID DOES NOT EXIST')        


# TO EXIT THE PROGRAM

con=mc.connect(host='localhost',user='root',passwd='password',database='BESTOW')
cur=con.cursor()
def mc_exit():
    con.close()
    


# MAIN PROGRAM

print('-'*50,'   BESTOW   ','-'*50)
print("\t                                      GIVE THE GIFT OF BLOOD\n")
print(" AVAILABLE OPERATIONS ")
print('-'*25)
print('\t 1. SHOW FULL RECORDS\n')
print('\t 2. INSERT\n')
print('\t 3. SEARCH\n')
print('\t 4. UPDATE\n')
print('\t 5. DELETE\n')
print('\t 6. EXIT\n')
ch=int(input('ENTER THE NUMBER SHOWN NEXT TO OPTIONS TO CHOOSE :  '))

if ch==1:
    print('\t 1. FULL RECORDS OF DONORS\n')
    print('\t 2. FULL RECORDS OF PATIENTS\n')
    s=int(input('ENTER THE NUMBER SHOWN NEXT TO THE OPTION TO CHOOSE : '))
    if s==1:
        show_donor()
    elif s==2:
        show_patient()
    else:
        print('...ENTER A VALID CHOICE...')
elif ch==2:
    print('\t 1. INSERT INTO DONOR\n')
    print('\t 2. INSERT INTO PATIENT\n')
    s=int(input('ENTER THE NUMBER SHOWN NEXT TO OPTIONS TO CHOOSE : '))
    if s==1:
        d_insert()
    elif s==2:
        p_insert()
    else:
        print('...ENTER A VALID CHOICE...')
elif ch==3:
    print('\t 1. SEARCH A DONOR DETAIL\n')
    print('\t 2. SEARCH A PATIENT DETAIL\n')
    s=int(input('ENTER THE NUMBER SHOWN NEXT TO THE OPTIONS TO CHOOSE : '))
    if s==1:
        print('\t 1. SEARCH USING DONOR ID\n')
        print('\t 2. SEARCH USING DONOR NAME\n')
        print('\t 3. SEARCH USING BLOOD GROUP DETAILS\n')
        c=int(input('ENTER THE NUMBER SHOWN NEXT TO THE OPTIONS TO CHOOSE : '))
        if c==1:
            did_search()
        elif c==2:
            dname_search()
        elif c==3:
            dbg_search()
        else:
            print('...ENTER A VALID CHOICE...')
    elif s==2:
        print('\t 1. SEARCH USING PATIENT ID\n')
        print('\t 2. SEARCH USING PATIENT NAME\n')
        print('\t 3. SEARCH USING BLOOD GROUP DETAILS\n')
        c=int(input('ENTER THE NUMBER SHOWN NEXT TO THE OPTIONS TO CHOOSE : '))
        if c==1:
            pid_search()
        elif c==2:
            pname_search()
        elif c==3:
            pbg_search()
        else:
            print('...ENTER A VALID CHOICE...')
    else:
        print('...ENTER A VALID CHOICE...')
elif ch==4:
    print('\t 1. UPDATE DONOR RECORDS\n')
    print('\t 2. UPDATE PATIENT RECORDS\n')
    s=int(input('ENTER THE NUMBER SHOWN NEXT TO THE OPTIONS TO CHOOSE : '))
    if s==1:
        d_update()
    elif s ==2 :
        p_update()
    else:
        print('...ENTER A VALID CHOICE...')
elif ch==5:
    print('\t 1. DELETE DONOR RECORDS\n')
    print('\t 2. DELETE PATIENT RECORDS\n')
    s= int(input('ENTER THE NUMBER SHOWN NEXT TO THE OPTIONS TO CHOOSE : '))
    if s==1:
        del_from_donor()
    elif s==2:
        del_from_patient()
    else:
        print('...ENTER A VALID CHOICE...')
elif ch==6:
    print('\t                   THANKS FOR USING BESTOW\n')
    print('\t                         EXITING.....\n')
    mc_exit()
else:
    print('...ENTER A VALID CHOICE...')
        
        
        
        
        
        
            
            
            
        
        
        
        
    
       








        
        
        
            
        
        



    
