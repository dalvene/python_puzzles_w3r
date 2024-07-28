"""
Puzzle 10 from w3resource Python Programming Puzzles
https://www.w3resource.com/python-exercises/puzzles/index.php

NOTE: Maybe come back to this one later to streamline.
"""


def a_function(input_string: str):
    # Enter a function here
    bracket_collection = ""
    output_brackets = []
    open_brackets = 0
    for n in input_string:
        if n == "(":
            open_brackets += 1
            bracket_collection += n
        elif n == ")":
            open_brackets -= 1
            bracket_collection += n
            if open_brackets == 0:
                output_brackets.append(bracket_collection)
                bracket_collection = ""
    print(output_brackets)


def main(input_string):
    # Enter main function here
    print(input_string)
    a_function(input_string)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main("( ()) ((()()())) (()) ()")
    main("() (( ( )() ( )) ) ( ())")
    print(f"Runtime: ---{time.time() - start_time}---")
