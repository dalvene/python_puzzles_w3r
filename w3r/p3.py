"""
Puzzle 3 from w3resource Python Programming Puzzles
https://www.w3resource.com/python-exercises/puzzles/index.php
"""


def a_function(i: int):
    # Enter a function here
    print(i > 4**4 and i % 34 == 4)


def main(i):
    # Enter main function here
    print(i)
    a_function(i)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main(922)
    main(914)
    main(854)
    main(854)

    print(f"Runtime: ---{time.time() - start_time}---")
