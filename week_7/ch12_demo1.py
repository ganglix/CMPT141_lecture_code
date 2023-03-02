# Read in the file data to create dictionary extensions that
# maps extension numbers to employees

# open
# absolute path
# path
# f = open(path, "r")

# relative path


# read and create the dictionary

# close

























#--------- alternative solution----------------
# # open
# # absolute path
# # path = "/Users/gangli/Library/CloudStorage/OneDrive-UniversityofSaskatchewan/CMPT141_big_folder/CMPT141_lecture_code/week_7/ext_directory_data.txt"
# # f = open(path, "r")
#
# # relative path
# f = open("../week_7/ext_directory_data.txt", "r")
# # f = open("./subfolder/scientists_data.txt")
#
# # read and create the dictionary
# phoneBook = {}
# for line in f:
#     line = line.rstrip().split(",")   #\n
#     phoneBook[int(line[0])] = line[1]
#
# # close
# f.close()
# print(phoneBook)