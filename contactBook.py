import tkinter as tk
from tkinter import ttk, messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Initialize an empty list to store contacts
        self.contacts = []

        # Main Frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(padx=20, pady=20)

        # Labels and Entry fields for contact information
        label_name = tk.Label(main_frame, text="Name:")
        label_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_name = tk.Entry(main_frame, width=30)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        label_email = tk.Label(main_frame, text="Email:")
        label_email.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_email = tk.Entry(main_frame, width=30)
        self.entry_email.grid(row=1, column=1, padx=10, pady=5)

        label_phone = tk.Label(main_frame, text="Phone:")
        label_phone.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_phone = tk.Entry(main_frame, width=30)
        self.entry_phone.grid(row=2, column=1, padx=10, pady=5)

        label_address = tk.Label(main_frame, text="Address:")
        label_address.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_address = tk.Entry(main_frame, width=30)
        self.entry_address.grid(row=3, column=1, padx=10, pady=5)

        # Buttons Frame
        buttons_frame = tk.Frame(main_frame)
        buttons_frame.grid(row=4, column=0, columnspan=2, pady=10)

        add_button = tk.Button(buttons_frame, text="Add Contact", command=self.add_contact, width=15)
        add_button.pack(side=tk.LEFT, padx=5)

        view_button = tk.Button(buttons_frame, text="View Contacts", command=self.view_contacts, width=15)
        view_button.pack(side=tk.LEFT, padx=5)

        search_button = tk.Button(buttons_frame, text="Search Contact", command=self.search_contact, width=15)
        search_button.pack(side=tk.LEFT, padx=5)

        update_button = tk.Button(buttons_frame, text="Update Contact", command=self.update_contact, width=15)
        update_button.pack(side=tk.LEFT, padx=5)

        delete_button = tk.Button(buttons_frame, text="Delete Contact", command=self.delete_contact, width=15)
        delete_button.pack(side=tk.LEFT, padx=5)

        # Table Frame
        table_frame = tk.Frame(main_frame)
        table_frame.grid(row=5, column=0, columnspan=2, pady=10)

        # Table to display contacts
        self.tree = ttk.Treeview(table_frame, columns=("Name", "Email", "Phone", "Address"), show="headings", selectmode="browse")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Address", text="Address")
        self.tree.column("Name", width=150)
        self.tree.column("Email", width=200)
        self.tree.column("Phone", width=120)
        self.tree.column("Address", width=250)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for the table
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)

    def add_contact(self):
        name = self.entry_name.get().strip()
        email = self.entry_email.get().strip()
        phone = self.entry_phone.get().strip()
        address = self.entry_address.get().strip()

        if not (name and email and phone and address):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if not self.validate_email(email):
            messagebox.showerror("Error", "Invalid email format.")
            return

        if not self.validate_phone(phone):
            messagebox.showerror("Error", "Invalid phone number format.")
            return

        contact = {'Name': name, 'Email': email, 'Phone': phone, 'Address': address}
        self.contacts.append(contact)
        self.update_table()
        messagebox.showinfo("Success", "Contact added successfully!")
        self.clear_entries()

    def view_contacts(self):
        # Clear existing items in the table
        self.tree.delete(*self.tree.get_children())

        if not self.contacts:
            messagebox.showwarning("Warning", "No contacts to display.")
        else:
            for contact in self.contacts:
                self.tree.insert("", "end", values=(contact['Name'], contact['Email'], contact['Phone'], contact['Address']))

    def search_contact(self):
        name_to_search = self.entry_name.get().strip().lower()
        found_contacts = []

        for contact in self.contacts:
            if name_to_search in contact['Name'].lower():
                found_contacts.append(contact)

        if found_contacts:
            # Clear existing items in the table
            self.tree.delete(*self.tree.get_children())
            
            for contact in found_contacts:
                self.tree.insert("", "end", values=(contact['Name'], contact['Email'], contact['Phone'], contact['Address']))
        else:
            messagebox.showwarning("Not Found", f"No contact found with name containing '{name_to_search}'.")

    def update_contact(self):
        selected_item = self.tree.selection()
        
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a contact from the list.")
            return
        
        name_to_update = self.tree.item(selected_item)['values'][0]

        name = self.entry_name.get().strip()
        email = self.entry_email.get().strip()
        phone = self.entry_phone.get().strip()
        address = self.entry_address.get().strip()

        if not (name and email and phone and address):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if not self.validate_email(email):
            messagebox.showerror("Error", "Invalid email format.")
            return

        if not self.validate_phone(phone):
            messagebox.showerror("Error", "Invalid phone number format.")
            return

        updated = False
        for contact in self.contacts:
            if contact['Name'] == name_to_update:
                contact['Name'] = name
                contact['Email'] = email
                contact['Phone'] = phone
                contact['Address'] = address
                updated = True

        if updated:
            self.update_table()
            messagebox.showinfo("Success", f"Contact '{name_to_update}' updated successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Not Found", f"No contact found with name '{name_to_update}'.")

    def delete_contact(self):
        selected_item = self.tree.selection()
        
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a contact from the list.")
            return
        
        name_to_delete = self.tree.item(selected_item)['values'][0]
        deleted = False

        for contact in self.contacts[:]:
            if contact['Name'] == name_to_delete:
                self.contacts.remove(contact)
                deleted = True

        if deleted:
            self.update_table()
            messagebox.showinfo("Success", f"Contact '{name_to_delete}' deleted successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Not Found", f"No contact found with name '{name_to_delete}'.")

    def update_table(self):
        # Clear existing items in the table
        self.tree.delete(*self.tree.get_children())

        # Insert updated contacts into the table
        for contact in self.contacts:
            self.tree.insert("", "end", values=(contact['Name'], contact['Email'], contact['Phone'], contact['Address']))

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

    def validate_email(self, email):
        # Simple email validation
        if "@" in email and "." in email:
            return True
        return False

    def validate_phone(self, phone):
        # Simple phone number validation
        if phone.isdigit() and len(phone) >= 10:
            return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
