class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"Name: {self.name}", end="")

# Book class
class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_info(self):
        super().print_info()
        print(f", Author: {self.author}, Pages: {self.pages}")

# Magazine class
class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_info(self):
        super().print_info()
        print(f", Editor: {self.editor}")

# Main program
pub = []
pub.append(Magazine("Donald Duck", "Aki Hyyppä"))
pub.append(Book("Compartment No. 6", "Rosa Liksom", 192))

for publication in pub:
    publication.print_info()
