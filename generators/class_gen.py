from utils.helpers import get_user_input, validate_identifier


class ClassGenerator:
    
    def generate(self):
        print("\n--- Class Generator ---")
        
        class_name = get_user_input("Enter class name")
        
        if not validate_identifier(class_name):
            print("Invalid class name!")
            return None
        
        attrs = get_user_input("Enter attributes (comma-separated)")
        attr_list = [attr.strip() for attr in attrs.split(',') if attr.strip()]
        
        if not attr_list:
            print("At least one attribute is required!")
            return None
        
        
        for attr in attr_list:
            if not validate_identifier(attr):
                print(f"Invalid attribute name: {attr}")
                return None
        
        params = ', '.join(attr_list)
        assignments = '\n        '.join([f"self.{attr} = {attr}" for attr in attr_list])
        str_repr = ', '.join([f"{attr}={{self.{attr}}}" for attr in attr_list])
        example_values = ', '.join([f'"{attr}_value"' for attr in attr_list])
        
        return f'''class {class_name}:
    """
    A class representing {class_name}.
    """
    
    def __init__(self, {params}):
        """Initialize {class_name} with given attributes."""
        {assignments}
    
    def __str__(self):
        """String representation of {class_name}."""
        return f"{class_name}({str_repr})"
    
    def __repr__(self):
        """Official string representation."""
        return self.__str__()

# Example usage
obj = {class_name}({example_values})
print(obj)'''
