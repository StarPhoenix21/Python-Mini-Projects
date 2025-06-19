import json
import datetime
import matplotlib.pyplot as plt
from collections import defaultdict
import calendar

class Habit:
    def __init__(self, name, category=None, goal_frequency="daily", goal_count=1):
        self.name = name
        self.category = category
        self.history = {}
        self.notes = defaultdict(str)
        self.goal_frequency = goal_frequency  # daily, weekly, monthly
        self.goal_count = goal_count  # number of times to complete per frequency

    def mark_completed(self, date=None):
        date = date or datetime.datetime.now().strftime('%Y-%m-%d')
        self.history[date] = True

    def add_note(self, date, note):
        self.notes[date] = note

    def get_streak(self):
        if not self.history:
            return 0
        
        dates = sorted(self.history.keys())
        current_date = datetime.datetime.now().date()
        last_completion = datetime.datetime.strptime(dates[-1], '%Y-%m-%d').date()
        
        # If the last completion is not today or yesterday, streak is broken
        if (current_date - last_completion).days > 1:
            return 0
            
        streak = 1
        for i in range(len(dates)-1, 0, -1):
            date1 = datetime.datetime.strptime(dates[i], '%Y-%m-%d').date()
            date2 = datetime.datetime.strptime(dates[i-1], '%Y-%m-%d').date()
            if (date1 - date2).days == 1:
                streak += 1
            else:
                break
        return streak

    def get_completion_rate(self, period="all"):
        today = datetime.datetime.now().date()
        total_days = 0
        completed_days = len(self.history)
        
        if period == "week":
            start_date = today - datetime.timedelta(days=7)
            completed_days = sum(1 for date in self.history if datetime.datetime.strptime(date, '%Y-%m-%d').date() >= start_date)
            total_days = 7
        elif period == "month":
            start_date = today.replace(day=1)
            completed_days = sum(1 for date in self.history if datetime.datetime.strptime(date, '%Y-%m-%d').date() >= start_date)
            total_days = calendar.monthrange(today.year, today.month)[1]
        elif period == "all":
            if self.history:
                start_date = datetime.datetime.strptime(min(self.history.keys()), '%Y-%m-%d').date()
                total_days = (today - start_date).days + 1
        
        return (completed_days / total_days * 100) if total_days > 0 else 0

    def get_goal_progress(self):
        today = datetime.datetime.now().date()
        completions = 0
        
        if self.goal_frequency == "daily":
            completions = 1 if today.strftime('%Y-%m-%d') in self.history else 0
        elif self.goal_frequency == "weekly":
            week_start = today - datetime.timedelta(days=today.weekday())
            completions = sum(1 for date in self.history 
                            if datetime.datetime.strptime(date, '%Y-%m-%d').date() >= week_start)
        elif self.goal_frequency == "monthly":
            month_start = today.replace(day=1)
            completions = sum(1 for date in self.history 
                            if datetime.datetime.strptime(date, '%Y-%m-%d').date() >= month_start)
        
        return (completions / self.goal_count * 100) if self.goal_count > 0 else 0

    def __repr__(self):
        return f"{self.name}: {len(self.history)} completions"

