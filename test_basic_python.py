
import pytest

import read_this_file_first



import module_string_study


def test_show_strings():

    print("\n**** Here in pytest ****\n")

    print(read_this_file_first.INTRODUCTION_WORDS)

    print("Show the basic variable __name_ of basic_python is now {}".format(read_this_file_first.__name__))

    print("\n**** End Here in pytest ****\n")
