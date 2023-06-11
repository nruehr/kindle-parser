import clipboard
import webbrowser
import time
from pynput.keyboard import Key, Controller

search_url = "https://jisho.org/search/"


def read_input():
    """Read input file and store the contents."""
    with open('input.txt', encoding='utf-8') as input:
        input_raw = input.read()
    return input_raw


def parse_input(input_raw: str):
    """Parse raw input and split it into titles and sentences."""
    global line_count 
    line_count = input_raw.count('\n') + 1
    lines_list = input_raw.splitlines()
    return lines_list


def process_lines(lines_list: str):
    """
    Go through every line.
    1. Show sentence if it's a sentence line.
    2. Copy it to the clipboard.
    3. Open a Jisho search.
    
    """
    keyboard = Controller()
    
    for line in range(1, line_count):
        # Choose only lines with sentences (line 2, 5, 8, etc.).
        if (line == 1) | ((line-1) % 3 == 0):

            # Output sentence and source.
            print(lines_list[line],f"\nfrom: {lines_list[line - 1]}\n")

            # Send the sentence to the clipboard.
            clipboard.copy(lines_list[line])

            # Start a Jisho search.
            url = search_url + lines_list[line]
            webbrowser.open_new_tab(url)
            time.sleep(0.5)
            keyboard.press(Key.alt_l)
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            keyboard.release(Key.alt_l)

            # Wait for user input to continue.
            input("...\n")


if __name__ == "__main__":
    input_raw = read_input()
    lines_list = parse_input(input_raw)
    process_lines(lines_list)
    
    pass