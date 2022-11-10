def computepay(h,r):
    if h<40:
        p=h*r
    else:
        p=40*r+(h-40)*r*1.5
    return p
#
while 1:
    hrs=input("Enter Hours: ")
    try:
        h=float(hrs)
        break
    except:
        print("Enter a valid number")
while 1:
    rate=input("Enter Rate: ")
    try:
        r=float(rate)
        break
    except:
        print("Enter a valid number")
#
pay=computepay(h,r)
print("Pay",pay)
