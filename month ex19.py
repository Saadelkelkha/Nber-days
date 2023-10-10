m=int(input("type a month between 1 and 12 :"))
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12 :
    print("the number of days in this month is : 31") 
elif m==2 :
    print("the number of days in this month is : 28 or 29")
else :
    print("the number of days in this month is : 30")