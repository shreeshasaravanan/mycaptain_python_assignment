import csv
def convert_csv(x):
    with open('stud_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(['Name','Age','Blood_grp','dob','sec','adno','gender'])
        writer.writerow(x)
        
print("admission for 2023-24 10th standard")
while True:
    lst=[]
    ct=1
    print("information of student",ct)
    name=input("Enter Name:")
    age=input("Enter Age:")
    bg=input("Enter blood group:")
    dob=input("Enter date of birth:")
    sec=input("Enter section:")
    adno=int(input("enter admission no:"))
    g=input("enter gender:")
    print("Check the entered info")
    print("Name:{}\nAge:{}\nBlood Group:{}\ndate of birth:{}\nsection:{}\n adno:{}\n gender:{}".format(name,age,bg,dob,sec,adno,g))
    check=input("Is given information are correct(yes/no):")
    if check=='yes':
        lst.extend([name,age,bg,dob,sec,adno,g])
        convert_csv(lst)
        ch=input("Do you wanna countinue(yes/no):")
        if ch=='no':
            break
        else:
            ct+=1
    else:
        print("requested to enter the value correctly ':)'")
