# CodeMate 2.0

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> Your Intelligent Code Assistant for Python Development

CodeMate 2.0 is a comprehensive command-line tool designed to accelerate Python development by providing intelligent code generation, analysis, and optimization capabilities. Whether you're a beginner learning Python or an experienced developer looking to prototype quickly, CodeMate helps you write better code faster.

## Features

### Code Generation
- **Function Generator**: Create common algorithms and custom functions
  - Pre-built templates: Factorial, Fibonacci, Palindrome, Bubble Sort, Merge Sort, Binary Search
  - Custom function scaffolding with proper structure
- **Class Generator**: Automatically generate Python classes with:
  - `__init__` method with parameters
  - `__str__` and `__repr__` methods
  - Comprehensive docstrings
- **List Generator**: Create lists using ranges or custom elements

### Code Analysis & Optimization
- **Issue Detection**: Identifies common Python anti-patterns and bugs
  - Missing docstrings
  - Mutable default arguments
  - Nested loops (potential O(n²) complexity)
  - String concatenation in loops
  - Inefficient sorting algorithms
- **Complexity Estimation**: Analyzes code to estimate time complexity
  - O(1), O(log n), O(n), O(n log n), O(n²), O(n³), O(2^n)
- **Optimization Suggestions**: Provides actionable recommendations for code improvement

### Code Execution
- **Safe Execution**: Run generated code in a sandboxed environment
- **Output Capture**: View execution results and error messages
- **Interactive Testing**: Test your code immediately after generation

### Built-in Documentation
- Comprehensive help system
- Algorithm complexity reference
- Best practices guide
- Usage examples

## Installation

### Prerequisites
- Python 3.6 or higher

### Install from Source
```bash
# Clone the repository
git clone https://github.com/yourusername/codemate.git
cd codemate

# Run the application
python main.py
```

### No External Dependencies
CodeMate uses only Python's standard library, so no additional packages are required.

## Usage

### Starting the Application
```bash
python main.py
```

### Main Menu Options

1. **Code Generation Mode**
   - Generate functions, classes, and lists
   - Choose from pre-built templates or create custom code

2. **Code Analysis & Optimization Mode**
   - Paste your Python code for analysis
   - Get detailed reports on issues and complexity
   - Receive optimization suggestions

3. **Help & Documentation**
   - Access built-in help guide
   - Learn about algorithm complexities
   - View best practices

4. **Exit**
   - Close the application

### Example Workflow

```
Welcome to CodeMate 2.0 - Your Intelligent Code Assistant
============================================================
         Generate | Analyze | Optimize Python Code
============================================================

Main Menu:
1. Code Generation Mode
2. Code Analysis & Optimization Mode
3. Help & Documentation
4. Exit

Enter your choice (1-4): 1

Code Generation Mode:
1. Generate Function
2. Generate Class
3. Generate List
4. Back to Main Menu

Enter your choice (1-4): 1

--- Function Generator ---

Available templates:
1. Factorial
2. Fibonacci
3. Palindrome
4. Bubble Sort
5. Merge Sort
6. Binary Search
7. Custom Function

Select function type: 1
```

## Examples

### Generating a Factorial Function
```python
def factorial(n):
    """
    Calculate the factorial of a number.
    Time Complexity: O(n)
    """
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
print(f"Factorial of 5: {factorial(5)}")
print(f"Factorial of 7: {factorial(7)}")
```

### Code Analysis Example
```
ANALYSIS RESULTS
============================================================

Estimated Time Complexity: O(n²)

Issues Found: 2

  HIGH:
     Line 5: Nested loops detected - potential O(n²) complexity
     Line 12: Bubble sort pattern detected - consider using sort() or efficient algorithms

Optimization Suggestions:
  • Use dictionary/set lookups instead of nested loops
  • Replace bubble sort with sorted() or list.sort() (O(n log n))
  • For custom sorting, use merge sort or quick sort
  • Current complexity is O(n²) - consider optimization
```

## Project Structure

```
codemate/
├── main.py                 # Application entry point
├── config.py              # Configuration and constants
├── analyzers/             # Code analysis modules
│   ├── __init__.py
│   ├── code_analyzer.py   # Main analyzer orchestrator
│   ├── complexity.py      # Time complexity estimation
│   ├── issue_detector.py  # Issue detection logic
│   └── approach1/         # Alternative analysis approaches
│       ├── __init__.py
│       └── complexity_string.py
├── generators/            # Code generation modules
│   ├── __init__.py
│   ├── algorithms.py      # Algorithm templates
│   ├── class_gen.py       # Class generator
│   ├── function_gen.py    # Function generator
│   └── list_gen.py        # List generator
├── ui/                    # User interface modules
│   ├── __init__.py
│   ├── display.py         # Output formatting
│   └── menus.py           # Menu display
└── utils/                 # Utility functions
    ├── __init__.py
    ├── executor.py        # Safe code execution
    └── helpers.py         # Input validation and formatting
```

## Technical Details

### Complexity Analysis
CodeMate uses Abstract Syntax Tree (AST) parsing to analyze Python code structure and estimate algorithmic complexity. The analyzer detects:

- Loop nesting levels
- Recursive function calls
- Data structure operations
- Algorithm patterns

### Safe Code Execution
Generated and analyzed code is executed in a controlled environment using Python's `exec()` with restricted globals to prevent system access.

### Modular Architecture
The application follows a modular design with clear separation of concerns:
- **Generators**: Handle code creation logic
- **Analyzers**: Perform static code analysis
- **UI**: Manage user interaction and display
- **Utils**: Provide shared utilities

## Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/codemate.git
cd codemate

# Make your changes
# Test thoroughly

# Submit a pull request
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Python's standard library
- Inspired by the need for accessible code generation tools
- Thanks to the Python community for excellent documentation

## Support

If you encounter any issues or have suggestions for improvement, please:

1. Check the built-in help system (`python main.py` → Help)
2. Open an issue on GitHub
3. Review the code analysis suggestions for your own code

---

**Happy Coding with CodeMate 2.0!**</content>
<parameter name="filePath">d:\DAU\1st Sem\assignment\python\project\codemate\README.md