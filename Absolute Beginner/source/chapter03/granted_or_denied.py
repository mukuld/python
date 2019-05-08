# Granted or Denied
# Demonstrates the if-else structure
# Michael Dawson - 12/29/02

print "Welcome to System Security Inc."
print "-- where security is our middle name\n"

password = raw_input("Enter your password: ")

if password == "secret":
    print "Access Granted"
else:
    print "Access Denied"

raw_input("\n\nPress the enter key to exit.")
