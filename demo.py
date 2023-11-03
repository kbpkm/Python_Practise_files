# Ask student details
name = input("Hey, Please Enter your Name: ").strip().title()
print(f"Hi, {name.title()}!")

# removing white spaces from str and capitalize name
text=("   Welcome " +name).strip().title()
print(text)

# Ask student if they submitted their previous assignment
check = input("Did you submit your previous assignment, " + name + "? ")

print("Good job, " + name + "!")

# Ask students for their goals for the next 3 days
task_1 = input("Write about the task you need to accomplish today: ")
print("Great!")

task_2 = input("What is the next task you need to do: ")
print("Fabulous!")

task_3 = input("Another task you need to accomplish: ")
print("Don't mess up these goals, okay!")

# Print the above statements in a proper way
print("Name:", name)
print("Previous assignment submission:", check)
print("Task 1:", task_1)
print("Task 2:", task_2)
print("Task 3:", task_3)
