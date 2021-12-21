#Read all of the content of the file in one variable.
file = open("student_names.txt", "r")
student = file.read()
print(student)
file. close()
#Write a list of random names to your file.
file = open("student_names.txt", "a+")
#file.write("\noussama \nimad \nreda \nlouai")
file. close()
#Read the first n lines of the file.
file = open("student_names.txt", "r")
lines = file.readlines()
n = int(input("Enter the nb of the first lines you want read: "))
print(lines[:n])
#Read the last n lines of the file.
m = int(input("Enter the nb of the last lines you want read: "))
print(lines[-m:])
#Check if the name x is in the file
x = input("Enter a name: ")
if x in file.read():
    print("word found")
else:
    print("word doesn't exist")