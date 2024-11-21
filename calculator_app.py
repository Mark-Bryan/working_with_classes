from tkinter import*
from tkinter import messagebox

# Creating Functions to assign to each button for proper functionability
def addition():
    num1 = int(first_numberEntry.get())
    num2 = int(second_numberEntry.get())
    result = num1 + num2
    result_label.configure(text=f"Result is: {result}")
    
# In the piece of code above and subsequently below, I used .configure method which is used to update or modify any frame. It could also be used for modify information like text without necessarily needing to recreate the frame

def subtraction(): 
    num1 = int(first_numberEntry.get())
    num2 = int(second_numberEntry.get())
    result = num1 - num2
    result_label.configure(text=f"Result is: {result}")


def multiplication():
    num1 = int(first_numberEntry.get())
    num2 = int(second_numberEntry.get())
    result = num1 * num2
    result_label.configure(text=f"Result is: {result}")

def division():
    num1 = int(first_numberEntry.get())
    num2 = int(second_numberEntry.get())
# Using branching statements to check that a number is not divisible by zero
    if num2 == 0:
        messagebox.showerror('Mathematical Error', 'Number cannot be disible by zero')
    else:
        result = num1 / num2
        result_label.configure(text=f"Result is: {result}")



mainWindow = Tk()
mainWindow.title("Calculator Application")

instructions = Label(mainWindow, text="Complete the following tasks")
instructions.pack(padx=20, pady=10)

#Creating a frame for the first number and packing it
first_numberFrame = Frame(mainWindow)
first_numberlabel = Label(first_numberFrame, text="Number 1")
first_numberEntry = Entry(first_numberFrame)

first_numberEntry.pack(side=RIGHT)
first_numberlabel.pack(side=LEFT)
first_numberFrame.pack(padx=20, pady=10)

# Creating a frame for the second number and packing it
second_numberFrame = Frame(mainWindow)
second_numberlabel = Label(second_numberFrame, text="Number 2")
second_numberEntry = Entry(second_numberFrame)

second_numberEntry.pack(side=RIGHT)
second_numberlabel.pack(side=LEFT)
second_numberFrame.pack(padx=20, pady=10)

# Creating a frame to group the action buttons
actionsFrame = Frame(mainWindow)

additionButton =  Button(mainWindow, text="Add", command=addition)
additionButton.pack(padx=10, pady=10)

subtractionButton = Button(mainWindow, text="Subtract", command=subtraction)
subtractionButton.pack(padx=10, pady=10)

multiplcationButton = Button(mainWindow, text="Multiply", command=multiplication)
multiplcationButton.pack(padx=10, pady=10)

divisionButton = Button(mainWindow, text="Divide", command=division)
divisionButton.pack(padx=10, pady=10)
actionsFrame.pack(padx=10, pady=10)

result_label = Label(mainWindow, text='Result is ')
result_label.pack(padx=10, pady=10)

mainWindow.mainloop()