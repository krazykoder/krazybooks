protein = "vlspadktnv" 
print(str(protein.find('p'))) 
print(str(protein.find('kt'))) 
print(str(protein.find('w')))

protein = "vlspadktnv"

# print positions three to five
print(protein[3:5])

# positions start at zero, not one
print(protein[0:6])

# if we miss out the last number, it goes to the end of the string
print(protein[2:])



