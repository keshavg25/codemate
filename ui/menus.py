from config import (
    APP_NAME, APP_DESCRIPTION, VERSION,
    MAIN_MENU_OPTIONS, GENERATION_MENU_OPTIONS
)
from utils.helpers import print_separator


class MenuDisplay:
    
    @staticmethod
    def display_banner():
        print("\n" + "="*60)
        print(f"          {APP_NAME} - {APP_DESCRIPTION}")
        print("="*60)
        print("         Generate | Analyze | Optimize Python Code")
        print("="*60 + "\n")
    
    @staticmethod
    def display_main_menu():
        print("\n Main Menu:")
        for key, value in MAIN_MENU_OPTIONS.items():
            icon = {'1': '', '2': '', '3': '', '4': ''}
            print(f"{key}. {icon.get(key, '•')} {value}")
    
    @staticmethod
    def display_generation_menu():
        print("\n Code Generation Mode:")
        for key, value in GENERATION_MENU_OPTIONS.items():
            print(f"{key}. {value}")