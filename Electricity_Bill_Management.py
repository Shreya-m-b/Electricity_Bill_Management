import random
from datetime import date
fa1=85;fa2=95;fa3=150;e1=4.1;e2=5.55;e3=7.10;e4=8.5;
f1=95;f2=105;f3=150;er1=8.35;er2=9.35;
       

def m():
 print("Choose the appropriate category:")
 print("1.Household/Domestic","2.Industrial/Commercial",sep="\n")
 a=int(input("Enter your choice: "))
 if(a>2 or a<1):
     print("Invalid choice , Try again")
     exit(0)
 if(a==1):
    aa=input("Enter your Aadhar number: ")
    details={"AJ8547H210":("Sneha Sharma","#145,Whitefield","9665411702"),"QG4478A956":("Nitin G","#66,Rajajinagar","8821579960"),"AS4423B230":("Adithya S B","#578,Malleshwaram","9665411280"),"DW1145L962":("Spoorthi K","#41,Nagarbhavi","9954412017"),"HK5847Q7289":("Harsh G","#114,Vijayanagar","8840035678"),"PR8510G566":("Veena N","#125,JP nagar","9663214755")}
    details_list=list(details)
    if(aa not in details_list):
       print("Sorry, details not found. Enter valid credentials and try again")
       exit(0)                                  
 if(a==1):
         print("---------Household bills----------")
         print("Do you want to:")
         print("1. Generate monthly electricity bill")
         print("2. View due bills in the past 6 months")
         b=int(input("Enter your choice: "))
 
         if(b==1):
                  print("-----Generation of monthly bills-----")
                  #input : units(u) , load sanctioned (ls)
                  u=float(input("Enter the units consumed: "))
                  sl=int(input("Enter the load sanctioned: "))
                  t1=0.0
                  t2=0.0
                  if(sl>=0 and sl<=1):
                          t1=sl*fa1
                  elif(sl>1 and sl<=50):
                          t1=1*fa1+(sl-1)*fa2
                  else:
                          t1=1*fa1+49*fa2+(sl-50)*fa3
                  #sanctioned load price calculated
                  if(u>=0 and u<=50):
                         t2=u*e1
                  elif(u>=51 and u<=100):
                         t2=(50*e1)+(u-50)*e2
                  elif(u>=101 and u<=200):
                         t2=(50*e1)+(50*e2)+(u-100)*e3
                  else:
                         t2=(50*e1)+(50*e2)+(100*e3)+(u-200)*e4
                 #total enery consumption price calculated
                  total=t1+t2
                  fac=0.5*u
                  tax=(6.3/100.0)*total
                  net=total+tax-fac
                  net=round(net)
                  k=random.randint(1120,1996)
                  print("----------Bill----------")
                  print(" Date: ",date.today())
                  print(" Bill number: ",k,"\n","Sanctioned Load: ",sl,"\n","Units consumed: ",u)
                  print(" Aadhar number: ",aa)
                  print(" Name: ",details[aa][0],"\n","Address: ",details[aa][1],"\n","Registered phone number: ",details[aa][2])
                  print(" Amount to be paid: ",net)
         elif(b==2):
                  print("-----View due bills in the past 6 months-----")
                  dues={"AJ8547H210":(),"QG4478A956":((12,582,"12/12/2020"),(2,866,"5/2/2022")),"AS4423B230":(),"HK5847Q7289":(),"DW1145L962":(10,267,"24/10/2020")}
                  QG4478A956={12:(582,"12/12/2020"),2:(866,"5/2/2022")}
                  AS4423B230={};HK5847Q7289={}
                  DW1145L962={10:(267,"24/10/2020"),12:(552,"15/12/2021"),1:(773,"11/1/2022")}
                  PR8510G566={2:(1286,"16/2/2022")}
                 
                 
       
 if(a==2):
      print("-----Generation of commercial bills-----")
      #input : units(u) , load sanctioned (ls)
      u=float(input("Enter the units consumed: "))
      sl=int(input("Enter the load sanctioned: "))
      t1=0.0
      t2=0.0
      if(sl>=0 and sl<=1):
          t1=sl*f1
      elif(sl>1 and sl<=50):
         t1=1*f1+(sl-1)*f2
      else:
         t1=1*f1+49*f2+(sl-50)*f3
       
      if(u>=0 and u<=50):
         t2=u*er1
      else:
         t2=(50*er1)+(u-50)*er2

      total=t1+t2
      fac=0.5*u
      tax=(12.4/100.0)*total
      net=total+tax-fac
      net=round(net)
      print("Amount to be paid: ",net)  

def main(z):
  if(z==2):
    fa1=85;fa2=95;fa3=150;e1=4.1;e2=5.55;e3=7.10;e4=8.5;
    f1=95;f2=105;f3=150;er1=8.35;er2=9.35;    
    m()
def rateh(a1,b1,c1,d1,e,f1,g1):
              fa1=a1;fa2=b1;fa3=c1;e1=d1;e2=e;e3=f1;e4=g1;
              m()
def ratei( h1,i1,j1,k1,l1):
             f1=h1;f2=i1;f3=j1;er1=k1;er2=l1;
             m()




print("\t\t\tBangalore Electricity Supply Company Limited")
print("Choose an appropriate option:")
print("1.Admin\t 2.Consumer")
k=int(input("Enter your choice: "))
def inc():
  print("Invalid input , Try again")
  exit(0)
if(k<0 or k>2):
  inc()
if(k==1):
     counter=0;
     password="pesu@123"
     word=input("Enter the password: ")
     if(word!=password):
        inc()
     else:
       print("Do you want to change the rates of:\n1.Household bills \n2.Industrial bills")
       rc=int(input("Enter your choice: "))
       if(rc<0 or rc>2):
          inc()
       if(rc==1):
          print("Update the Fixed charges")
          fa1=float(input("For 1st KW:"));fa2=float(input("For every additional KW up to and inclusive of 50 KW:"))
          fa3=float(input("For every additional KW above 50 KW:"))
          print("Update Energy consumption charges")
          e1=float(input("0 to 50 KWH:"));e2=float(input("51 to 100 KWH:"));e3=float(input("101 to 200 KWH: "))
          e4=float(input("Above 200KWH: "));print("Altered rates successfully updated")
          rateh(fa1,fa2,fa3,e1,e2,e3,e4);
         
       if(rc==2):
          print("Update the FC for industrial")
          f1=float(input("FC For 1st KW:"));f2=float(input("For every additional KW up to and inclusive of 50 KW:"))
          f3=float(input("For every additional KW above 50 KW:"))
          print("Update EC for industrial")
          er1=float(input("0 to 50KWH :"))
          er2=float(input("Above 50KWH:"));print("Altered rates successfully updated")
          ratei(f1,f2,f3,er1,er2);
             
if(k==2):
      main(2);