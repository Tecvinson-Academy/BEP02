import tkinter as tk
from tkinter import ttk
import csv
import re
from tkinter import messagebox
import registration
import login as authenticate
import data


class Interface(tk.Frame):
    def __init__(self, root):
        self.pager = None
        self.current_page_index = 1
        self.pages = [self.page1, self.page2, self.page3, self.page4, self.page5, self.page6]
        self.colour1 = '#222448'
        self.colour2 = '#54527E'
        self.colour3 = 'WHITE'
        self.USER = None

        super().__init__(root, bg=self.colour1)

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        self.load_main_widgets()

    def logout(self):
        self.USER = None
        self.page2()
    def load_main_widgets(self):  # Load page components
        self.create_page_container()
        self.create_pager()
        self.pages[self.current_page_index]()  # Load first page

    def clear_frame(self, frame):
        for child in frame.winfo_children():
            child.destroy()

    def create_page_container(self):  # main container for the APP
        self.page_container = tk.Frame(
            self.main_frame,
            background=self.colour1,
        )

        self.page_container.columnconfigure(0, weight=1)
        self.page_container.rowconfigure(0, weight=0)
        self.page_container.rowconfigure(1, weight=1)
        self.page_container.grid(column=0, row=0, sticky=tk.NSEW)

    def create_pager(self):
        self.pager = tk.Frame(
            self.main_frame,  # Inside the Main Frame
            background=self.colour1,
            height=125,
            width=400
        )
        self.pager.columnconfigure(1, weight=1)
        self.pager.rowconfigure(0, weight=1)
        self.pager.grid(column=0, row=1, sticky=tk.NS)
        self.pager.grid_propagate(False)

        def change_page(button):
            self.clear_frame(self.page_container)

            # match button:
            #     case 'Previous':
            #         self.current_page_index -= 1
            #         self.pages[self.current_page_index]()
            #     case 'Next':
            #         self.current_page_index += 1
            #         self.pages[self.current_page_index]()
            #     case 'New_Order':
            #         self.current_page_index = 3
            #
            # if self.current_page_index == 0:
            #     prev_button.config(state=tk.DISABLED)
            # else:
            #     prev_button.config(state=tk.ACTIVE)
            #
            # if self.current_page_index == len(self.pages) - 1:
            #     next_button.config(state=tk.DISABLED)
            # else:
            #     next_button.config(state=tk.ACTIVE)

            self.page_number['text'] = f'{self.current_page_index + 1} / {len(self.pages)}'

        # Navigation Button
        # prev_button = tk.Button(
        #     self.pager,
        #     background=self.colour2,
        #     foreground=self.colour3,
        #     activebackground=self.colour2,
        #     activeforeground=self.colour3,
        #     disabledforeground='#3B3A56',
        #     highlightthickness=0,
        #     width=7,
        #     relief=tk.FLAT,
        #     font=('Arial', 18),
        #     cursor='hand1',
        #     text='Previous',
        #     state=tk.DISABLED,
        #     command=lambda button='Previous': change_page(button)
        # )
        # prev_button.grid(column=0, row=0)
        #
        # self.page_number = tk.Label(
        #     self.pager,
        #     background=self.colour1,
        #     foreground=self.colour3,
        #     font=('Arial', 18),
        #     text=f'{self.current_page_index + 1} / {len(self.pages)}'
        # )
        # self.page_number.grid(column=1, row=0)

        # next_button = tk.Button(
        #     self.pager,
        #     background=self.colour2,
        #     foreground=self.colour3,
        #     activebackground=self.colour2,
        #     activeforeground=self.colour3,
        #     disabledforeground='#3B3A56',
        #     highlightthickness=0,
        #     width=7,
        #     relief=tk.FLAT,
        #     font=('Arial', 18),
        #     cursor='hand1',
        #     text='Next',
        #     command=lambda button='Next': change_page(button)
        # )
        # next_button.grid(column=2, row=0)

    #  NAVIGATION TO CHANGE SCREENS FROM MAIN MENU

    def page1(self):
        def validate_email(email):
            # Check if the email format is valid
            return re.match(r"[^@]+@[^@]+\.[^@]+", email)

        def register_user():
            fname = name_texbox.get().strip()
            sname = sname_texbox.get().strip()
            email = email_texbox.get().strip()
            gender = gender_picker.get().strip()
            age = age_picker.get().strip()
            address = address_texbox.get().strip()
            password = password_textbox.get().strip()
            conf_password = conf_password_texbox.get().strip()

            if not validate_email(email):
                messagebox.showerror("Invalid Email", "Please enter a valid email address.")
                return

            if password != conf_password:
                messagebox.showerror("Password Error", "Passwords do not match!")
                return

            # Save user details to CSV
            with open('users.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([fname, sname, email, gender, age, address, password])

            # Clear all entries
            name_texbox.delete(0, tk.END)
            sname_texbox.delete(0, tk.END)
            email_texbox.delete(0, tk.END)
            gender_picker.set('')
            age_picker.set('')
            address_texbox.delete(0, tk.END)
            password_textbox.delete(0, tk.END)
            conf_password_texbox.delete(0, tk.END)

            messagebox.showinfo("Registration Successful", "User registered successfully!")

        title = tk.Label(
            self.page_container,
            background=self.colour1,
            foreground=self.colour3,
            height=2,
            font=('Arial', 26, 'bold'),
            text='User Registration'
        )
        title.grid(column=0, row=0)

        user_info_frame = tk.LabelFrame(
            self.page_container,
            text='User Information',
            pady=20,
            padx=20,
        )
        user_info_frame.grid(row=1, column=0, sticky='news')

        name_label = tk.Label(user_info_frame, text="First Name:")
        name_label.grid(row=0, column=0, sticky=tk.W)
        name_texbox = tk.Entry(user_info_frame, width=20)
        name_texbox.grid(row=0, column=1, sticky=tk.W)

        sname_label = tk.Label(user_info_frame, text="Surname:")
        sname_label.grid(row=0, column=2, sticky=tk.W)
        sname_texbox = tk.Entry(user_info_frame, width=28)
        sname_texbox.grid(row=0, column=3, sticky=tk.W)

        email_label = tk.Label(user_info_frame, text="Email:")
        email_label.grid(row=1, column=0, sticky=tk.W)
        email_texbox = tk.Entry(user_info_frame, width=58)
        email_texbox.grid(row=1, column=1, columnspan=3, sticky=tk.W)

        gender_label = tk.Label(user_info_frame, text="Gender:")
        gender_label.grid(row=2, column=0, sticky=tk.W)
        gender_picker = ttk.Combobox(user_info_frame, values=['Male', 'Female'])
        gender_picker.grid(row=2, column=1, sticky='w')

        age_label = tk.Label(user_info_frame, text="Age:")
        age_label.grid(row=2, column=2, sticky=tk.W)
        age_picker = ttk.Combobox(user_info_frame, values=['18-29', '30-45', 'Over 45'])
        age_picker.grid(row=2, column=3, sticky='w')

        address_label = tk.Label(user_info_frame, text="Address:")
        address_label.grid(row=3, column=0, sticky=tk.W)
        address_texbox = tk.Entry(user_info_frame, width=58)
        address_texbox.grid(row=3, column=1, columnspan=3)

        password_label = tk.Label(user_info_frame, text="Password:")
        password_label.grid(row=4, column=0, sticky=tk.W)
        password_textbox = tk.Entry(user_info_frame, width=58, show='*')
        password_textbox.grid(row=4, column=1, columnspan=3)

        conf_password_label = tk.Label(user_info_frame, text="Confirm Password:")
        conf_password_label.grid(row=5, column=0, sticky=tk.W)
        conf_password_texbox = tk.Entry(user_info_frame, width=58, show='*')
        conf_password_texbox.grid(row=5, column=1, columnspan=3)

        register_button = tk.Button(user_info_frame, text="Register", bg=self.colour1, command=register_user)
        register_button.grid(row=6, column=1, sticky='news', columnspan=3)

        login_button = tk.Button(user_info_frame, text="Go to Login Screen", bg=self.colour1, command=self.page2)
        login_button.grid(row=7, column=1, sticky='news', columnspan=3)

    def page2(self):
        self.clear_frame(self.page_container)

        def login_user():
            user_name = username_textbox.get().strip()
            if authenticate.check_password(user_name,password_textbox.get().strip()):
                # messagebox.showinfo('Sign in success', 'You have logged in successfully')
                self.USER = user_name
                self.page3()
            else:
                messagebox.showerror('Sign in Fail', 'Wrong password or username')

        title = tk.Label(
            self.page_container,
            background=self.colour1,
            foreground=self.colour3,
            height=2,
            font=('Arial', 26, 'bold'),
            text='Login / Signup'
        )
        title.grid(column=0, row=0)

        user_info_frame = tk.LabelFrame(
            self.page_container,
            text='Login Information',
            pady=20,
            padx=20,
        )
        user_info_frame.grid(row=1, column=0, sticky='news')

        username_label = tk.Label(user_info_frame, text="Username:")
        username_label.grid(row=0, column=0, sticky=tk.W)
        username_textbox = tk.Entry(user_info_frame, width=58)
        username_textbox.grid(row=0, column=1, columnspan=3, sticky=tk.W)

        password_label = tk.Label(user_info_frame, text="Password:")
        password_label.grid(row=1, column=0, sticky=tk.W)
        password_textbox = tk.Entry(user_info_frame, width=58, show='*')
        password_textbox.grid(row=1, column=1, columnspan=3, sticky=tk.W)

        login_button = tk.Button(user_info_frame, text="Login", bg=self.colour1, fg='white', command=login_user)
        login_button.grid(row=2, column=1, sticky='news', columnspan=3, pady=10)

        signup_button = tk.Button(user_info_frame, text="Register", bg=self.colour1, fg='white', command=self.page1)
        signup_button.grid(row=3, column=1, sticky='news', columnspan=3, pady=20)



    def page3(self):
        self.clear_frame(self.page_container)

        title = tk.Label(
            self.page_container,
            background=self.colour1,
            foreground=self.colour3,
            height=2,
            font=('Arial', 26, 'bold'),
            text='Main Menu'
        )
        title.grid(column=0, row=0)

        user_info_frame = tk.LabelFrame(
            self.page_container,
            text='Main Menu',
            pady=20,
            padx=20,
        )
        user_info_frame.grid(row=1, column=0, sticky='news')

        order_button = tk.Button(user_info_frame, text='New Order', width=13, height=5, command=self.page4)
        order_button.grid(row=0, column=0)

        profile_button = tk.Button(user_info_frame, text='My Profile', width=13, height=5, command=self.page6)
        profile_button.grid(row=0, column=1)

        my_orders_button = tk.Button(user_info_frame, text='My Orders', width=13, height=5, command=self.page5)
        my_orders_button.grid(row=0, column=2)

        billing_button = tk.Button(user_info_frame, text='Billing', width=13, height=5,)
        billing_button.grid(row=0, column=3)

    def page4(self):
        self.clear_frame(self.page_container)

        title = tk.Label(
            self.page_container,
            background=self.colour1,
            foreground=self.colour3,
            height=2,
            font=('Arial', 26, 'bold'),
            text='New Order'
        )
        title.grid(column=0, row=0)

        user_info_frame = tk.LabelFrame(
            self.page_container,
            text='Review Details',
            pady=20,
            padx=20,
        )
        user_info_frame.grid(row=1, column=0, sticky='news')

        date_label = tk.Label(user_info_frame, text="Delivery Date:")
        date_label.grid(row=0, column=0, sticky=tk.W)
        date_texbox = tk.Entry(user_info_frame, width=20)
        date_texbox.grid(row=0, column=1, sticky=tk.W)

        time_label = tk.Label(user_info_frame, text="Time:")
        time_label.grid(row=0, column=2, sticky=tk.W)
        age_picker = ttk.Combobox(user_info_frame, values=['10h00', '11h00', '12h00', '13h00', '14h00', '15h00',
                                                           '16h00', '17h00', '18h00', '19h00', '20h00', '21h00'], state='readonly')
        age_picker.grid(row=0, column=3, sticky='w')

        pax_label = tk.Label(user_info_frame, text="No. of People:")
        pax_label.grid(row=1, column=2, sticky=tk.W)
        number_of_people = []
        for i in range(50):
            number_of_people.append(i)
        pax_picker = ttk.Combobox(user_info_frame, values=number_of_people, state='readonly')
        pax_picker.grid(row=1,column=3,sticky=tk.W)

        packages_label = tk.Label(user_info_frame, text="Packages:")
        packages_label.grid(row=1, column=0, sticky=tk.W)
        packages = data.get_packages()
        package_picker = ttk.Combobox(user_info_frame, width=10, values=packages, state='readonly')
        package_picker.grid(row=2,column=0, sticky=tk.NW)
        package_picker.bind('<<ComboboxSelected>>', lambda _: update_package_list_items())

        package_list = tk.Listbox(user_info_frame)
        package_list.grid(row=2, column=1)

        def update_package_list_items():
            package = package_picker.get()
            package_list.delete(0,tk.END)
            package_list_items = data.get_package_items(package)
            for item in package_list_items:
                package_list.insert(0,item)

        place_order_button = tk.Button(user_info_frame, text='Place Order', width=10, height=5)
        place_order_button.grid(row=2, column=3)

        register_button = tk.Button(user_info_frame, text="Cancel", bg=self.colour1, command=self.page3)
        register_button.grid(row=3, column=1, sticky='news', columnspan=3)

    def page5(self):
        self.clear_frame(self.page_container)

        title = tk.Label(
            self.page_container,
            background=self.colour1,
            foreground=self.colour3,
            height=2,
            font=('Arial', 26, 'bold'),
            text='My Orders'
        )
        title.grid(column=0, row=0)

        user_info_frame = tk.LabelFrame(
            self.page_container,
            text='My Order History',
            pady=20,
            padx=20,
        )
        user_info_frame.grid(row=1, column=0, sticky='news')

# TABLE TO DISPLAY ORDER HISTORY
        table = ttk.Treeview(user_info_frame, columns=('Order Date','Delivery Date','Address','Package', 'People',
                                                       'Status'),
                             show='headings')
        # Format Columns
        table.column('Order Date', width=100)
        table.column('Delivery Date', width=100)
        table.column('Address', width=120)
        table.column('Package', width=100)
        table.column('People', width=100)
        table.column('Status', width=100)

        # Set headings
        table.heading('Order Date', text='OrderDate', anchor=tk.W)
        table.heading('Delivery Date', text='Delivery Date', anchor=tk.W)
        table.heading('Address', text='Address', anchor=tk.W)
        table.heading('Package', text='Package')
        table.heading('People', text='People')
        table.heading('Status', text='Status')
        table.grid(row=0, column=0)
        orders = data.get_oders(self.USER)  # Get List of oders from the data

        for item in orders:
            table.insert('', tk.END, values=item)

        main_menu_button = tk.Button(user_info_frame, text="Back to Main Menu", bg=self.colour1, command=self.page3)
        main_menu_button.grid(row=1, column=0, sticky='news', columnspan=3)

        logout_button = tk.Button(user_info_frame, text="log Out", bg=self.colour1, command=self.logout, pady=10)
        logout_button.grid(row=2, column=0, sticky='news', columnspan=3)
    def page6(self):
        self.clear_frame(self.page_container)

        title = tk.Label(
            self.page_container,
            background=self.colour1,
            foreground=self.colour3,
            height=2,
            font=('Arial', 26, 'bold'),
            text='My Profile'
        )
        title.grid(column=0, row=0)

        user_info_frame = tk.LabelFrame(
            self.page_container,
            text='Edit Your Details',
            pady=20,
            padx=20,
        )
        user_info_frame.grid(row=1, column=0, sticky='news')

        profile = data.get_profile(self.USER)  # Current User Details

        name_label = tk.Label(user_info_frame, text="First Name:", font=('Arial', 16), pady=10, fg=self.colour1)
        name_label.grid(row=0, column=0, sticky=tk.W)
        name = tk.Label(user_info_frame, width=20, text=profile[0], anchor='w')
        name.grid(row=0, column=1, sticky=tk.W)

        sname_label = tk.Label(user_info_frame, text="Surname:", font=('Arial', 16), pady=10, fg=self.colour1)
        sname_label.grid(row=0, column=2, sticky=tk.W)
        sname = tk.Label(user_info_frame, width=28, text=profile[1], anchor='w')
        sname.grid(row=0, column=3, sticky=tk.W)

        email_label = tk.Label(user_info_frame, text="Email:", font=('Arial', 16), pady=10, fg=self.colour1)
        email_label.grid(row=1, column=0, sticky=tk.W)
        email = tk.Label(user_info_frame, width=58, text=self.USER, anchor='w')
        email.grid(row=1, column=1, columnspan=3, sticky=tk.W)

        gender_label = tk.Label(user_info_frame, text="Gender:", font=('Arial', 16), pady=10, fg=self.colour1)
        gender_label.grid(row=2, column=0, sticky=tk.W)
        gender = ttk.Label(user_info_frame, text=profile[4], anchor='w')
        gender.grid(row=2, column=1, sticky='w')

        age_label = tk.Label(user_info_frame, text="Age:", font=('Arial', 16), pady=10, fg=self.colour1)
        age_label.grid(row=2, column=2, sticky=tk.W)
        age = ttk.Label(user_info_frame, text=profile[5], anchor='w')
        age.grid(row=2, column=3, sticky='w')

        # address_label = tk.Label(user_info_frame, text="Address:", font=('Arial', 16))
        # address_label.grid(row=3, column=0, sticky=tk.W)
        # address_texbox = tk.Entry(user_info_frame, width=58)
        # address_texbox.grid(row=3, column=1, columnspan=3)

        main_button = tk.Button(user_info_frame, text="Back to Main Menu", bg=self.colour1, command=self.page3)
        main_button.grid(row=6, column=1, sticky='news', columnspan=3)

        update_button = tk.Button(user_info_frame, text="Update", bg=self.colour1, command=self.page1)
        update_button.grid(row=7, column=1, sticky='news', columnspan=3)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x500")
    root.title('PARTY EATS')
    app = Interface(root)
    root.mainloop()
