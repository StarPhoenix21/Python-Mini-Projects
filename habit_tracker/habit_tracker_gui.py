import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
import json
import datetime
from habit_tracker_terminal import HabitTracker, Habit
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

class HabitTrackerGUI:
    def __init__(self):
        self.tracker = HabitTracker()
        self.tracker.load_from_file()
        
        self.root = ThemedTk(theme="arc")  # Modern theme
        self.root.title("Habit Tracker")
        self.root.geometry("1200x800")
        
        # Configure grid
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=3)
        self.root.grid_rowconfigure(0, weight=1)
        
        # Create main containers
        self.create_sidebar()
        self.create_main_content()
        
        # Style configuration
        self.style = ttk.Style()
        self.style.configure("Custom.TFrame", background="#f0f0f0")
        self.style.configure("Sidebar.TButton", padding=10, width=20)
        
    def create_sidebar(self):
        sidebar = ttk.Frame(self.root, style="Custom.TFrame", padding="10")
        sidebar.grid(row=0, column=0, sticky="nsew")
        
        # Buttons
        ttk.Button(sidebar, text="Add Habit", command=self.show_add_habit_dialog,
                  style="Sidebar.TButton").pack(pady=5)
        ttk.Button(sidebar, text="View All Habits", command=self.show_all_habits,
                  style="Sidebar.TButton").pack(pady=5)
        ttk.Button(sidebar, text="Categories", command=self.show_categories,
                  style="Sidebar.TButton").pack(pady=5)
        ttk.Button(sidebar, text="Statistics", command=self.show_statistics,
                  style="Sidebar.TButton").pack(pady=5)
        ttk.Button(sidebar, text="Save", command=self.save_habits,
                  style="Sidebar.TButton").pack(pady=5)
        
    def create_main_content(self):
        self.main_content = ttk.Frame(self.root, padding="20")
        self.main_content.grid(row=0, column=1, sticky="nsew")
        self.show_all_habits()  # Show habits by default
        
    def show_add_habit_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add New Habit")
        dialog.geometry("400x500")
        dialog.transient(self.root)
        
        ttk.Label(dialog, text="Habit Name:").pack(pady=5)
        name_entry = ttk.Entry(dialog, width=30)
        name_entry.pack(pady=5)
        
        ttk.Label(dialog, text="Category:").pack(pady=5)
        category_entry = ttk.Entry(dialog, width=30)
        category_entry.pack(pady=5)
        
        ttk.Label(dialog, text="Goal Frequency:").pack(pady=5)
        frequency_var = tk.StringVar(value="daily")
        frequencies = ["daily", "weekly", "monthly"]
        frequency_combo = ttk.Combobox(dialog, textvariable=frequency_var,
                                     values=frequencies, state="readonly", width=27)
        frequency_combo.pack(pady=5)
        
        ttk.Label(dialog, text="Goal Count:").pack(pady=5)
        count_var = tk.StringVar(value="1")
        count_entry = ttk.Entry(dialog, textvariable=count_var, width=30)
        count_entry.pack(pady=5)
        
        def save_habit():
            name = name_entry.get().strip()
            if name:
                self.tracker.add_habit(
                    name,
                    category_entry.get().strip() or None,
                    frequency_var.get(),
                    int(count_var.get())
                )
                dialog.destroy()
                self.show_all_habits()
            else:
                messagebox.showerror("Error", "Habit name is required!")
                
        ttk.Button(dialog, text="Save", command=save_habit).pack(pady=20)
        
    def show_all_habits(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()
            
        # Create a canvas for scrolling
        canvas = tk.Canvas(self.main_content)
        scrollbar = ttk.Scrollbar(self.main_content, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Headers
        headers = ["Habit", "Category", "Streak", "Today's Progress", "Actions"]
        for col, header in enumerate(headers):
            ttk.Label(scrollable_frame, text=header, font=("TkDefaultFont", 10, "bold")).grid(
                row=0, column=col, padx=10, pady=5, sticky="w")
            
        # Habit rows
        for idx, (name, habit) in enumerate(self.tracker.habits.items(), 1):
            ttk.Label(scrollable_frame, text=name).grid(
                row=idx, column=0, padx=10, pady=5, sticky="w")
            ttk.Label(scrollable_frame, text=habit.category or "Uncategorized").grid(
                row=idx, column=1, padx=10, pady=5, sticky="w")
            ttk.Label(scrollable_frame, text=f"{habit.get_streak()} days").grid(
                row=idx, column=2, padx=10, pady=5, sticky="w")
            
            progress = habit.get_goal_progress()
            progress_bar = ttk.Progressbar(scrollable_frame, length=100, mode='determinate')
            progress_bar['value'] = progress
            progress_bar.grid(row=idx, column=3, padx=10, pady=5)
            
            actions_frame = ttk.Frame(scrollable_frame)
            actions_frame.grid(row=idx, column=4, padx=10, pady=5)
            
            ttk.Button(actions_frame, text="✓", width=3,
                      command=lambda n=name: self.mark_completed(n)).pack(side=tk.LEFT, padx=2)
            ttk.Button(actions_frame, text="📊", width=3,
                      command=lambda n=name: self.show_habit_stats(n)).pack(side=tk.LEFT, padx=2)
            ttk.Button(actions_frame, text="🗑", width=3,
                      command=lambda n=name: self.delete_habit(n)).pack(side=tk.LEFT, padx=2)
            
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
    def show_categories(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()
            
        categories = self.tracker.get_habits_by_category()
        
        for category, habits in categories.items():
            frame = ttk.LabelFrame(self.main_content, text=category, padding="10")
            frame.pack(fill="x", pady=5)
            
            for habit in habits:
                habit_frame = ttk.Frame(frame)
                habit_frame.pack(fill="x", pady=2)
                
                ttk.Label(habit_frame, text=habit).pack(side=tk.LEFT)
                progress = self.tracker.habits[habit].get_goal_progress()
                progress_bar = ttk.Progressbar(habit_frame, length=200, mode='determinate')
                progress_bar['value'] = progress
                progress_bar.pack(side=tk.LEFT, padx=10)
                
    def show_statistics(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()
            
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111)
        
        habits = list(self.tracker.habits.keys())
        completion_rates = [self.tracker.get_completion_stats(habit, 'week') 
                          for habit in habits]
        
        ax.bar(habits, completion_rates)
        ax.set_title('Weekly Completion Rates')
        ax.set_ylabel('Completion Rate (%)')
        plt.xticks(rotation=45)
        
        canvas = FigureCanvasTkAgg(fig, master=self.main_content)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    def mark_completed(self, habit_name):
        self.tracker.mark_completed(habit_name)
        self.show_all_habits()
        
    def delete_habit(self, habit_name):
        if messagebox.askyesno("Confirm Delete", 
                             f"Are you sure you want to delete {habit_name}?"):
            self.tracker.delete_habit(habit_name)
            self.show_all_habits()
            
    def show_habit_stats(self, habit_name):
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Statistics - {habit_name}")
        dialog.geometry("600x400")
        dialog.transient(self.root)
        
        notebook = ttk.Notebook(dialog)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Timeline tab
        timeline_frame = ttk.Frame(notebook)
        notebook.add(timeline_frame, text="Timeline")
        
        fig1 = plt.figure(figsize=(8, 4))
        self.tracker.visualize_habit(habit_name, "timeline")
        canvas1 = FigureCanvasTkAgg(fig1, master=timeline_frame)
        canvas1.draw()
        canvas1.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Heatmap tab
        heatmap_frame = ttk.Frame(notebook)
        notebook.add(heatmap_frame, text="Heatmap")
        
        fig2 = plt.figure(figsize=(8, 4))
        self.tracker.visualize_habit(habit_name, "heatmap")
        canvas2 = FigureCanvasTkAgg(fig2, master=heatmap_frame)
        canvas2.draw()
        canvas2.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    def save_habits(self):
        self.tracker.save_to_file()
        messagebox.showinfo("Success", "Habits saved successfully!")
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = HabitTrackerGUI()
    app.run()
