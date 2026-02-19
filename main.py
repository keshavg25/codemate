from ui.menus import MenuDisplay
from ui.display import OutputDisplay
from generators.function_gen import FunctionGenerator
from generators.class_gen import ClassGenerator
from generators.list_gen import ListGenerator
from analyzers.code_analyzer import CodeAnalyzer
from utils.executor import CodeExecutor
from utils.helpers import get_user_input


class CodeMateApp:

    def __init__(self):
        self.menu_display = MenuDisplay()
        self.output_display = OutputDisplay()
        self.function_gen = FunctionGenerator()
        self.class_gen = ClassGenerator()
        self.list_gen = ListGenerator()
        self.code_analyzer = CodeAnalyzer()
        self.executor = CodeExecutor()
    
    def run(self):
        self.menu_display.display_banner()
        
        while True:
            self.menu_display.display_main_menu()
            choice = get_user_input("\nEnter your choice (1-4)")
            
            if choice == '1':
                self.code_generation_mode()
            elif choice == '2':
                self.code_analysis_mode()
            elif choice == '3':
                self.show_help()
            elif choice == '4':
                print("\n" + "="*60)
                print("Thank you for using CodeMate 2.0! Happy coding!")
                print("="*60 + "\n")
                break
            else:
                print("Invalid choice! Please select 1-4.")
    
    def code_generation_mode(self):
        while True:
            self.menu_display.display_generation_menu()
            choice = get_user_input("\nEnter your choice (1-4)")
            
            if choice == '1':
                code = self.function_gen.generate()
                if code:
                    self.display_and_execute(code)
            elif choice == '2':
                code = self.class_gen.generate()
                if code:
                    self.display_and_execute(code)
            elif choice == '3':
                code = self.list_gen.generate()
                if code:
                    self.display_and_execute(code)
            elif choice == '4':
                break
            else:
                print("Invalid choice!")
    
    def display_and_execute(self, code: str):
        self.output_display.display_code(code)
        
        execute = get_user_input("\n Execute this code? (y/n)").lower()
        
        if execute == 'y':
            print("\n--- Execution Output ---")
            success, output, error = self.executor.execute_code(code)
            
            if success:
                print(output)
            else:
                print(f"Execution Error: {error}")
    
    def code_analysis_mode(self):
        print("\n--- Code Analysis & Optimization ---")
        print("Paste your Python code (type 'END' on a new line to finish):\n")
        
        code_lines = []
        while True:
            try:
                line = input()
                if line.strip() == 'END':
                    break
                code_lines.append(line)
            except EOFError:
                break
        
        code = '\n'.join(code_lines)
        
        if not code.strip():
            print(" No code provided!")
            return
        
        print("\n Analyzing code...\n")
        
        results = self.code_analyzer.analyze(code)
        
        self.output_display.display_analysis_results(
            code,
            results['issues'],
            results['complexity'],
            results['suggestions']
        )
    
    def show_help(self):
        help_text = """
╔══════════════════════════════════════════════════════════════╗
║                   CodeMate 2.0 - Help Guide                  ║
╚══════════════════════════════════════════════════════════════╝

OVERVIEW:
CodeMate 2.0 is your intelligent Python coding assistant that helps
you generate, analyze, and optimize Python code.

CODE GENERATION MODE:
   • Function Generator: Create common algorithms or custom functions
     - Factorial, Fibonacci, Palindrome checker
     - Sorting algorithms (Bubble Sort, Merge Sort)
     - Binary Search and more
   
   • Class Generator: Build Python classes with custom attributes
     - Automatically generates __init__, __str__, __repr__
   
   • List Generator: Create lists using ranges or custom elements

CODE ANALYSIS MODE:
   Paste your code to get:
   • Time complexity estimation (O(n), O(n²), etc.)
   • Detection of common issues and bad practices
   • Optimization suggestions
   
   Issues detected:
   - Missing docstrings
   - Mutable default arguments
   - Nested loops (O(n²) complexity)
   - String concatenation in loops
   - Inefficient sorting algorithms

TIPS:
   • Generated code can be executed immediately for testing
   • All generated code includes examples and documentation
   • Analysis provides actionable suggestions for improvement
   • Use complexity estimates to choose better algorithms

ALGORITHM COMPLEXITY REFERENCE:
   O(1)       - Constant time (hash lookup)
   O(log n)   - Logarithmic (binary search)
   O(n)       - Linear (simple loop)
   O(n log n) - Linearithmic (merge sort, quick sort)
   O(n²)      - Quadratic (nested loops, bubble sort)
   O(2^n)     - Exponential (recursive fibonacci)

BEST PRACTICES:
   • Always add docstrings to functions
   • Avoid mutable default arguments
   • Use built-in functions when possible
   • Choose appropriate algorithms for your data size
   • Profile before optimizing

═══════════════════════════════════════════════════════════════
"""
        print(help_text)


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    app = CodeMateApp()
    app.run()