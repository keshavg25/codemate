def get_user_input(prompt: str, default: str = None) -> str:
    """Get user input with optional default value"""
    if default:
        prompt = f"{prompt} (default: {default}): "
    else:
        prompt = f"{prompt}: "
    
    value = input(prompt).strip()
    return value if value else default


def validate_identifier(name: str) -> bool:
    """Validate if string is a valid Python identifier"""
    return name.isidentifier()


def print_separator(char='=', length=60):
    """Print a separator line"""
    print(char * length)


def print_section_header(title: str):
    """Print a formatted section header"""
    print_separator()
    print(f"  {title}")
    print_separator()