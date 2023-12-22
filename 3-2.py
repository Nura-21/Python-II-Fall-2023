import tkinter as tk


def scan():
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    print(start_date)
    print(end_date)


root = tk.Tk()
root.title('3')
root.geometry('500x500')

top_label = tk.Label(root, text='Bookins scan', font=('Helvetica', 16))
top_label.pack(pady=40)

center_frame = tk.Frame(root)
center_frame.pack()

start_date_label = tk.Label(center_frame, text='Start date')
start_date_label.grid(row=0, column=0)
start_date_entry = tk.Entry(center_frame)
start_date_entry.grid(row=0, column=1)

end_date_label = tk.Label(center_frame, text='End date')
end_date_label.grid(row=1, column=0)
end_date_entry = tk.Entry(center_frame)
end_date_entry.grid(row=1, column=1)

scan_button = tk.Button(root, text='Scan', command=scan)
scan_button.pack()

radio_frame = tk.Frame(root)    
radio_frame.pack()

selected_option_var = tk.StringVar(value='Username')

username_radio = tk.Radiobutton(
    radio_frame, text="Username", variable=selected_option_var, value="Username")
username_radio.grid(row=0, column=0)

password_radio = tk.Radiobutton(
    radio_frame, text="Password", variable=selected_option_var, value="Password")
password_radio.grid(row=0, column=1)

root.mainloop()
