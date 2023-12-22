import tkinter as tk

root = tk.Tk()
root.title('3')
root.geometry('350x350')

top_center_frame = tk.Frame(root)
top_center_frame.pack()

top_left_frame = tk.Frame(top_center_frame, width=50, height=70)
top_left_frame.grid(row=0, column=0)

contact_list_label = tk.Label(top_left_frame, text='Contact List')
contact_list_label.grid(row=0, column=0, pady=2)

contact_list_text = tk.Entry(top_left_frame)
contact_list_text.grid(row=1, column=0, pady=5, ipady=70)

contact_list_button = tk.Button(top_left_frame, text='Display Contact')
contact_list_button.grid(row=2, column=0)

top_right_frame = tk.Frame(top_center_frame, width=50, height=70)
top_right_frame.grid(row=0, column=1)

new_contact_label = tk.Label(top_right_frame, text='New contact')
new_contact_label.grid(row=0, column=0)

new_contact_frame = tk.Frame(top_right_frame)
new_contact_frame.grid(row=1, column=0)

first_name_label = tk.Label(new_contact_frame, text='First name:')
last_name_label = tk.Label(new_contact_frame, text='Last name:')
phone_label = tk.Label(new_contact_frame, text='Phone #:')

first_name_label.grid(row=0, column=0)
last_name_label.grid(row=1, column=0)
phone_label.grid(row=2, column=0)

first_name_entry = tk.Entry(new_contact_frame)
first_name_entry.grid(row=0, column=1)
last_name_entry = tk.Entry(new_contact_frame)
last_name_entry.grid(row=1, column=1)
phone_entry = tk.Entry(new_contact_frame)
phone_entry.grid(row=2, column=1)

is_friend_chekcbox = tk.Checkbutton(new_contact_frame)
is_friend_chekcbox.grid(row=3, column=0, columnspan=5)
is_friend_label = tk.Label(new_contact_frame, text='Friend')
is_friend_label.grid(row=3, column=1)

add_contact_button = tk.Button(new_contact_frame, text='Add contact')
add_contact_button.grid(row=4, column=1, padx=tuple([50, 0]))

mid_frame = tk.Frame(root, width=100, height=20)
mid_frame.pack()

last_name_new_label = tk.Label(mid_frame, text='Last name: ', pady=40)
last_name_new_label.grid(row=0, column=0)

last_name_new_entry = tk.Entry(mid_frame, width=20)
last_name_new_entry.grid(row=0, column=1)

result_text = tk.Label(mid_frame, text='Result: Last, First, Phone', width=20)
result_text.grid(row=0, column=2,)

bottom_frame = tk.Frame(root, width=100)
bottom_frame.pack()

search_button = tk.Button(bottom_frame, text='Search', width=4)
search_button.pack(side='left')

root.mainloop()
