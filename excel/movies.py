#!/usr/bin/env python3

## sudo apt install python3-pip

## python3 -m pip install pyexcel
## python3 -m pip install pyexcel-xls
import pyexcel as pyx

# Request data from user
def get_input():
    input_name = input("\nEnter the name of a movie director:  ")
    return input_name


# Load file into memory 
def load_file():
    global sheet1
    global sheet2
    global sheet3
    book=pyx.get_book(file_name='movies.xls')
    sheet1 = book["1900s"]
    sheet2 = book["2000s"]
    sheet3 = book["2010s"]
    sheet3.name_columns_by_row(0)
    print(sheet1[1])
    print(sheet2[1])
    print(sheet3[1])

# search for movies by given Director
def find_movies(director):
    global sheet3
    for row, name in sheet3.column["Director"]:
        if name.lower().strip() == director.lower():
            print(f"Found movie: {sheet3.column['Title', row]}")

def main():
    load_file()
    dir_name = get_input()
    find_movies(dir_name)

main()

