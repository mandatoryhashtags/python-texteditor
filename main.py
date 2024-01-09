import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py")])
    
    if not filepath:
        return
    
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)

    window.title(f"Text by MHT: {filepath}")

def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py")])

    if not filepath:
        return


    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)

    window.title(f"Text by MHT: {filepath}")

def main():
    # Window Creation
    window = tk.Tk()
    window.title("Text by MHT")
    window.rowconfigure(0,minsize=400)
    window.columnconfigure(0,minsize=100)
    window.columnconfigure(1,minsize=500)


    # Text Editor
    text_edit = tk.Text(window,font="Helvetica 16")
    text_edit.grid(row=0, column=1)

    # Framing
    frame = tk.Frame(window, relief=tk.RIDGE, bd=2)
    frame.grid(row=0, column=0, sticky="ns")

    # Buttons
    save_button = tk.Button(
        frame, text="Save", font="Helvetica 12", justify="center", padx=5, pady=5, 
        command=lambda: save_file(window, text_edit))
    open_button = tk.Button(
        frame, text="Open", font="Helvetica 12", justify="center", padx=5, pady=5, 
        command=lambda: open_file(window, text_edit))

    save_button.grid(row=0, column=0, sticky="ew")
    open_button.grid(row=1, column=0, sticky="ew")

    # Keyboard Shortcuts
    # TODO Move this to a config json file and load it here
    window.bind('<Control-s>', lambda x: save_file(window, text_edit))
    window.bind('<Control-o>', lambda x: open_file(window, text_edit))

    # Running Loop
    window.mainloop()

main()
