from generators.algorithms import AlgorithmTemplates
from utils.helpers import get_user_input, validate_identifier


class FunctionGenerator:
    
    def __init__(self):
        self.algorithms = {
            'factorial': AlgorithmTemplates.factorial,
            'fibonacci': AlgorithmTemplates.fibonacci,
            'palindrome': AlgorithmTemplates.palindrome,
            'bubble_sort': AlgorithmTemplates.bubble_sort,
            'merge_sort': AlgorithmTemplates.merge_sort,
            'binary_search': AlgorithmTemplates.binary_search
        }
    
    def generate(self):
        print("\n--- Function Generator ---")
        print("\nAvailable templates:")
        
        algo_list = list(self.algorithms.keys())
        for i, algo in enumerate(algo_list, 1):
            print(f"{i}. {algo.replace('_', ' ').title()}")
        print(f"{len(algo_list) + 1}. Custom Function")
        
        choice = get_user_input("\nSelect function type")
        
        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(algo_list):
                algo_name = algo_list[choice_num - 1]
                return self.algorithms[algo_name]()
            elif choice_num == len(algo_list) + 1:
                return self.generate_custom()
            else:
                print("Invalid choice!")
                return None
        except (ValueError, TypeError):
            print("Please enter a valid number!")
            return None
    
    def generate_custom(self):
        func_name = get_user_input("Enter function name")
        
        if not validate_identifier(func_name):
            print("Invalid function name!")
            return None
        
        params = get_user_input("Enter parameters (comma-separated)", "")
        docstring = get_user_input("Enter brief description", "Custom function")
        
        return f'''def {func_name}({params}):
    """
    {docstring}
    """
    # TODO: Implement function logic
    pass

# Example usage
# result = {func_name}()
# print(result)'''