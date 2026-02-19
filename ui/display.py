from typing import List, Dict
from utils.helpers import print_separator


class OutputDisplay:
    
    @staticmethod
    def display_code(code: str, title: str = "Generated Code"):
        print_separator()
        print(f" {title}:")
        print_separator()
        print(code)
        print_separator()
    
    @staticmethod
    def display_analysis_results(code: str, issues: List[Dict], 
                                 complexity: str, suggestions: List[str]):
        print_separator()
        print(" ANALYSIS RESULTS")
        print_separator()
        
        
        print(f"\n  Estimated Time Complexity: {complexity}")
        
        
        print(f"\n Issues Found: {len(issues)}")
        
        if issues:
            OutputDisplay._display_issues_by_severity(issues)
        else:
            print("  No issues detected!")
        
    
        print(f"\n Optimization Suggestions:")
        for suggestion in suggestions:
            print(f"  {suggestion}")
        
        print("\n" + "="*60)
    
    @staticmethod
    def _display_issues_by_severity(issues: List[Dict]):
        critical = [i for i in issues if i['severity'] == 'Critical']
        high = [i for i in issues if i['severity'] == 'High']
        medium = [i for i in issues if i['severity'] == 'Medium']
        
        if critical:
            print("\n  CRITICAL:")
            for issue in critical:
                print(f"     Line {issue['line']}: {issue['message']}")
        
        if high:
            print("\n  HIGH:")
            for issue in high:
                print(f"     Line {issue['line']}: {issue['message']}")
        
        if medium:
            print("\n  MEDIUM:")
            for issue in medium:
                print(f"     Line {issue['line']}: {issue['message']}")