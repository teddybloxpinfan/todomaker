import os

print("""
WHAT DO YOU NEED TO DO TODAY?
""")

main = input()

#write to file
with open("todo.txt", "w") as todo:
	todo.write(main)
