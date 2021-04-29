#!/usr/bin/env python3
import csv

f = open("comics.txt", "r")
authors_list = []

for row in csv.reader(f, delimiter=';'):
        authors = row[-1]
        # There sould be several comma separated names, so split them
        new_authors = authors.split(",") 
        #print("Author: " + author)
        for author_name in new_authors:
            if author_name.strip(" '") not in authors_list:
                authors_list.append(author_name.strip(" '"))

# Now print the unique list of authors
authors_list.sort()
for x in authors_list:
    print(x)

