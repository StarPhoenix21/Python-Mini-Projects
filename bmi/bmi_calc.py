class Bmi:
    def __init__(self):
        self.user_weight = None
        self.user_height = None
        self.user_choice = None
        self.bmi_index =  None
    
    def input_validation(self):
        while True:
            try:
                user_height, user_weight = map(float,input().split())
                if user_height > 0 and user_weight > 0:
                    return user_height,user_weight
                else:
                    print("Invalid Input: Height and weight must be positive numbers.")
            except ValueError:
                print("Invalid Input: Please enter numeric values for height and weight.")
    
    def selection(self):
        while True:
            try:
                user_choice = int(input("Select the Conversion\n1:Centimeter/Pounds\n2:Meter/Kilograms -> "))
                if 1<= user_choice <=2:
                    return user_choice
                else:
                    print("Invalid Choice: Please select 1 or 2.")
            except ValueError:
                print("Invalid Input: Please enter a numeric value.")
    
    def conversion(self,choice,height,weight):
        if choice == 1: # Convert from Centimeters/Pounds to Meters/Kilograms
            height = height * 0.01 # Convert cm to meters
            weight = weight * 0.4535924 # Convert pounds to kilograms
            return height,weight
        else:
            return height,weight
    
    def bmi_calc(self,height,weight):
        return round((weight/(height*height)),2)
    
    def bmi_map(self,result):
        bmi_categories = {
            "Very severely underweight": (0, 15),
            "Severely underweight": (15, 16),
            "Underweight": (16, 18.5),
            "Normal (healthy weight)": (18.5, 25),
            "Overweight": (25, 30),
            "Moderately obese": (30, 35),
            "Severely obese": (35, 40),
            "Very severely obese": (40, float('inf'))  # 'inf' represents "Over 40"
        }
        for category, (lower,higher) in bmi_categories.items():
            if lower <= result < higher:
                return category
        return "Invalid BMI value"
        
    def bmi_table(self, bmi_value):
        # Define the BMI categories and their ranges
        bmi_categories = [
            ("Very severely underweight", 0, 15),
            ("Severely underweight", 15, 16),
            ("Underweight", 16, 18.5),
            ("Normal (healthy weight)", 18.5, 25),
            ("Overweight", 25, 30),
            ("Moderately obese", 30, 35),
            ("Severely obese", 35, 40),
            ("Very severely obese", 40, float('inf'))
        ]

        # Create the BMI table with an arrow pointing to the user's category
        table = []
        for category, lower, upper in bmi_categories:
            range_str = f"{lower} - {upper}" if upper != float('inf') else f"{lower}+"
            arrow = "-->" if lower <= bmi_value < upper else "   "
            table.append(f"{arrow} {category.ljust(25)} | Range: {range_str}")

        # Join the table rows into a single string
        return "\n".join(table)
    
    def user_detail(self):
        print("======================================")
        print("Welcome to the BMI App!")
        print("======================================")
        self.user_choice = self.selection()
        print("Please Enter your Height and weight")
        self.user_height, self.user_weight = self.input_validation()
        self.user_height, self.user_weight = self.conversion(self.user_choice,self.user_height, self.user_weight)
        result = self.bmi_calc(self.user_height, self.user_weight)
        print("=====================================================")
        #print(f"BMI index value -> {round(result,2)}")
        self.bmi_index = self.bmi_map(result)
        print(f"You fall under the category of : {self.bmi_index}")
        print("=====================================================")
        print("\nBMI Category Table:")
        # Generate and display the BMI table
        bmi_table = self.bmi_table(result)
        print(bmi_table)
        print("=====================================================")
    
    
if __name__ == "__main__":
    bmi_calculator = Bmi()
    bmi_calculator.user_detail()