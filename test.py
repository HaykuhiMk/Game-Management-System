import tkinter as tk
from tkinter import font

def display_fonts():
    root = tk.Tk()
    root.title("Available Fonts")
    root.geometry("600x600")
    canvas = tk.Canvas(root, bg="white")
    scrollbar = tk.Scrollbar(root, command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="white")

    # Configure the canvas to scroll
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Add fonts to the scrollable frame
    fonts = font.families()
    for f in fonts:
        sample_text = tk.Label(scrollable_frame, text=f"Sample Text ({f})", font=(f, 16), bg="white")
        sample_text.pack(padx=10, pady=5, anchor="w")

    # Pack canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    root.mainloop()

display_fonts()
