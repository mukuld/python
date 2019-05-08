# Useless Trivia
#
# Gets personal information from the user and then
# prints true, but useless information about him or her
#
# Michael Dawson - 1/14/03

name = raw_input("Hi.  What's your name? ")

age = raw_input("And how old are you? ")
age = int(age)

weight = raw_input("Okay, last question.  How many pounds do you weigh? ")
weight = int(weight)

print "\nIf poet ee cummings were to email you, he'd address you as", name.lower()

ee_mad = name.upper()
print "But if ee were mad, he'd call you", ee_mad

dog_years = age / 7
print "\nDid you know that you're just", dog_years, "in dog years?"

seconds = age * 365 * 24 * 60 * 60
print "But you're also over", seconds, "seconds old."

called = name * 5
print "\nIf a small child were trying to get your attention, " \
      "your name would become:"
print called

moon_weight = weight / 6.0
print "\nDid you know that on the moon you would weigh only", moon_weight, "pounds?" 

sun_weight = weight * 27.1
print "But on the sun, you'd weigh", sun_weight, "(but, ah... not for long)."

raw_input("\n\nPress the enter key to exit.")
