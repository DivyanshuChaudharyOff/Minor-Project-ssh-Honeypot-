import tkinter as tk
from tkinter import scrolledtext
from honeypot_server import SSHHoneypotServer

class HoneypotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SSH Honeypot Server")

        # Create start and stop buttons
        self.start_button = tk.Button(self.root, text="Start Honeypot", command=self.start_server)
        self.start_button.grid(row=0, column=0, padx=10, pady=10)

        self.stop_button = tk.Button(self.root, text="Stop Honeypot", command=self.stop_server, state=tk.DISABLED)
        self.stop_button.grid(row=0, column=1, padx=10, pady=10)

        # Create a text area to log the connection attempts
        self.log_area = scrolledtext.ScrolledText(self.root, width=50, height=20)
        self.log_area.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.log_area.config(state=tk.DISABLED)

        # Initialize honeypot server instance
        self.server = None

    # Function to log messages to the text area
    def log_message(self, message):
        self.log_area.config(state=tk.NORMAL)
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.config(state=tk.DISABLED)

    # Start the honeypot server
    def start_server(self):
        self.server = SSHHoneypotServer(log_callback=self.log_message)
        self.server.start()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    # Stop the honeypot server
    def stop_server(self):
        if self.server:
            self.server.stop()
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

# Main function to initialize the UI
if __name__ == "__main__":
    root = tk.Tk()
    app = HoneypotUI(root)
    root.mainloop()
