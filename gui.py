import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
from scraper.backend import scrape_website

class ScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic Content Scraper")
        self.root.geometry("800x600")

        tk.Label(root, text="Enter URL:").pack(pady=5)
        self.url_entry = tk.Entry(root, width=80)
        self.url_entry.pack(pady=5)

        tk.Button(root, text="Scrape Content", command=self.scrape).pack(pady=10)

        self.text_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=25)
        self.text_display.pack(padx=10, pady=10)

        tk.Button(root, text="Save Content", command=self.save_content).pack(pady=10)

    def scrape(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a URL")
            return
        try:
            content = scrape_website(url)
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_content(self):
        content = self.text_display.get(1.0, tk.END)
        if not content.strip():
            messagebox.showerror("Error", "No content to save")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            messagebox.showinfo("Success", "Content saved successfully")