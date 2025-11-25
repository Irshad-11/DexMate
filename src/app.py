# src/app.py
import sys
import argparse
from src.pokemon_api import get_pokemon_data, suggest_names


RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
MAGENTA = "\033[1;35m"

def pretty_print(p):
    print(f"{CYAN}Name:{RESET} {BOLD}{p['name'].title()}{RESET}")
    print(f"{YELLOW}Height:{RESET} {p['height']}")
    print(f"{YELLOW}Weight:{RESET} {p['weight']}")
    print(f"{MAGENTA}Types:{RESET} {', '.join(p['types']) if p['types'] else 'N/A'}")
    print(f"{MAGENTA}Abilities:{RESET} {', '.join(p['abilities']) if p['abilities'] else 'N/A'}")
    print(f"{GREEN}Base Stats:{RESET}")
    for stat, val in p['base_stats'].items():
        print(f"  {stat.title():12}{RESET} {val}")

def main():
    parser = argparse.ArgumentParser(prog="pokemon-console", description="Get Pokémon info from PokéAPI")
    parser.add_argument("name", nargs="?", help="Pokémon name (e.g. pikachu)")
    args = parser.parse_args()

    if not args.name:
        try:
            name = input("Enter pokemon name: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            sys.exit(0)
    else:
        name = args.name

    print(f"{BOLD}Fetching info for:{RESET} {name}")
    data = get_pokemon_data(name)
    if data:
        pretty_print(data)
    else:
        print(f"{RED}Invalid Pokémon name or error fetching data: '{name}'{RESET}")
        suggestions = suggest_names(prefix=name)
        print(f"{BOLD}Try these names:{RESET} {', '.join(suggestions)}")

if __name__ == "__main__":
    main()
