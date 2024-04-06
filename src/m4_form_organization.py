import tkinter as tk
###############################################################################
# TODO: 1. (5 pts)
#
#   For this _todo_, copy your code from your fillable form from Session 18 and
#   paste it below.
#
#   Now, use the geometry managers we have learned about and reorganize/
#   reformat your fillable form. You must use more than just the pack() method,
#   but you can still use it if it is what you need in a certain spot.
#
#   You may need to add more frames and such to move things around effectively.
#
#   Feel free to be creative on how you want your form to look.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

window = tk.Tk()
window.title("Form")

frameA = tk.Frame()
frameA.place(x=50, y=0)
frameB = tk.Frame()
frameB.place(x=50, y=75)
frameC = tk.Frame()
frameC.place(x=50, y=150)
frameD = tk.Frame()
frameD.place(x=50, y=225)
frameE = tk.Frame()
frameE.place(x=50, y=300)
frameF = tk.Frame()
frameF.place(x=50, y=375)
frameG = tk.Frame()
frameG.place(x=50, y=450)
frameH = tk.Frame()
frameH.place(x=50, y=525)

name_label = tk.Label(master=frameA, text="Name", height=2, bg="#808080", width=17)
name_label.pack()
name_entry = tk.Entry(master=frameA)
name_entry.pack()

address1_label = tk.Label(master=frameB, text="Address Line 1", height=2, bg="#808080", width=17)
address1_label.pack()
address1_entry = tk.Entry(master=frameB)
address1_entry.pack()

address2_label = tk.Label(master=frameC, text="Address Line 2", height=2, bg="#808080", width=17)
address2_label.pack()
address2_entry = tk.Entry(master=frameC)
address2_entry.pack()

city_label = tk.Label(master=frameD, text="City", height=2, bg="#808080", width=17)
city_label.pack()
city_entry = tk.Entry(master=frameD)
city_entry.pack()

state_label = tk.Label(master=frameE, text="State", height=2, bg="#808080", width=17)
state_label.pack()
state_entry = tk.Entry(master=frameE)
state_entry.pack()

zip_label = tk.Label(master=frameF, text="Zip Code", height=2, bg="#808080", width=17)
zip_label.pack()
zip_entry = tk.Entry(master=frameF)
zip_entry.pack()

phone_label = tk.Label(master=frameG, text="Phone Number", height=2, bg="#808080", width=17)
phone_label.pack()
phone_entry = tk.Entry(master=frameG)
phone_entry.pack()

email_label = tk.Label(master=frameH, text="Email Address", height=2, bg="#808080", width=17)
email_label.pack()
email_entry = tk.Entry(master=frameH)
email_entry.pack()

button = tk.Button(text="Submit", width=20, height=9)
button.place(x=300, y=200)

window.mainloop()