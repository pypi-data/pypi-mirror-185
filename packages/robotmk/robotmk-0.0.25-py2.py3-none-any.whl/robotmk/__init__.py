"""Robot Framework test execution and result parsing for Check_MK"""
__version__ = "0.0.25"

# from robotmk import cli
# import sys

import robotmk.cli as cli

# # check if module was imported with cmdline args
# if __name__ == "robotmk" and len(sys.argv) > 1:
if __name__ == "robotmk":
    print(
        __name__
        + ": "
        + "You have imported robotmk module with sys args => execute cli!"
    )
    cli.main()
# else:
#     print(__name__ + ": " + "You have just imported the robotmk module! No execution")
