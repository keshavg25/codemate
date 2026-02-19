from utils.helpers import get_user_input


class ListGenerator:
    
    def generate(self):
        print("\n--- List Generator ---")
        print("1. Range-based list")
        print("2. Custom elements list")
        
        choice = get_user_input("Enter choice")
        
        if choice == '1':
            return self.generate_range_list()
        elif choice == '2':
            return self.generate_custom_list()
        else:
            print("Invalid choice!")
            return None
    
    def generate_range_list(self):
        start = get_user_input("Enter start value", "0")
        end = get_user_input("Enter end value")
        step = get_user_input("Enter step", "1")
        
        if not end:
            print("End value is required!")
            return None
        
        return f'''# Generate list using range
my_list = list(range({start}, {end}, {step}))
print(f"Generated list: {{my_list}}")
print(f"Length: {{len(my_list)}}")
print(f"Sum: {{sum(my_list)}}")'''
    
    def generate_custom_list(self):
        elements = get_user_input("Enter list elements (comma-separated)")
        
        if not elements:
            print("At least one element is required!")
            return None
        
        return f'''# Custom list
my_list = [{elements}]
print(f"Generated list: {{my_list}}")
print(f"Length: {{len(my_list)}}")
print(f"Data types: {{[type(x).__name__ for x in my_list]}}")'''