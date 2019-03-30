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


# ----------------------------------------------------------------------------------- #
# Read Sudoku file and load to list 

# Open the file with read only permit
f = open('sudoku_data1.txt', "r")
# use readlines to read all lines in the file
# The variable "lines" is a list containing all lines in the file
lines = f.readlines()

mylist = []

# do all processing
for line in lines :
    thesudoku = line.replace('\n','')
    thesudoku = thesudoku.replace('\"', '')
    thesudoku = thesudoku.replace(',', '')
#     mylist.append(temp)
# print (mylist)

# for item in mylist : 
#     thesudoku = item
    thesudoku = thesudoku.replace('e',"00")
    thesudoku = thesudoku.replace('d',"000")
    thesudoku = thesudoku.replace('c',"0000")
    thesudoku = thesudoku.replace('b',"00000")
    thesudoku = thesudoku.replace('a',"000000")
    thesudoku = " ".join(thesudoku)
    # print(thesudoku)
    mylist.append(thesudoku)
# print( mylist)
# close the file after reading the lines.
f.close()

# open file to write 
f = open('sudoku_data_processed.txt', "w")
# append newline to each list item and write
f.write('\n'.join(mylist))
f.close()

# ----------------------------------------------------------------------------------- #
