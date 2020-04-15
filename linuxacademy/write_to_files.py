file_name = "recipes.txt"

try:
    myfile = open(file_name, "x")
    myfile.write("Puran Poli\n")
    myfile.close()
except FileExistsError as err:
    print(f"The {file_name} file already exists.")
except:
    print(f"Something went wrong. Unable to write to the  file")
else:
    print(f"Wrote to {file_name}")
finally:
    print(f"Execution Completed")
