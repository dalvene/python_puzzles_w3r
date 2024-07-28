"""
Puzzle 6 from w3resource Python Programming Puzzles
https://www.w3resource.com/python-exercises/puzzles/index.php
"""


def a_function(l: list):
    # Enter a function here
    state = True
    for n in range(len(l)-1):
        if l[n] + 10 != l[n+1]:
            state = False
            break
    print(state)


def main(l):
    # Enter main function here
    print(l)
    a_function(l)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main([n for n in range(0, 999, 10)])
    main([n for n in range(0, 999, 20)])

    print(f"Runtime: ---{time.time() - start_time}---")
