from typing import List, Dict
from analyzers.issue_detector import IssueDetector
from analyzers.complexity import ComplexityEstimator


class CodeAnalyzer:
    
    def __init__(self):
        self.issue_detector = IssueDetector()
        self.complexity_estimator = ComplexityEstimator()
    
    def analyze(self, code: str) -> Dict:
        issues = self.issue_detector.detect_issues(code)
        complexity = self.complexity_estimator.estimate(code)
        suggestions = self.generate_suggestions(issues, complexity)
        
        return {
            'issues': issues,
            'complexity': complexity,
            'suggestions': suggestions
        }
    
    def generate_suggestions(self, issues: List[Dict], complexity: str) -> List[str]:

        suggestions = []
        
        for issue in issues:
            if issue['type'] == 'Nested Loop':
                suggestions.append("• Use dictionary/set lookups instead of nested loops")
            
            elif issue['type'] == 'Inefficient Algorithm':
                suggestions.append("• Replace bubble sort with sorted() or list.sort() (O(n log n))")
                suggestions.append("• For custom sorting, use merge sort or quick sort")
            
            elif issue['type'] == 'String Concatenation in Loop':
                suggestions.append("• Use ''.join(list) instead of += for strings")
            
            elif issue['type'] == 'Mutable Default Argument':
                suggestions.append("• Use None as default and create mutable object inside function")
            
            elif issue['type'] == 'Missing Docstring':
                suggestions.append("• Add docstrings to improve documentation")
        
        if complexity in ['O(n²)', 'O(n^3)']:
            suggestions.append(f"• Current complexity is {complexity} - consider optimization")
            suggestions.append("• Complexity is high")
        
        suggestions = list(dict.fromkeys(suggestions))
        
        return suggestions if suggestions else ["✓ No major optimization opportunities detected"]