# Python Programme Number 6
# Password programme
# Programmer: Mukul Dharwadkar
# Date: 22 February 2006

print """\t\tWelcome to Dharwadkar Corporation.
\t Access to these systems is restricted and monitored
\tIf you are not authorized to access, please shutdown now
      """

password = raw_input("Please enter your password: ")

if password == "taln@T2004":
    print "Access Granted"
else:
    print "Access Denied"
    print "\nYou have attempted breach and it will be reported and investigated!!!"
#raw_input ("\n\nPress Enter to exit")
