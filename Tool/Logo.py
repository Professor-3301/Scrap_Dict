import colorama
from colorama import Fore, Style

def print_colorful_logo():
    colorama.init(autoreset=True)  # Initialize colorama for cross-platform ANSI color support

    logo = f"""
{Fore.BLUE}  _________                         ________  .__        __   
{Fore.BLUE} /   _____/ ________________  ______\______ \ |__| _____/  |_ 
{Fore.CYAN} \_____  \_/ ___\_  __ \__  \ \____ \|    |  \|  |/ ___\   __\\
{Fore.CYAN} /        \  \___|  | \// __ \|  |_> >    `   \  \  \___|  |  
{Fore.RED} /_______  /\___  >__|  (____  /   __/_______  /__|\___  >__|  
{Fore.RED}        \/     \/           \/|__|          \/        \/      
    """
    print(f"{Fore.GREEN}{Style.BRIGHT}{logo}")
    return logo
def print_normal_logo():
    colorama.init(autoreset=True)  # Initialize colorama for cross-platform ANSI color support

    logo = f"""
  _________                         ________  .__        __   
 /   _____/ ________________  ______\______ \ |__| _____/  |_ 
 \_____  \_/ ___\_  __ \__  \ \____ \|    |  \|  |/ ___\   __\\
 /        \  \___|  | \// __ \|  |_> >    `   \  \  \___|  |  
 /_______  /\___  >__|  (____  /   __/_______  /__|\___  >__|  
{Fore.RED}        \/     \/           \/|__|          \/        \/      
    """
    print(f"{Fore.GREEN}{Style.BRIGHT}{logo}")
    return logo

if __name__ == "__main__":
    print_colorful_logo()

