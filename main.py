import tkinter as tk
from scraper.gui import ScraperApp

if __name__ == "__main__":
    root = tk.Tk()
    app = ScraperApp(root)
    root.mainloop()