print("**********WELCOME**********")
print("HEALTH MANGEMENT SYSTEM")
lock=1
retrive=2
diet=1
exercise=2
RAM=1
SHYAM=2
RAJESH=3
def gettime():
    import datetime
    return datetime.datetime.now()
time=str(gettime())

a=int(input("Enter Your Choice \n 1-lock \n 2-Retrive \n"))
b=int(input("Enter Your Choice \n 1-Diet \n 2-Exercise \n"))
c=int(input("Choose Your Clients \n 1-RAM \n 2-SHYAM \n 3-RAJESH \n"))
if a==lock and b==diet and c==RAM:
    with open("RAM_diet.txt","a") as f1:
        data=str(input("What Do You Want to Add ?"))
        f1.write(str(gettime())+"  "+data+"\n")
elif a==lock and b==diet and c==SHYAM :
    with open("SHYAM_diet.txt","a") as f2:
        data1=str(input("What Do You Want to Add ?"))
        f2.write(time+"  "+data1+"\n")

elif a==lock and b==diet and c==RAJESH:
    with open("RAJESH_diet.txt","a") as f2:
        data2=str(input("What Do You Want to Add ?"))
        f2.write(time+"  "+data2+"\n")

elif a==lock and b==exercise and c==RAM :
    with open("RAM_diet.txt","a") as f2:
        data1=str(input("What Do You Want to Add ?"))
        f2.write(time+"  "+data1+"\n")


elif a==lock and b==exercise and c==SHYAM :
    with open("SHYAM_diet.txt","a") as f2:
        data1=str(input("What Do You Want to Add ?"))
        f2.write(time+"  "+data1+"\n")

elif a==lock and b==exercise and c==RAJESH :
    with open("RAJESH_diet.txt","a") as f2:
        data1=str(input("What Do You Want to Add ?"))
        f2.write(time+"  "+data1+"\n")
elif a==retrive and b==diet and c==RAM:
    with open("Ram_Diet.txt","r") as f3:
        print(f3.read())

elif a==retrive and b==diet and c==SHYAM:
    with open("Ram_Diet.txt","r") as f3:
        print(f3.read())
elif a==retrive and b==diet and c==RAJESH:
    with open("Ram_Diet.txt","r") as f3:
        print(f3.read())
elif a==retrive and b==exercise and c==RAM:
    with open("Ram_Diet.txt", "r") as f3:
        print(f3.read())
elif a==retrive and b==exercise and c==SHYAM:
    with open("Ram_Diet.txt", "r") as f3:
        print(f3.read())
elif a==retrive and b==exercise and c==RAJESH:
    with open("Ram_Diet.txt", "r") as f3:
        print(f3.read())
print("****************************************")
