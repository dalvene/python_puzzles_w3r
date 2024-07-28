"""
Puzzle 4 from w3resource Python Programming Puzzles
https://www.w3resource.com/python-exercises/puzzles/index.php
"""


def a_function(i: int):
    # Enter a function here
    print([2*n+i for n in range(0, i)])


def main(i):
    # Enter main function here
    print(i)
    a_function(i)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main(2)
    main(10)
    main(3)
    main(17)

    print(f"Runtime: ---{time.time() - start_time}---")
