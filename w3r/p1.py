"""
Puzzle 1 from w3resource Python Programming Puzzles
https://www.w3resource.com/python-exercises/puzzles/index.php
"""


def a_function(list_of_integers: list):
    # Enter a function here
    print(list_of_integers.count(19) == 2 and list_of_integers.count(5) >= 3)


def main(list_of_ints):
    # Enter main function here
    print(list_of_ints)
    a_function(list_of_ints)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main([19, 19, 15, 5, 3, 5, 5, 2])
    main([19, 15, 15, 5, 3, 3, 5, 2])
    main([19, 19, 5, 5, 5, 5, 5])

    print(f"Runtime: ---{time.time() - start_time}---")
