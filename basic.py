import cmd
import tkinter as tk
import os

class PlateInterpreter(cmd.Cmd):
    prompt = 'plater > '
    window = None

    def do_text(self, arg):
        """Prints out the text."""
        print(arg)

    def do_window(self, arg):
        """Creates a window with optional text."""
        if not self.window:
            self.window = tk.Tk()
            self.window.geometry("800x600")
            self.window.title("plate window")
            print("plate window created :)")
        else:
            print("plate window already exists")

        # Display optional text in the window
        if arg:
            label = tk.Label(self.window, text=arg)
            label.place(relx=0.5, rely=0.5, anchor="center")

    def do_delete(self, arg):
        """Deletes the window."""
        if self.window:
            self.window.destroy()
            self.window = None
            print("plate window deleted.")
        else:
            print("man you trippin there ain't no window")

    def do_createfile(self, arg):
        """Creates a file named main.pae in the current directory."""
        file_path = os.path.join(os.getcwd(), "main.pae")
        try:
            with open(file_path, "w") as file:
                print("main.pae created.")
        except Exception as e:
            print(f"Error creating main.pae: {e}")

    def do_open(self, arg):
        """Runs the commands in the main.pae file."""
        file_path = os.path.join(os.getcwd(), "main.pae")
        try:
            with open(file_path, "r") as file:
                for line in file:
                    self.onecmd(line.strip())
        except FileNotFoundError:
            print("main.pae not found.")

    def do_exit(self, arg):
        """Exit the program."""
        print("buh bye")
        if self.window:
            self.window.destroy()
        return True

    def do_credits(self, arg):
        """Displays the credits and exits."""
        try:
            with open("README.txt", "r") as file:
                print(file.read())  # Print contents of README.txt
        except FileNotFoundError:
            print("README.txt not found.")
        return True  # Exit the program

    def do_EOF(self, line):
        """Exit the interpreter."""
        print("\nbuh bye")
        if self.window:
            self.window.destroy()
        return True

if __name__ == '__main__':
    PlateInterpreter().cmdloop()
