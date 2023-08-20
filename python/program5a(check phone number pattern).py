import re


def isphonenumber(numStr):
    if len(numStr)!=12:
        return False
    for i in range(len(numStr)):
      if i==3 or i==7 :
        if numStr[i]!="-":
           return False
      else :
         if numStr[i].isdigit()==False:
            return False
    return True
def checkphonenumber(numStr):
   phone_number_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
   if phone_number_pattern.match(numStr):
      return True
   else :
      return False
   
ph_num=input (" enter a  phome number:")
print("without using regular expression :")
if isphonenumber(ph_num):
   print("valid phone number")
else:
   print("invalid phone number")

print("with using regual expression:")
if checkphonenumber(ph_num):
   print("valid phone number")
else:
   print("invald phone number")

