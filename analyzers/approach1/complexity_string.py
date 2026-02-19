import re

def remove_comments_and_strings(code: str) -> str:
    code = re.sub(r"#.*", "", code)
    code = re.sub(r"'''(.|\n)*?'''", "", code)
    code = re.sub(r'"""(.|\n)*?"""', "", code)
    code = re.sub(r'".*?"', "", code)
    code = re.sub(r"'.*?'", "", code)
    return code

def string_based_complexity(code: str) -> dict:
    clean = remove_comments_and_strings(code)

    metrics = {
        "for_loops": len(re.findall(r"\bfor\b", clean)),
        "while_loops": len(re.findall(r"\bwhile\b", clean)),
        "if_statements": len(re.findall(r"\bif\b", clean)),
        "elif_statements": len(re.findall(r"\belif\b", clean)),
        "else_statements": len(re.findall(r"\belse\b", clean)),
        "function_defs": len(re.findall(r"\bdef\b", clean)),
    }

    metrics["complexity_score"] = (
        metrics["for_loops"]
        + metrics["while_loops"]
        + metrics["if_statements"]
        + metrics["elif_statements"]
        + metrics["function_defs"]
    )

    return metrics
