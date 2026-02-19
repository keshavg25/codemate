import sys
from io import StringIO


class CodeExecutor:
    """Execute Python code safely and capture output"""
    
    @staticmethod
    def execute_code(code: str) -> tuple:
        """
        Execute Python code and return success status and output
        
        Returns:
            tuple: (success: bool, output: str, error: str)
        """
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        redirected_output = StringIO()
        redirected_error = StringIO()
        
        sys.stdout = redirected_output
        sys.stderr = redirected_error
        
        try:
            exec(code, {'__name__': '__main__'})
            success = True
            error = None
        except Exception as e:
            success = False
            error = str(e)
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr
        
        output = redirected_output.getvalue()
        error_output = redirected_error.getvalue()
        
        return success, output, error or error_output