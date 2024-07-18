import tkinter as tk
from tkinter import* 
count = 0
check_btn = True
clear_button = None
list_data = []




def addlist():
    global check_btn
    if check_btn == True:
        usernumber = int(userinput_number.get())
        clear_entries()
        for i in range(usernumber):
            userinput_x = tk.Entry(second_frame)
            userinput_x.pack(pady=2)  
            list_data.append(userinput_x)
        cleardata()
        check_btn = False
    

def cleardata():
    global clear_button
    clear_button = tk.Button(root, text="Clear Number", command=clear_entries ,bg="red" ,fg="white")
    clear_button.pack(side="bottom" ,pady=10)
   

def x_barcal():
    x_bar = 0
    usernumber = int(userinput_number.get())  # Convert user input to an integer
    for j in range(usernumber):
        x_bar += int(list_data[j].get())  # Retrieve the value using get() method
        j += 1
    result_label.config(text="x̄ = %f Σx = %d" %(x_bar / usernumber,x_bar))
    

def clear_entries():
    global check_btn,clear_button
    for entry in list_data:
        entry.destroy()  
    list_data.clear()  
    check_btn = True
    if clear_button:
        clear_button.destroy()
    result_label.config(text="") 


def on_entry_click(event):
    if userinput_number.get() == "Enter N":
        userinput_number.delete(0, "end")

        
root = tk.Tk()
root.geometry('400x600')
root.option_add("*Font", "consolas 20")

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)


my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)


my_scrollbar = tk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))


second_frame =Frame(my_canvas)


my_canvas.create_window((0,0), window=second_frame, anchor="nw")




userinput_number_label = tk.Label(second_frame, text="Xbar Cal by tartah")
userinput_number_label.pack(padx=50)

userinput_number = tk.Entry(second_frame, textvariable=tk.StringVar())
userinput_number.insert(0, "Enter N")
userinput_number.bind("<FocusIn>", on_entry_click)
userinput_number.pack(pady=10)



calculate_button = tk.Button(second_frame, text="Enter", command=addlist )  
calculate_button.pack() 


calculate_button = tk.Button(root, text="Calculate", command=x_barcal,bg="green",fg="white") 
calculate_button.pack(side="bottom", pady=20)   


result_label = tk.Label(second_frame, text="")
result_label.pack(side="bottom")




root.mainloop()

