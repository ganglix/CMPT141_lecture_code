# Read in the file data to create dictionary extensions that
# maps extension numbers to employees

# open
# absolute path: full directory

# relative path
path = "ext_directory_data.txt"  # by default, use current folder
# # current folder .
# "./ext_directory_data.txt"
# # parent folder ..
# "../week_7/ext_directory_data.txt"

# open
f = open(path, "r")   # r read
# read and create the dictionary
phoneBook = {}  # ext: name
for line in f:
    # clean the line and parse it # "\n" new line at the end of each line
    line = line.rstrip().split(',')
    ext = int(line[0])
    name = line[1]
    phoneBook[ext] = name
# close
f.close()

print(phoneBook)