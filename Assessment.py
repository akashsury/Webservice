#Input list has to be given like this none1@gmail.com,none2@gmail.com
def webservice(Email_list):
  Unique = []
  for i in range(0,len(Email_list)):
    at = Email_list[i].index("@")  
    if "+" in Email_list[i]:
      plus = Email_list[i].index("+")
      Email_list[i] = Email_list[i][:plus]+Email_list[i][at:]
      at = Email_list[i].index("@")  
    temp = Email_list[i][:at].replace(".","")
    Email_list[i] = temp+Email_list[i][at:]
    if Email_list[i] not in Unique:
      Unique.append(Email_list[i])
  print(Unique)  
  return(len(Unique))  
Emails = input("Enter a list of emails: ")
Email_list = Emails.split(",")
Result = webservice(Email_list)
print("Number of email addresses:",Result)
