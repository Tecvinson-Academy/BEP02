import tkinter as tk
from tkinter import ttk


class Interface(tk.Frame):
    def __init__(self, root):
        self.pager = None
        self.current_page_index = 0
        self.pages = [self.page1, self.page2, self.page3, self.page4]
        self.colour1 = '#222448'
        self.colour2 = '#54527E'
        self.colour3 = 'WHITE'

        super().__init__(root, bg=self.colour1)

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        self.load_main_widgets()

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

            match button:
                case 'Previous':
                    self.current_page_index -= 1
                    self.pages[self.current_page_index]()
                case 'Next':
                    self.current_page_index +=1
                    self.pages[self.current_page_index]()

            if self.current_page_index == 0:
                prev_button.config(state=tk.DISABLED)
            else:
                prev_button.config(state=tk.ACTIVE)

            if self.current_page_index == len(self.pages) - 1:
                next_button.config(state=tk.DISABLED)
            else:
                next_button.config(state=tk.ACTIVE)

            self.page_number['text'] = f'{self.current_page_index + 1} / {len(self.pages)}'
        # Navigation Button
        prev_button = tk.Button(
            self.pager,
            background=self.colour2,
            foreground=self.colour3,
            activebackground=self.colour2,
            activeforeground=self.colour3,
            disabledforeground='#3B3A56',
            highlightthickness=0,
            width=7,
            relief=tk.FLAT,
            font=('Arial', 18),
            cursor='hand1',
            text='Previous',
            state=tk.DISABLED,
            command=lambda button='Previous':change_page(button)
        )
        prev_button.grid(column=0, row=0)

        self.page_number = tk.Label(
            self.pager,
            background=self.colour1,
            foreground=self.colour3,
            font=('Arial', 18),
            text=f'{self.current_page_index + 1} / {len(self.pages)}'
        )
        self.page_number.grid(column=1, row=0)

        next_button = tk.Button(
            self.pager,
            background=self.colour2,
            foreground=self.colour3,
            activebackground=self.colour2,
            activeforeground=self.colour3,
            disabledforeground='#3B3A56',
            highlightthickness=0,
            width=7,
            relief=tk.FLAT,
            font=('Arial', 18),
            cursor='hand1',
            text='Next',
            command=lambda button='Next': change_page(button)
        )
        next_button.grid(column=2, row=0)


    def page1(self):
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
        password_textbox = tk.Entry(user_info_frame, width=58, show="*")
        password_textbox.grid(row=4, column=1, columnspan=3)

        conf_password_label = tk.Label(user_info_frame, text="Confirm Password:")
        conf_password_label.grid(row=5, column=0, sticky=tk.W)
        conf_password_texbox = tk.Entry(user_info_frame, width=58, show="*")
        conf_password_texbox.grid(row=5, column=1, columnspan=3)

        def toggle_password_visibility():
            if password_textbox.cget('show') == '*':
                password_textbox.config(show='')
                conf_password_texbox.config(show='')
            else:
                password_textbox.config(show='*')
                conf_password_texbox.config(show='*')

        show_password_var = tk.IntVar()
        show_password_check = tk.Checkbutton(
            user_info_frame,
            text="Show Password",
            variable=show_password_var,
            command=toggle_password_visibility
        )
        show_password_check.grid(row=6, column=1, sticky=tk.W)

        register_button = tk.Button(user_info_frame, text="Register", bg=self.colour1,
                                     command=self.register_user)
        register_button.grid(row=7, column=1, sticky='news', columnspan=3)

    def register_user(self):
        first_name = self.page_container.winfo_children()[1].winfo_children()[1].get()
        surname = self.page_container.winfo_children()[1].winfo_children()[3].get()
        email = self.page_container.winfo_children()[1].winfo_children()[5].get()
        gender = self.page_container.winfo_children()[1].winfo_children()[7].get()
        age = self.page_container.winfo_children()[1].winfo_children()[9].get()
        address = self.page_container.winfo_children()[1].winfo_children()[11].get()
        password = self.page_container.winfo_children()[1].winfo_children()[13].get()
        conf_password = self.page_container.winfo_children()[1].winfo_children()[15].get()

        success = registration.register_user(first_name, surname, email, gender, age, address, password, conf_password)
        
        if success:
            self.clear_entries()

    def clear_entries(self):
        for widget in self.page_container.winfo_children()[1].winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)
            elif isinstance(widget, ttk.Combobox):
                widget.set('')

                
    def page2(self):
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

        username_label = tk.Label(user_info_frame, text='Email Address')
        username_label.grid(row=0, column=0)
        username_entry = tk.Entry(user_info_frame, width=60)
        username_entry.grid(row=0, column=1)

        password_label = tk.Label(user_info_frame, text='Password')
        password_label.grid(row=1, column=0)
        password_entry = tk.Entry(user_info_frame, width=60)
        password_entry.grid(row=1, column=1)

        # content = tk.Label(
        #     self.page_container,
        #     background=self.colour2,
        #     foreground=self.colour3,
        #     justify=tk.LEFT,
        #     anchor=tk.N,
        #     pady=20,
        #     font=('Arial', 16),
        #     text='',
        #     wraplength=600
        # )
        # content.grid(column=0, row=1, sticky=tk.NSEW)


    def page3(self):
        title = tk.Label(
            self.page_container,
            background=self.colour1,
            foreground=self.colour3,
            height=2,
            font=('Arial', 26, 'bold'),
            text='Page 3'
        )
        title.grid(column=0, row=0)

        text = ('Aenean vitae est nulla. Duis ipsum orci, accumsan id consectetur quis, '
                'placerat id libero. Maecenas nisl mauris, sodales non ultrices quis, '
                'consectetur a felis. Maecenas at hendrerit nibh, sed tempor mi. Proin '
                'elementum nibh at sem tristique, vitae vehicula turpis mattis. Vivamus sed '
                'pellentesque arcu, eget egestas diam. Donec viverra odio id mollis commodo.')

        content = tk.Label(
            self.page_container,
            background=self.colour2,
            foreground=self.colour3,
            justify=tk.LEFT,
            anchor=tk.N,
            pady=20,
            font=('Arial', 16),
            text=text,
            wraplength=600
        )
        content.grid(column=0, row=1, sticky=tk.NSEW)

    def page4(self):
        title = tk.Label(
            self.page_container,
            background=self.colour1,
            foreground=self.colour3,
            height=2,
            font=('Arial', 26, 'bold'),
            text='Page 4'
        )
        title.grid(column=0, row=0)

        text = ('Maecenas tincidunt pharetra est eget tempus. Aliquam hendrerit '
                'ullamcorper justo ut dictum. Donec molestie sodales dui, '
                'ac posuere turpis placerat et. Integer viverra orci in felis '
                'hendrerit viverra. Aliquam pulvinar odio ac facilisis pulvinar. '
                'Suspendisse pretium aliquam lectus, lobortis mattis tellus pellentesque eget.')

        content = tk.Label(
            self.page_container,
            background=self.colour2,
            foreground=self.colour3,
            justify=tk.LEFT,
            anchor=tk.N,
            pady=20,
            font=('Arial', 16),
            text=text,
            wraplength=600
        )
        content.grid(column=0, row=1, sticky=tk.NSEW)


root = tk.Tk()
root.title('Party Planner App')
root.geometry('700x500')
interface_instance = Interface(root)

root.mainloop()
