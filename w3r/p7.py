"""
Puzzle 7 from w3resource Python Programming Puzzles
https://www.w3resource.com/python-exercises/puzzles/index.php
Easy
"""


def a_function(l: list):
    # Enter a function here
    print(sum(l) == len(l))


def main(l):
    # Enter main function here
    print(l)
    a_function(l)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main([0, 1, 2, 3, 4, 5])
    main([1, 1, 1, 1, 1, 1])
    main([2, 2, 2, 2, 2])
    print(f"Runtime: ---{time.time() - start_time}---")
