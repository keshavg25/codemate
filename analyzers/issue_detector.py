import ast
from typing import List, Dict


class IssueDetector:
    
    @staticmethod
    def detect_issues(code: str) -> List[Dict]:
        issues = []
        
        try:
            tree = ast.parse(code)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    if not ast.get_docstring(node):
                        issues.append({
                            'type': 'Missing Docstring',
                            'line': node.lineno,
                            'message': f"Function '{node.name}' lacks a docstring",
                            'severity': 'Medium'
                        })
                    
                    for default in node.args.defaults:
                        if isinstance(default, (ast.List, ast.Dict, ast.Set)):
                            issues.append({
                                'type': 'Mutable Default Argument',
                                'line': node.lineno,
                                'message': f"Function '{node.name}' uses mutable default argument",
                                'severity': 'High'
                            })
                
                if isinstance(node, ast.For):
                    for child in ast.walk(node):
                        if child != node and isinstance(child, ast.For):
                            issues.append({
                                'type': 'Nested Loop',
                                'line': node.lineno,
                                'message': 'Nested loops detected - potential O(n²) complexity',
                                'severity': 'High'
                            })
                            break
            
            lines = code.split('\n')
            for i, line in enumerate(lines, 1):
                if 'for' in line and '+=' in line and ("'" in line or '"' in line):
                    issues.append({
                        'type': 'String Concatenation in Loop',
                        'line': i,
                        'message': 'String concatenation in loop - use join() instead',
                        'severity': 'Medium'
                    })
            
          
            if IssueDetector._detect_bubble_sort(code):
                issues.append({
                    'type': 'Inefficient Algorithm',
                    'line': 0,
                    'message': 'Bubble sort pattern detected - consider using sort() or efficient algorithms',
                    'severity': 'High'
                })
        
        except SyntaxError as e:
            issues.append({
                'type': 'Syntax Error',
                'line': e.lineno or 0,
                'message': f'Syntax error: {e.msg}',
                'severity': 'Critical'
            })
        
        return issues
    
    @staticmethod
    def _detect_bubble_sort(code: str) -> bool:
        has_nested_loop = 'for' in code and code.count('for') >= 2
        has_swap = ('[i]' in code and '[j]' in code) or ('swap' in code.lower())
        return has_nested_loop and has_swap