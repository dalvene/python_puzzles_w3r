"""
Puzzle 9 from w3resource Python Programming Puzzles
https://www.w3resource.com/python-exercises/puzzles/index.php

"""


def a_function(some_integers: list):
    # Enter a function here
    entries = {n: True for n in some_integers}
    repeats = 0
    for n in range(len(some_integers)-1):
        if n >= 20:
            break
        elif some_integers[n] == some_integers[n+1]:
            repeats = 1
            break
    print(repeats == 0 and len(entries) == 4)


def main(some_integers):
    # Enter main function here
    print(some_integers)
    a_function(some_integers)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4])
    main([1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3])
    main([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Runtime: ---{time.time() - start_time}---")
