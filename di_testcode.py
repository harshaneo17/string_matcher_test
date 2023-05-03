#test for deeper insights
"""Author: Sriharsha Aryasomayajula
   Date: 30-04-2023
   Position: Machine Learning Software Engineer"""

import logging as log
from argparse import ArgumentParser, SUPPRESS
from pathlib import Path
import re
import os

log.basicConfig(level=log.INFO) #sets the basic logging level as info in that way any warnings or info statements are shown

def build_argparser() -> object:
    #inspired from intel openvino code base
    """Build the command line argument parser for the program.
    Returns:
    argparse.ArgumentParser object: A configured argument parser object."""
    parser = ArgumentParser(add_help=False)
    args = parser.add_argument_group('Options')
    args.add_argument('-h','--help',action='help',help = 'Please follow the readme.md file for instructions on how to run this program') #adds a -h flag to help the user with the program
    args.add_argument('file',help = 'Required. Path to an .txt file')
    return parser

#if and else statement with yaml config to describe what the status is
#package this into a pip cli package

class StringMatcher():
    def __init__(self) -> None:
        self.args = build_argparser().parse_args()
        self.file_path = self.args.file

    def search_item(self) -> tuple:
        """stores the search item from the txt file.
        Returns:
        A tuple of search item and lines in the file
        note: This doesnt solve the problem for larger files"""
        with open(self.file_path, "r") as file:
            lines = []
            for line in file: #a simple for loop to collect all the lines into a list. This goes easy on the memory for large files
                lines.append(line)
            search_term = lines[-1].strip() #stores the last line as the search term
            return search_term,lines
             
    def check_file_health(self) -> None:
        """Checks the file health based on existence and extension of file path. 
        Returns:
        Error message or None."""
        if not Path(self.file_path).is_file(): #checks if it is a valid path 
            return f'{self.file_path} is not a valid file path. Make sure the file exists'
        if not self.args.file.endswith('.txt'): #checks if it is a .txt file
            return f'{self.file_path} is not text file.Please input a text file'
        if os.stat(self.file_path).st_size == 0:
            return f'{self.file_path} is empty. Please make sure it has contents'
        return None

    def perform_string_operation(self, last_line: str,lines_file: list) -> None:
        """Performs string operation by matching last line with each line in the file and does some regex filtering to avoid numerical,special characters. 
        Returns
        print statement."""
        for line in lines_file[:-1]: #this for loop go through all the lines except the last line in the file
            if last_line in line: #sub string matching using python "in"
                clean_line = re.sub(r'[^A-Za-zÀ-ÖØ-öø-ÿ\s]+', ' ', line) #more filters can be added here
                print(f'[{clean_line.strip()}]')
        return None

    def run(self) -> None:
        """Main block of the code."""
        error_message = self.check_file_health()
        if error_message:
            log.error(error_message)
            return

        log.info('opening a text file')
        last_line, lines_file = self.search_item()
        with open(self.file_path, "r") as file:
            self.perform_string_operation(last_line, lines_file)
        return None


def main():
    """Creates an object of the type class StringMatcher and runs it"""
    stringapp = StringMatcher()
    stringapp.run()

if __name__ == main():
    main()