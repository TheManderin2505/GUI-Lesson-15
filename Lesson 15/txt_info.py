import tkinter as tk
# Create the main window
root = tk.Tk()
root.title("Dropdown Example")
# Define a StringVar to hold the selected option
selected_option = tk.StringVar(root)
# Set an initial value
selected_option.set("Option 1")
# Create a list of options
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Create the OptionMenu widget
dropdown = tk.OptionMenu(root, selected_option, *options)

dropdown.pack(pady=20)
# Function to display the selected value

def show_selection():
    print("Selected option:", selected_option.get())
    
# Add a button to trigger the display
button = tk.Button(root, text="Show Selection", command=show_selection)
button.pack()
# Run the Tkinter event loop
root.mainloop()