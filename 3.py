import tkinter as tk


def scan():
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    username_checked = username_var.get()
    password_checked = password_var.get()

    # You can add your scanning logic here
    print("Start Date:", start_date)
    print("End Date:", end_date)
    print("Username Checked:", username_checked)
    print("Password Checked:", password_checked)


root = tk.Tk()
root.title("Bookings Scan")
root.geometry('500x500')

# Top Center Text
top_label = tk.Label(root, text="Bookings scan", font=("Helvetica", 16))
top_label.pack(pady=40)

# Bottom Inputs and Scan Button
start_date_label = tk.Label(root, text="Enter the start date")
start_date_label.pack()
start_date_entry = tk.Entry(root)
start_date_entry.pack()

end_date_label = tk.Label(root, text="Enter the end date")
end_date_label.pack()
end_date_entry = tk.Entry(root)
end_date_entry.pack()

scan_button = tk.Button(root, text="Scan", command=scan)
scan_button.pack()

# Bottom Center Checkboxes
checkbox_frame = tk.Frame(root)
checkbox_frame.pack()

username_var = tk.IntVar()
password_var = tk.IntVar()

username_checkbox = tk.Checkbutton(
    checkbox_frame, text="Username", variable=username_var)
username_checkbox.grid(row=0, column=0)

password_checkbox = tk.Checkbutton(
    checkbox_frame, text="Password", variable=password_var)
password_checkbox.grid(row=0, column=1)

root.mainloop()
