# Topic(s): Writing Files
# DEMO
# records of books to write to file
books = [
    {"title": "The Cat in the Hat", "author": "Dr. Seuss",
     "year_published": 1605},
    {"title": "The Cat in the Hat Comes Back", "author": "Dr. Seuss",
     "year_published": 1859},
    {"title": "The Adventures of Tom Sawyer", "author": "Mark Twain",
     "year_published": 1876},
    {"title": "The Prince and the Pauper", "author": "Mark Twain",
     "year_published": 1881},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee",
     "year_published": 1960},
    {"title": "Animal Farm", "author": "George Orwell",
     "year_published": 1945},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger",
     "year_published": 1951},
    {"title": "Pride and Prejudice", "author": "Jane Austen",
     "year_published": 1813}
]


# open for writing

# for each book , write its title , author , year published in that order

# done writing , close file






















#--------------------- alternative way -----------------

# # open for writing
# f = open("my_books.txt", 'w')
# # for each book , write its title , author , year published in that order
# for book in books:
#     # f.write(book["title"] + "," + book['author'] + "," + str(book['year_published']))
#     line_to_write = ','.join([book["title"], book['author'],str(book['year_published'])])
#     f.write((line_to_write))
#     # f.write('\n')
#
# # done writing , close file
# f.close()
