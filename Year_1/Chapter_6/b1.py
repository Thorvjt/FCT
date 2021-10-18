num=0
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
    num=num+1
    tot=tot+sval
print(tot,num,tot/num)