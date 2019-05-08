# Pickle It
# Demonstrates pickling and shelving data
# Michael Dawson 5/1/03

import cPickle, shelve

print "Pickling lists."
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]
f = open("pickles1.dat", "w")
cPickle.dump(variety, f)
cPickle.dump(shape, f)
cPickle.dump(brand, f)
f.close()

print "\nUnpickling lists."
f = open("pickles1.dat", "r")
variety = cPickle.load(f)
shape = cPickle.load(f)
brand = cPickle.load(f)
print variety, "\n", shape, "\n", brand
f.close()

print "\nShelving lists."
pickles = shelve.open("pickles2.dat")
pickles["variety"] = ["sweet", "hot", "dill"]
pickles ["shape"] = ["whole", "spear", "chip"]
pickles["brand"] = ["Claussen", "Heinz", "Vlassic"]
pickles.sync()    # make sure data is written

print "\nRetrieving the lists from a shelved file:"
for key in pickles.keys():
    print key, "-", pickles[key]
pickles.close()

raw_input("\n\nPress the enter key to exit.")
