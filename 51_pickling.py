# Python Programme Number 51
# Complex data storage: Demonstrates pickling (preserving) and shelving
# (storing & randomly accessing) data
# Programmer: Mukul Dharwadkar
# Date: 14 April 2006

import cPickle, shelve

print "Pickling Lists."
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]
pickle_file = open("/home/mukul/src/python/pickles.dat", "w")
cPickle.dump(variety, pickle_file, 1)
cPickle.dump(shape, pickle_file, 1)
cPickle.dump(brand, pickle_file, 1)
pickle_file.close()

print "\nUnpickling lists."
pickle_file = open("/home/mukul/src/python/pickles.dat", "r")
variety = cPickle.load(pickle_file)
shape = cPickle.load(pickle_file)
brand = cPickle.load(pickle_file)

# Testing that the process worked...
print variety, "\n", shape, "\n", brand
pickle_file.close()

# Shelving...
print "\nShelving lists."
pickles = shelve.open("pickles2.dat")

# Add lists to shelf
pickles["variety"] = ["sweet", "hot", "dill"]
pickles["shape"] = ["whole", "spear", "chip"]
pickles["brand"] = ["Claussen", "Heinz", "Vlassic"]

# Ensure that data is written
pickles.sync()

# Retrieving shelved values...
print "\nRetrieving the lists from a shelved file:"
for key in pickles.keys():
    print key, "-", pickles[key]

pickles.close()

raw_input("Press enter to exit.")
