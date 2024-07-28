"""
Puzzle 5 from w3resource Python Programming Puzzles
https://www.w3resource.com/python-exercises/puzzles/index.php
"""


def a_function(l: list):
    # Enter a function here
    print(l[len(l)-2] in l[len(l)-1])


def main(l):
    # Enter main function here
    print(l)
    a_function(l)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main(['a', 'abb', 'sfs', 'oo', 'de', 'sfde'])
    main(['a', 'abb', 'sfs', 'oo', 'ee', 'sfde'])
    main(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew'])
    main(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew'])

    print(f"Runtime: ---{time.time() - start_time}---")