class HabitTracker:
    def __init__(self):
        self.habits = {}

    def add_habit(self, name, category=None, goal_frequency="daily", goal_count=1):
        if name not in self.habits:
            self.habits[name] = Habit(name, category, goal_frequency, goal_count)
        else:
            print("Habit already exists.")

    def delete_habit(self, name):
        if name in self.habits:
            del self.habits[name]
        else:
            print("Habit does not exist.")

    def mark_completed(self, name, date=None):
        if name in self.habits:
            self.habits[name].mark_completed(date)
        else:
            print("Habit does not exist.")

    def add_note(self, name, date, note):
        if name in self.habits:
            self.habits[name].add_note(date, note)
        else:
            print("Habit does not exist.")

    def view_habits(self):
        for habit in self.habits.values():
            print(habit)

    def get_habits_by_category(self):
        categories = defaultdict(list)
        for habit in self.habits.values():
            categories[habit.category or "Uncategorized"].append(habit.name)
        return dict(categories)

    def get_streak(self, name):
        if name in self.habits:
            return self.habits[name].get_streak()
        else:
            print("Habit does not exist.")
            return 0

    def get_completion_stats(self, name, period="all"):
        if name in self.habits:
            return self.habits[name].get_completion_rate(period)
        else:
            print("Habit does not exist.")
            return 0

    def get_goal_progress(self, name):
        if name in self.habits:
            return self.habits[name].get_goal_progress()
        else:
            print("Habit does not exist.")
            return 0

    def save_to_file(self, filename='habits.json'):
        data = {name: habit.history for name, habit in self.habits.items()}
        with open(filename, 'w') as f:
            json.dump(data, f)
        print("Habits saved to file.")

    def load_from_file(self, filename='habits.json'):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.habits = {name: Habit(name) for name in data}
                for name, history in data.items():
                    self.habits[name].history = history
            print("Habits loaded from file.")
        except FileNotFoundError:
            print("File not found. Starting with an empty habit tracker.")

    def visualize_habit(self, name, view_type="timeline"):
        if name in self.habits:
            habit = self.habits[name]
            dates = list(habit.history.keys())
            dates.sort()
            
            if not dates:
                print("No data to visualize.")
                return

            plt.figure(figsize=(12, 6))
            
            if view_type == "timeline":
                completions = [1 if date in dates else 0 for date in dates]
                plt.plot(dates, completions, marker='o')
                plt.title(f'Habit Timeline: {name}')
                plt.xlabel('Date')
                plt.ylabel('Completion')
            
            elif view_type == "heatmap":
                # Create weekly heatmap
                weeks = len(dates) // 7 + 1
                data = [[0] * 7 for _ in range(weeks)]
                
                for date in dates:
                    dt = datetime.datetime.strptime(date, '%Y-%m-%d')
                    week = (dt.date() - datetime.datetime.strptime(dates[0], '%Y-%m-%d').date()).days // 7
                    weekday = dt.weekday()
                    if week < weeks and weekday < 7:
                        data[week][weekday] = 1
                
                plt.imshow(data, cmap='YlOrRd')
                plt.title(f'Habit Heatmap: {name}')
                plt.xlabel('Day of Week')
                plt.ylabel('Week')
                plt.colorbar(label='Completion')
                plt.xticks(range(7), ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
            
            plt.tight_layout()
            plt.show()
        else:
            print("Habit does not exist.")

def main():
    tracker = HabitTracker()
    tracker.load_from_file()
    
    while True:
        print("\nHabit Tracker")
        print("1. Add Habit")
        print("2. Delete Habit")
        print("3. Mark Habit as Completed")
        print("4. View All Habits")
        print("5. Save Habits to File")
        print("6. Load Habits from File")
        print("7. Visualize Habit")
        print("8. Add Note to Habit")
        print("9. View Habit Statistics")
        print("10. View Habits by Category")
        print("11. View Goal Progress")
        print("12. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter habit name: ")
            category = input("Enter habit category (or press Enter to skip): ")
            frequency = input("Enter goal frequency (daily/weekly/monthly) [daily]: ") or "daily"
            count = input("Enter goal count [1]: ") or "1"
            tracker.add_habit(name, category or None, frequency, int(count))
        elif choice == '2':
            name = input("Enter habit name to delete: ")
            tracker.delete_habit(name)
        elif choice == '3':
            name = input("Enter habit name: ")
            date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
            tracker.mark_completed(name, date if date else None)
        elif choice == '4':
            tracker.view_habits()
        elif choice == '5':
            tracker.save_to_file()
        elif choice == '6':
            tracker.load_from_file()
        elif choice == '7':
            name = input("Enter habit name to visualize: ")
            view_type = input("Enter view type (timeline/heatmap) [timeline]: ") or "timeline"
            tracker.visualize_habit(name, view_type)
        elif choice == '8':
            name = input("Enter habit name: ")
            date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
            note = input("Enter note: ")
            tracker.add_note(name, date if date else None, note)
        elif choice == '9':
            name = input("Enter habit name: ")
            print(f"\nStreak: {tracker.get_streak(name)} days")
            print(f"Week completion rate: {tracker.get_completion_stats(name, 'week'):.1f}%")
            print(f"Month completion rate: {tracker.get_completion_stats(name, 'month'):.1f}%")
            print(f"Overall completion rate: {tracker.get_completion_stats(name, 'all'):.1f}%")
        elif choice == '10':
            categories = tracker.get_habits_by_category()
            for category, habits in categories.items():
                print(f"\n{category}:")
                for habit in habits:
                    print(f"  - {habit}")
        elif choice == '11':
            name = input("Enter habit name: ")
            progress = tracker.get_goal_progress(name)
            print(f"Current goal progress: {progress:.1f}%")
        elif choice == '12':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()