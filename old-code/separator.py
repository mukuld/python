fl = "sortedsonglist.txt"
def open_to_read(inp_file):
    f = open(fl, "r+")
    lines = f.readlines()
    f.close()
    return lines

def open_to_write(inp_file, inp_lines):
    f = open(fl, "r+")
    #lines = "".join(inp_lines)
    f.writelines(inp_lines)
    f.close()
    #return lines

lines1 = open_to_read(fl)

lines1.insert(0, "A \n")

open_to_write(fl, lines1)

#open_to_read(fl)
a_list = []

for i in range(len(lines1) - 1): # Not using the modern "FOR" loop here as it gives an IndexError
    #TODO: Need to handle the IndexError gracefully.
    if lines1[i][0] != lines1[i+1][0]:
        list = [(lines1[i+1][0])]
        for item in list:
            a_list.append(item)
 
for i in range(len(lines1)+len(a_list) - 1):
    if lines1[i][0] != lines1[i+1][0]:
        lines1.insert(i + 1, a_list[0] + "\n")
        a_list.pop(0)

open_to_write(fl, lines1)