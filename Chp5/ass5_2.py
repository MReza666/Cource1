largest = None
smallest = None
while True:
    snum = input("Enter a number: ")
    if snum == "done":
        break
    try:
        num = int(snum)
    except:
        print("Invalid input")
        continue
    #
    if largest is None:
        largest = num
        smallest = num
    elif largest<num:
        largest = num
    elif smallest>num:
        smallest = num
#
print("Maximum is",largest)
print("Minimum is",smallest)
