val=int(input("enetr a number"))
s=str(val)
if s==s[::-1]:
    print("palidrome")
else :
    print("not palindrome")

for i in range(10):
    if s.count(str(i))> 0:
        print(str(i),"appears",s.count(str(i)),"times")