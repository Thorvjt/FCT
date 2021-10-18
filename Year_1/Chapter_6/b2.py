num=0
max_num=0
min_num=10000000
tot=0
while True:
    sval=input("Enter a number: ")
    if sval=="Done":
        break
    try:
        sval=float(sval)
    except:
        print("bad data")
        continue
    if max_num<sval:
        max_num=sval
    if min_num>sval:
        min_num=sval
    num=num+1
    tot=tot+sval
print(tot,num,max_num,min_num)