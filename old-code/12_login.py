# Python Programme Number 12
# Pseudo Login prompt: Demonstration of compound conditions
# Programmer: Mukul Dharwadkar
# Date: 24 February 2006

print "\t\tRestricted Access"
print "\t\tMembers Only\n"

security = 0
username = ""

while not username:
    username = raw_input("Username: ")

password = ""
while not password:
    password = raw_input("Password: ")

if username == "mukul_d" and password == "latihs":
    print "Welcome Back, Mukul"
    security = 5
elif username == "sheetalp3" and password == "sumo2004":
    print "Welcome Back, Shital"
    security = 3
elif username == "guest" or password == "guest":
    print "Welcome, Guest.\n Enjoy your visit"
    security = 1
else:
    print "Access Denied. Your username and / or password is incorrect.\n Please try again."

    
