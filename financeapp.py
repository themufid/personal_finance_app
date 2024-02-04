import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import pandas as pd
from datetime import datetime
from tkcalendar import Calendar

class PersonalFinanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance App")
        self.root.geometry("1920x1080")

        self.page = 1
        self.data = []

        self.navbar_frame = tk.Frame(self.root, bg="#0A1931", width=800, height=40)
        self.navbar_frame.pack(side=tk.TOP, fill=tk.X)

        self.title_label = tk.Label(self.navbar_frame, text="Personal Finance App", font=("Helvetica", 24), bg="#0A1931", fg="white")
        self.title_label.pack(pady=5)

        self.image = Image.open("images/banner.png")
        self.image = self.image.resize((300, 200), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self.root, image=self.image)
        self.image_label.pack()

        self.about_title_label = tk.Label(self.root, text="About Application", font=("Helvetica", 20))
        self.about_title_label.pack(pady=20)

        self.about_description_label = tk.Label(self.root, text=
            """Personal Finance App is a simple application designed to assist you in tracking and managing your daily financial transactions. 
            With this application, you can easily record all your financial transactions. The app also comes with helpful features, 
            such as the ability to save data in Excel format for further reference.""", 
            font=("Helvetica", 14), justify="center")



        self.about_description_label.pack()

        self.add_data_button = tk.Button(self.root, text="Add Data", command=self.go_to_page_2)
        self.add_data_button.pack()

        self.footer_frame = tk.Frame(self.root, bg="black", width=800, height=40)
        self.footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.footer_label = tk.Label(self.footer_frame, text="Copyright 2024. Personal Finance App", font=("Helvetica", 10), bg="#0A1931", fg="white")
        self.footer_label.pack(pady=10)

    def go_to_page_2(self):
        self.clear_widgets()
        self.page = 2

        self.navbar_frame = tk.Frame(self.root, bg="#0A1931", width=800, height=40)
        self.navbar_frame.pack(side=tk.TOP, fill=tk.X)

        self.title_label = tk.Label(self.navbar_frame, text="Personal Finance App", font=("Helvetica", 24), bg="#0A1931", fg="white")
        self.title_label.pack(pady=5)

        self.income_label = tk.Label(self.root, text="Income", font=("Helvetica", 20))
        self.income_label.pack(pady=20)

        self.calendar_label = tk.Label(self.root, text="Date:", font=("Helvetica", 16))
        self.calendar_label.pack()
        self.calendar = Calendar(self.root)
        self.calendar.pack(pady=10)

        self.category_label = tk.Label(self.root, text="Category:", font=("Helvetica", 16))
        self.category_label.pack()
        self.category_entry = tk.Entry(self.root)
        self.category_entry.pack(pady=10)

        self.amount_label = tk.Label(self.root, text="Amount:", font=("Helvetica", 16))
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=10)

        self.description_label = tk.Label(self.root, text="Description:", font=("Helvetica", 16))
        self.description_label.pack()
        self.description_entry = tk.Entry(self.root)
        self.description_entry.pack(pady=10)

        self.save_button = tk.Button(self.root, text="Save", command=self.save_data)
        self.save_button.pack(pady=20)

        self.back_button = tk.Button(self.root, text="Go back", command=self.go_to_page_1)
        self.back_button.pack()

        self.footer_frame = tk.Frame(self.root, bg="black", width=800, height=40)
        self.footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.footer_label = tk.Label(self.footer_frame, text="Copyright 2024. Personal Finance App", font=("Helvetica", 10), bg="#0A1931", fg="white")
        self.footer_label.pack(pady=10)

    def go_to_page_1(self):
        self.clear_widgets()
        self.page = 1

        self.navbar_frame = tk.Frame(self.root, bg="#0A1931", width=800, height=40)
        self.navbar_frame.pack(side=tk.TOP, fill=tk.X)

        self.title_label = tk.Label(self.navbar_frame, text="Personal Finance App", font=("Helvetica", 24), bg="#0A1931", fg="white")
        self.title_label.pack(pady=5)

        self.image = Image.open("images/banner.png")
        self.image = self.image.resize((300, 200), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self.root, image=self.image)
        self.image_label.pack()

        self.about_title_label = tk.Label(self.root, text="About Application", font=("Helvetica", 20))
        self.about_title_label.pack(pady=20)

        self.about_description_label = tk.Label(self.root, text=
            """Personal Finance App is a simple application designed to assist you in tracking and managing your daily financial transactions. 
            With this application, you can easily record all your financial transactions. The app also comes with helpful features, 
            such as the ability to save data in Excel format for further reference.""", 
            font=("Helvetica", 14), justify="center")
        
        self.about_description_label.pack()

        self.add_data_button = tk.Button(self.root, text="Add Data", command=self.go_to_page_2)
        self.add_data_button.pack()

        self.footer_frame = tk.Frame(self.root, bg="black", width=800, height=40)
        self.footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.footer_label = tk.Label(self.footer_frame, text="Copyright 2024. Personal Finance App", font=("Helvetica", 10), bg="#0A1931", fg="white")
        self.footer_label.pack(pady=10)

    def save_data(self):
        date = self.calendar.get_date()
        category = self.category_entry.get()
        amount = self.amount_entry.get()
        description = self.description_entry.get()

        if not all([date, category, amount, description]):
            messagebox.showerror("Please Review Your Data", "Kindly Complete All Columns!")
            return

        self.data.append([date, category, amount, description])

        messagebox.showinfo("Success", "Data Added Successfully!")

        self.display_data()

    def display_data(self):
        self.clear_widgets()

        self.title_label = tk.Label(self.root, text="Financial Data", font=("Helvetica", 20))
        self.title_label.pack(pady=10)

        columns = ["Date", "Category", "Amount", "Description"]
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        self.tree.pack(pady=10)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        for d in self.data:
            self.tree.insert("", "end", values=d)

        self.download_button = tk.Button(self.root, text="Download", command=self.download_data)
        self.download_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Go back", command=self.go_to_page_1)
        self.back_button.pack()

        self.footer_frame = tk.Frame(self.root, bg="black", width=800, height=40)
        self.footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.footer_label = tk.Label(self.footer_frame, text="Copyright 2024. Personal Finance App", font=("Helvetica", 10), bg="#0A1931", fg="white")
        self.footer_label.pack(pady=10)

    def download_data(self):
        filetypes = (
            ("Excel files", "*.xlsx"),
            ("PDF files", "*.pdf")
        )
        filepath = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=filetypes)

        if filepath:
            if filepath.endswith(".xlsx"):
                df = pd.DataFrame(self.data, columns=["Date", "Category", "Amount", "Description"])
                df.to_excel(filepath, index=False, header=["Date", "Category", "Amount", "Description"])
            elif filepath.endswith(".pdf"):
                pass

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalFinanceApp(root)
    root.mainloop()
