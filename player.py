import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

class SimplePlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TCPlayer")
        
        # Set the background color to white
        self.root.configure(bg="white")
        
        # Main frame for layout with white background
        main_frame = tk.Frame(root, bg="white")
        main_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Custom style for buttons to simulate rounded corners and add a gray border
        style = ttk.Style()
        style.configure("RoundedButton.TButton",
                        font=("Arial", 10),
                        padding=6,
                        relief="solid",
                        borderwidth=1,
                        background="white",
                        foreground="black")
        
        style.map("RoundedButton.TButton",
                  background=[("active", "#e0e0e0")],  # Change color on hover
                  relief=[("pressed", "sunken")])

        # Textbox for user input with white background and gray border
        text_frame = tk.Frame(main_frame, bg="gray", bd=1)  # Gray border around text box
        text_frame.pack(pady=10, padx=10)
        
        self.text_box = ScrolledText(text_frame, height=10, width=50, font=("Arial", 12), bg="white", bd=0, relief="flat")
        self.text_box.pack()

        # Frame for control buttons
        controls_frame = tk.Frame(main_frame, bg="white")
        controls_frame.pack(pady=10)

        # Play, Pause, and Restart buttons with rounded style and gray border
        self.play_button = ttk.Button(controls_frame, text="Play", style="RoundedButton.TButton", command=self.play)
        self.play_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = ttk.Button(controls_frame, text="Pause", style="RoundedButton.TButton", command=self.pause)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.restart_button = ttk.Button(controls_frame, text="Restart", style="RoundedButton.TButton", command=self.restart)
        self.restart_button.pack(side=tk.LEFT, padx=10)

    def play(self):
        print("Playing text")

    def pause(self):
        print("Pausing text")

    def restart(self):
        print("Restarting text")

    def run(self):
        self.root.mainloop()


# Initialize tkinter main window
root = tk.Tk()

# Create and run the app
app = SimplePlayerApp(root)
app.run()
