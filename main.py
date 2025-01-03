import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import importlib


class GameManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Management System")
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", self.toggle_fullscreen)

        self.games_folder = "./games"
        self.assets_folder = "./assets"

        self.create_custom_scrollbar_style()
        self.create_gradient_background()
        self.create_game_menu()

    def toggle_fullscreen(self, event=None):
        """Toggle fullscreen mode."""
        current_state = self.root.attributes('-fullscreen')
        self.root.attributes('-fullscreen', not current_state)
        return "break"

    def create_custom_scrollbar_style(self):
        """Create a custom style for the scrollbar."""
        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "Vertical.TScrollbar",
            gripcount=0,
            background="#4682B4", 
            darkcolor="#2E8B57",  
            lightcolor="#5F9EA0", 
            troughcolor="#87CEEB",
            bordercolor="#4682B4",
            arrowcolor="#FFFFFF"  
        )

    def create_gradient_background(self):
        """Create a gradient background using Canvas."""
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()

        if not hasattr(self, 'canvas_bg') or not self.canvas_bg.winfo_exists():
            self.canvas_bg = tk.Canvas(self.root, width=width, height=height, highlightthickness=0)
            self.canvas_bg.place(relx=0, rely=0, relwidth=1, relheight=1)

        for i in range(height):
            color = f"#{int(30 + i * 0.2):02X}D0FF"
            self.canvas_bg.create_line(0, i, width, i, fill=color)

    def draw_gradient(self, canvas, width, height):
        """Create a gradient background on a specific canvas with larger color steps."""
        canvas.delete("gradient")
        for i in range(height):
            color_step = int(90 + i * 0.2)
            color = f"#{min(color_step, 255):02X}D0FF"
            canvas.create_line(0, i, width, i, fill=color, tags="gradient")

    def create_game_menu(self):
        """Create the game menu with cards."""
        if not hasattr(self, 'canvas_bg') or not self.canvas_bg.winfo_exists():
            self.create_gradient_background()

        for widget in self.root.winfo_children():
            if widget != self.canvas_bg:
                widget.destroy()

        self.canvas_bg.create_text(
            self.root.winfo_width() // 2, 50,
            text="🎮 Game Menu 🎮",
            font=("Helvetica", 36, "bold"),
            fill="white",
            anchor="center"
        )

        canvas = tk.Canvas(self.root, bg="#4682B4", highlightthickness=0)
        canvas.place(relx=0.5, rely=0.55, anchor="center", width=850, height=580)

        self.draw_gradient(canvas, 850, 580)

        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=canvas.yview, style="Vertical.TScrollbar")
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(in_=canvas, relx=1.0, rely=0, relheight=1.0, anchor="ne")

        scrollable_frame = tk.Frame(canvas, bg="#4682B4")
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        games = [game for game in os.listdir(self.games_folder) if os.path.isdir(os.path.join(self.games_folder, game))]
        for game in games:
            self.create_game_card(scrollable_frame, game)

    
    def create_game_card(self, parent, game_name):
        """Create an advanced game card with hover effects and icons."""
        card_frame = tk.Frame(parent, bg="", borderwidth=2, relief="flat")
        card_frame.pack(pady=(1, 1), padx=(1, 1), fill="x", expand=True)

        icon_path = self.find_icon(game_name)
        if icon_path:
            icon_image = Image.open(icon_path).resize((100, 100), Image.Resampling.LANCZOS)
            icon = ImageTk.PhotoImage(icon_image)
        else:
            icon = None

        if icon:
            icon_label = tk.Label(card_frame, image=icon, bg="black")
            icon_label.image = icon
            icon_label.pack(side="left", padx=20, pady=10)

        game_title = tk.Label(
            card_frame,
            text=game_name.replace("_", " ").title(),
            font=("Helvetica", 20, "bold"),
            fg="#333333"
        )
        game_title.pack(anchor="w", padx=10, pady=10)

        self.set_label_bg_color(game_title, card_frame)

        play_button = tk.Button(
            card_frame,
            text="▶ Play",
            font=("Helvetica", 14, "bold"),
            activebackground="#4682B4",
            activeforeground="black",
            relief="flat",
            cursor="hand2",
            command=lambda g=game_name: self.launch_game(g)
        )
        play_button.pack(pady=10, padx=10)

        play_button.bind("<Enter>", lambda e: play_button.configure(bg="#4682B4"))
        play_button.bind("<Leave>", lambda e: play_button.configure(bg="#1E90FF"))

    def set_label_bg_color(self, label, parent):
        """Set the background color of a label dynamically based on its position."""
        parent.update_idletasks() 
        y_position = label.winfo_y() + parent.winfo_y()
        color_step = int(90 + y_position * 0.2)
        bg_color = f"#{min(color_step, 255):02X}D0FF"
        label.configure(bg=bg_color)

    def find_icon(self, game_name):
        """Find the icon image file for a game."""
        for ext in ["jpeg", "png", "jpg"]:
            icon_path = os.path.join(self.assets_folder, f"{game_name}_icon.{ext}")
            if os.path.exists(icon_path):
                return icon_path
        return None

    def launch_game(self, game_name):
        """Launch the selected game."""
        try:
            game_module = importlib.import_module(f"games.{game_name}.main")
            game_module.start_game(self.root, self.create_game_menu)
        except Exception as e:
            print(f"Error launching game {game_name}: {e}")
            messagebox.showerror("Error", f"Failed to launch {game_name}.")


if __name__ == "__main__":
    root = tk.Tk()
    app = GameManagementSystem(root)
    root.mainloop()
