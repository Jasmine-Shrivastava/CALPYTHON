
from tkinter import *
expressionforOperation = ""


# Function to update expression
# in the text entry box
def press(num):
	# point out the global expression variable
	global expressionforOperation
	expressionforOperation = expressionforOperation + str(num)
   # update the expression by using set method
	equation.set(expressionforOperation)


# Function to evaluate the final expression
def equalpress():
	
	try:

		global expressionforOperation

		# eval function evaluate the expression
		# and str function convert the result
		# into string
		total = str(eval(expressionforOperation))

		equation.set(total)

		
		expressionforOperation = ""

	#if there is an error
	except:

		equation.set(" error ")
		expressionforOperation = ""


#to clear the contents
def clear():
	global expressionforOperation
	expressionforOperation = ""
	equation.set("")


# Driver code
if __name__ == "__main__":
	
	root = Tk()

	# background colour of GUI window
	root.configure(background="purple")

	# set the title of GUI window
	root.title("Basic Calculator")

	# set the configuration of GUI window
	root.geometry("270x150")

	equation = StringVar()

	# create the text entry box for
	# showing the expression .
	expression_field = Entry(root, textvariable=equation)
    #grid method
	expression_field.grid(columnspan=4, ipadx=70)

	#buttons created 
	#function will be executed when user presses any button
	button1 = Button(root, text=' 1 ', fg='black', bg='red',
					command=lambda: press(1), height=1, width=7)
	button1.grid(row=2, column=0)

	button2 = Button(root, text=' 2 ', fg='black', bg='red',
					command=lambda: press(2), height=1, width=7)
	button2.grid(row=2, column=1)

	button3 = Button(root, text=' 3 ', fg='black', bg='red',
					command=lambda: press(3), height=1, width=7)
	button3.grid(row=2, column=2)

	button4 = Button(root, text=' 4 ', fg='black', bg='red',
					command=lambda: press(4), height=1, width=7)
	button4.grid(row=3, column=0)

	button5 = Button(root, text=' 5 ', fg='black', bg='red',
					command=lambda: press(5), height=1, width=7)
	button5.grid(row=3, column=1)

	button6 = Button(root, text=' 6 ', fg='black', bg='red',
					command=lambda: press(6), height=1, width=7)
	button6.grid(row=3, column=2)

	button7 = Button(root, text=' 7 ', fg='black', bg='red',
					command=lambda: press(7), height=1, width=7)
	button7.grid(row=4, column=0)

	button8 = Button(root, text=' 8 ', fg='black', bg='red',
					command=lambda: press(8), height=1, width=7)
	button8.grid(row=4, column=1)

	button9 = Button(root, text=' 9 ', fg='black', bg='red',
					command=lambda: press(9), height=1, width=7)
	button9.grid(row=4, column=2)

	button0 = Button(root, text=' 0 ', fg='black', bg='red',
					command=lambda: press(0), height=1, width=7)
	button0.grid(row=5, column=0)

	plus = Button(root, text=' + ', fg='black', bg='red',
				command=lambda: press("+"), height=1, width=7)
	plus.grid(row=2, column=3)

	minus = Button(root, text=' - ', fg='black', bg='red',
				command=lambda: press("-"), height=1, width=7)
	minus.grid(row=3, column=3)

	multiply = Button(root, text=' * ', fg='black', bg='red',
					command=lambda: press("*"), height=1, width=7)
	multiply.grid(row=4, column=3)

	divide = Button(root, text=' / ', fg='black', bg='red',
					command=lambda: press("/"), height=1, width=7)
	divide.grid(row=5, column=3)

	equalSym = Button(root, text=' = ', fg='black', bg='red',
				command=equalpress, height=1, width=7)
	equalSym.grid(row=5, column=2)

	clear = Button(root, text='Clear', fg='black', bg='red',
				command=clear, height=1, width=7)
	clear.grid(row=5, column='1')

	Decimal= Button(root, text='.', fg='black', bg='red',
					command=lambda: press('.'), height=1, width=7)
	Decimal.grid(row=6, column=0)
	# start the GUI
	root.mainloop()
