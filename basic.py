#!/usr/bin/env python
"""Defining methods """

import subprocess
from subprocess import os

print("\n Thanks for running my program! \n")



def wrte_file():
    """ Showing and making a directory. Then asking user if process should be started.
    Finally, changing into that directory for file creation if process is started. """

    gett_currwd = os.getcwd()
    print(gett_currwd, end="\n")

    text_for_file = "This text is for the txt file."

    print("\nDo you want to start the file writing process? ")
    openning = input("Yes or No ?_:>> ")

    if openning == "yes" or openning == "y":
        if openning == "yes" or openning == "y":
            print(os.mkdir("txtFiles"), end="")
            print(os.chdir("txtFiles"), end="")
        with open("writing.txt", "w") as file_text:
            file_text.write(text_for_file)
            file_text.close()
    else:
        if openning == "no" or openning == "n":
            print("\nQuitting.....")


def strt_trcrt():
    """ Starting a trceroute process based on wether the user chooses to
        start the process. """
