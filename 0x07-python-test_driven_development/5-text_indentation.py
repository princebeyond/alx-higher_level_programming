#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """splits a text into lines along "?", ":", "." followed by 2 new lines"""
    if not isinstance(text, str):
        raise TypeError ("text must be a string")
    new_text = text.replace(".", ".\n\n")
    new_text1 = new_text.replace("?", "?\n\n")
    new_text2 =  new_text1.replace(":", ":\n\n")

    lines = [line.strip() for line in new_text2.split('\n')]
    result = '\n'.join(lines)

    print(result)
