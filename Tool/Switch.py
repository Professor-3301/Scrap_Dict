import colorama
from colorama import Fore, Style
from scrape_functions import *
from Output import *

def print_colorful_menu():
    colorama.init(autoreset=True)  # Initialize colorama for cross-platform ANSI color support

    menu = f"""
    {Fore.YELLOW}{Style.BRIGHT}Select Scraping Option:
    {Fore.BLUE}1. Image Scraping
    2. Link Scraping
    3. HTML Scraping
    4. Metadata
    0. Exit
    """

    print(menu)

def select_scraping_option(url):
    while True:
        print_colorful_menu()
        user_choice = input(f"{Fore.YELLOW}{Style.BRIGHT}Enter your choice (0-3): {Fore.RESET}")

        if user_choice == '1':
            print(f"{Fore.RED}{Style.BRIGHT}You selected Image Scraping!")
            result = scrape_images(url)
        elif user_choice == '2':
            print(f"{Fore.RED}{Style.BRIGHT}You selected Link Scraping!")
            result = scrape_hyperlinks(url)
            Save_All(user_choice,result)
        elif user_choice == '3':
            print(f"{Fore.RED}{Style.BRIGHT}You selected HTML Scraping!")
            result = scrape_html(url)
            Save_All(user_choice)
        elif user_choice == '4':
            print(f"{Fore.RED}{Style.BRIGHT}You selected Metadata Scraping!")
            result = scrape_metadata(url)
            Save_All(user_choice)
        elif user_choice == '0':
            print(f"{Fore.GREEN}{Style.BRIGHT}Exiting the program. Goodbye!")
            break
        else:
            print(f"{Fore.YELLOW}{Style.BRIGHT}Invalid choice. Please enter a valid option.")
        return result

if __name__ == "__main__":
    select_scraping_option()
