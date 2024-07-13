import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Entry fields for numbers
        self.label_num1 = tk.Label(root, text="Enter first number:")
        self.label_num1.grid(row=0, column=0, padx=10, pady=10)
        self.entry_num1 = tk.Entry(root, width=20)
        self.entry_num1.grid(row=0, column=1, padx=10, pady=10)

        self.label_num2 = tk.Label(root, text="Enter second number:")
        self.label_num2.grid(row=1, column=0, padx=10, pady=10)
        self.entry_num2 = tk.Entry(root, width=20)
        self.entry_num2.grid(row=1, column=1, padx=10, pady=10)

        # Dropdown menu for operations
        self.operations = ['Addition', 'Subtraction', 'Multiplication', 'Division']
        self.selected_operation = tk.StringVar()
        self.selected_operation.set(self.operations[0])  # default operation

        self.operation_label = tk.Label(root, text="Choose operation:")
        self.operation_label.grid(row=2, column=0, padx=10, pady=10)
        self.operation_menu = tk.OptionMenu(root, self.selected_operation, *self.operations)
        self.operation_menu.grid(row=2, column=1, padx=10, pady=10)

        # Calculate button
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def calculate(self):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            operation = self.selected_operation.get()

            if operation == 'Addition':
                result = num1 + num2
            elif operation == 'Subtraction':
                result = num1 - num2
            elif operation == 'Multiplication':
                result = num1 * num2
            elif operation == 'Division':
                if num2 == 0:
                    messagebox.showerror("Error", "Division by zero is not allowed")
                    return
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Invalid operation selected")
                return

            messagebox.showinfo("Result", f"Result of {operation}: {result}")

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
