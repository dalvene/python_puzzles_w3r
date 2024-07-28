"""
Puzzle 2 from w3resource Python Programming Puzzles
https://www.w3resource.com/python-exercises/puzzles/index.php
"""


def a_function(list_of_integers: list):
    # Enter a function here
    filtered_list = [x for x in list_of_integers if x == list_of_integers[4]]
    print(len(list_of_integers) == 8 and len(filtered_list) == 3)


def main(list_of_ints):
    # Enter main function here
    print(list_of_ints)
    a_function(list_of_ints)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main([19, 19, 15, 5, 5, 5, 1, 2])
    main([19, 15, 5, 7, 5, 5, 2])
    main([11, 12, 14, 13, 14, 13, 15, 14])
    main([19, 15, 11, 7, 5, 6, 2])

    print(f"Runtime: ---{time.time() - start_time}---")
