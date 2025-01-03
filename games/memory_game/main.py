import tkinter as tk

def start_game(root, return_to_menu):
    """Start the Memory Game."""
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Label(root, 
         text="🧠 Memory Game 🧠", 
         font=("Helvetica", 36, "bold"),  
         bg="#c1e5fe",  
         padx=10, 
         pady=5, 
         relief="solid"  
    ).pack(pady=5)

    back_button = tk.Button(root, 
                    text="⬅ Back to Menu", 
                    font=("Helvetica", 14, "bold"), 
                    activebackground="#4682B4",
                    activeforeground="black",
                    relief="flat",
                    cursor="hand2",
                    command=return_to_menu,
                    
    )
    back_button.pack(pady=20)
    
    from games.memory_game.memory_game_GUI import MemoryGameGUI
    game = MemoryGameGUI(root)  
