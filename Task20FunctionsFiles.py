
from sys import argv

# script, input_file = argv

# def print_all(f):
#     print(f.read())

# def rewind(f):
#     f.seek(2)
#     print("It worked?")

# def print_a_line(line_count, f):
#     print(line_count, f.readline())

# current_file = open(input_file)

# print("First let's print the whole file: \n")

# print_all(current_file)#

# print("Now let's rewind, kind of like a tape. ")

# rewind(current_file)

# print("Let's print three lines:")

# current_line = 1
# print_a_line(current_line, current_file)

# current_line += 1
# print_a_line(current_line, current_file)

# current_line += 1
# print_a_line(current_line, current_file)
# # #Solo


# # current_file.seek(2)
# # print(current_file.readline())

#s1
# print("----------------------------------------------------------------")


script, input_file = argv

print("Script:", script, "\nFile Name:", input_file)

def print_all(f):
    print(f.read())

def tell(f):
    print("Number:",f.tell())
    print("??Worked??")

def rewind(f):
    f.seek(26)
    print("??reqind???")

def tell_t(f):
    print("Number:",f.tell())
    print("??Worked??")

current_file = open(input_file)
print_all(current_file)
print("----------------------------------------------------------------")
tell(current_file)
rewind(current_file)
tell_t(current_file)
print_all(current_file)


