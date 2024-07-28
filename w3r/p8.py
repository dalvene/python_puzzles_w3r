"""
Puzzle 8 from w3resource Python Programming Puzzles
https://www.w3resource.com/python-exercises/puzzles/index.php
Hard without re. Easy with re.
"""

import re


def a_function(input_string: str):
    # Enter a function here
    word_list = re.findall(r"\w+", input_string)
    sep_list = re.findall(r",? ", input_string)
    print([word_list, sep_list])


def main(input_string):
    # Enter main function here
    print(input_string)
    a_function(input_string)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main("W3resource Python, Exercises.")
    main("The dance, held in the school gym, ended at midnight.")
    main("The colors in my studyroom are blue, green, and yellow.")
    print(f"Runtime: ---{time.time() - start_time}---")
