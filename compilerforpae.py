def compile_to_python(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    python_code = ""
    for line in lines:
        command, *args = line.strip().split()
        if command == "text":
            # Add a print statement with the specified text
            text = ' '.join(args)
            python_code += f'print("{text}")\n'
        elif command == "window":
            # Add code to create an empty 800x600 Tkinter window
            python_code += '''
import tkinter as tk

window = tk.Tk()
window.geometry("800x600")
window.mainloop()
'''
        else:
            # If there's anything else after the window command, add it as text into a Tk window
            if python_code.endswith("window.mainloop()\n"):
                text = ' '.join(args)
                python_code = python_code.replace("window.mainloop()\n", f'''
label = tk.Label(window, text="{text}")
label.place(relx=0.5, rely=0.5, anchor="center")
window.mainloop()
''')
            else:
                print(f"Ignoring unrecognized command: {command}")

    # Write the generated Python code to the output file
    with open(output_file, 'w') as file:
        file.write(python_code)

def main():
    input_file = "main.pae"  # Change this to the name of your input ".pae" file
    output_file = "main.py"   # Change this to the name of the output Python file

    # Compile the ".pae" file to Python
    compile_to_python(input_file, output_file)
    print(f"Compilation completed. Python file: {output_file}")

if __name__ == "__main__":
    main()
