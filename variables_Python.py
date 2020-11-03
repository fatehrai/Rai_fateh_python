# This is a comment
print("This is my first Python script!")

#variables are placeholders with dynamic values - > things that can change
#they get stored in memory and referenced later
name = "Fateh"
age = "old"
eyecolor = "blue"
haircolor = "red"

#print is a built-in python command that outputs whatever is in the round brackets
print("Name is currently" + name)

#input is another built-in Python 'thing' - it waits with a flashng cursor until you type something and hit enter
name = input("What is YOUR name?")
age = 22

#another request for output - str is a data type {text} - we're converting a number to text with this command
print("Your name is now: " + name + "and your age is " + str(age))


counter = 0
# set a condition and run a loop until that condition is set - this is a very common convention
while (counter < 8):
	counter += 1 
	print("counter is now at:" + str(counter))

print("counter is greater than 8, our loop is done")

