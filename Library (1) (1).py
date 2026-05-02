
# Create Class Named Library

class Library:
    def __init__(self, name="", author=""):
        self.name = name
        self.author = author
        self.available = True

    def show_details(self):
        print("\n--- Book Details ---")
        print("Name       :", self.name if self.name else "Not given")
        print("Author     :", self.author if self.author else "Not given")
        print("Available  :", "Yes" if self.available else "No")

    def checkout(self):
        if self.available:
            self.available = False
            print("\nBook checked out successfully.")
        else:
            print("\nSorry, book is not available.")


# Main Program
print("1. Enter Book Name")
print("2. Enter Author Name")

choice = input("Choose option (1 or 2): ")

if choice == "1":
    name = input("Enter Book Name: ")
    book = Library(name=name)
elif choice == "2":
    author = input("Enter Author Name: ")
    book = Library(author=author)
else:
    print("Invalid choice")
    exit()

book.show_details()
book.checkout()
book.show_details()
