import ast


class ComplexityEstimator:
    
    @staticmethod
    def estimate(code: str) -> str:
        try:
            tree = ast.parse(code)
            
            if ComplexityEstimator._has_recursion(tree, code):
                if 'merge' in code.lower() or 'quick' in code.lower():
                    return 'O(n log n)'
                return 'O(2^n)'  
            
            linear_depth, log_depth = ComplexityEstimator._calculate_loop_complexity(tree)
            
            if linear_depth == 0 and log_depth == 0:
                return 'O(1)'
            
            parts = []
            if linear_depth > 0:
                parts.append('n' if linear_depth == 1 else f'n^{linear_depth}')
            if log_depth > 0:
                parts.append('log n' if log_depth == 1 else f'(log n)^{log_depth}')
            
            return f"O({' '.join(parts)})"
        
        except Exception as e:
            return 'Unable to determine'
    
    @staticmethod
    def _calculate_loop_complexity(node) -> tuple[int, int]:

        max_linear = 0
        max_log = 0
        
        current_linear = 0
        current_log = 0
        
        if isinstance(node, (ast.For, ast.While)):
            is_log = False
            if isinstance(node, ast.While):
                is_log = ComplexityEstimator._is_logarithmic_loop(node)
            
            if is_log:
                current_log = 1
            else:
                current_linear = 1
        
        
        child_max_linear = 0
        child_max_log = 0
        
        children_to_visit = []
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef)):
            children_to_visit = node.body
        elif isinstance(node, (ast.For, ast.AsyncFor, ast.While)):
            children_to_visit = node.body
        elif isinstance(node, ast.If):
            children_to_visit = node.body + node.orelse
        elif isinstance(node, (ast.Try)):
            children_to_visit = node.body + node.handlers + node.finalbody
        elif isinstance(node, ast.ExceptHandler):
            children_to_visit = node.body
        elif isinstance(node, ast.With):
            children_to_visit = node.body
        else:
            children_to_visit = list(ast.iter_child_nodes(node))

        for child in children_to_visit:
            c_lin, c_log = ComplexityEstimator._calculate_loop_complexity(child)
            
            if c_lin > child_max_linear:
                child_max_linear = c_lin
                child_max_log = c_log
            elif c_lin == child_max_linear:
                child_max_log = max(child_max_log, c_log)
        
        return current_linear + child_max_linear, current_log + child_max_log

    @staticmethod
    def _is_logarithmic_loop(node: ast.While) -> bool:
        try:
            # Extract loop variables from condition
            # Simple case: while k < n
            if not isinstance(node.test, ast.Compare):
                return False
                
            # Look for multiplicative updates in the body
            # k = k * 2, k *= 2, k = k / 2, k /= 2
            for child in ast.walk(node):
                if isinstance(child, ast.AugAssign):
                    if isinstance(child.op, (ast.Mult, ast.Div, ast.FloorDiv)):
                        return True
                elif isinstance(child, ast.Assign):
                    # Check for k = k * 2 pattern
                    if isinstance(child.value, ast.BinOp) and isinstance(child.value.op, (ast.Mult, ast.Div, ast.FloorDiv)):
                        return True
            return False
        except:
            return False

    @staticmethod
    def _has_recursion(tree, code: str) -> bool:
        func_names = set()
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_names.add(node.name)
                
                for child in ast.walk(node):
                    if isinstance(child, ast.Call):
                        if isinstance(child.func, ast.Name) and child.func.id == node.name:
                            return True
        
        return False