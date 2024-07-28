"""
Puzzle 12 from w3resource Python Programming Puzzles
https://www.w3resource.com/python-exercises/puzzles/index.php
"""


def a_function(palindromes: list):
    # Create a list of booleans that tells us if each word in an input list is a palindrome.
    # Function compares each word in the list to its reverse.

    # output_list = []
    # for word in palindromes:
    #     reverse_word = word[-1::-1]
    #     if reverse_word == word:
    #         output_list.append(True)
    #     else:
    #         output_list.append(False)
    # print(output_list)

    # This list comprehension achieves the same as the eight line code above.
    print([word[-1::-1] == word for word in palindromes])


def main(palindromes):
    # Enter main function here
    print(palindromes)
    a_function(palindromes)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main(['palindrome', 'madamimadam', '', 'foo', 'eyes'])
    print(f"Runtime: ---{time.time() - start_time}---")
