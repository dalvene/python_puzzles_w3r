"""
Puzzle 11 from w3resource Python Programming Puzzles
https://www.w3resource.com/python-exercises/puzzles/index.php
"""


def a_function(some_numbers: list):
    # Enter a function here
    threshold = int(input("Threshold: "))
    print([n for n in range(len(some_numbers)) if some_numbers[n] < threshold])


def main(some_numbers):
    # Enter main function here
    print("Check the indexes of numbers of the said list below the given threshold:")
    print(some_numbers)
    a_function(some_numbers)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main([0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55])
    main([0, 12, 4, 3, 49, 9, 1, 5, 3])
    print(f"Runtime: ---{time.time() - start_time}---")
