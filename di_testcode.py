#test for deeper insights
"""Author: Sriharsha Aryasomayajula
   Date: 30-04-2023
   Position: Machine Learning Software Engineer"""

import logging as log
from argparse import ArgumentParser, SUPPRESS
from pathlib import Path
import re

log.basicConfig(level=log.INFO) #sets the basic logging level as info in that way any warnings or info statements are shown

class StringMatcher():
    def build_argparser(self) -> object:
        #inspired from intel openvino code base
        """Build the command line argument parser for the program.
        Returns:
        argparse.ArgumentParser object: A configured argument parser object."""
        parser = ArgumentParser(add_help=False)
        args = parser.add_argument_group('Options')
        args.add_argument('-h','--help',action='help',help = 'Please follow the readme.md file for instructions on how to run this program') #adds a -h flag to help the user with the program
        args.add_argument('file',help = 'Required. Path to an .txt file')
        return parser
    
    def search_item(self) -> tuple:
        """stores the search item from the txt file.
        Returns:
        A tuple of search item and lines in the file"""
        args = self.build_argparser().parse_args()
        self.file_path = args.file
        with open(self.file_path, "r") as file:
            lines = file.readlines() #reads the files contents line by line and stores them in lines variable
            search_term = lines[-1].strip() #stores the last line as the search term
            return search_term,lines
             
    def check_file_health(self) -> None:
        """Checks the file health based on existence and extension of file path. 
        Returns:
        Error message or None."""
        args = self.build_argparser().parse_args()
        self.file_path = args.file
        if not Path(self.file_path).is_file(): #checks if it is a valid path 
            return f'{self.file_path} is not a valid file path'
        if not args.file.endswith('.txt'): #checks if it is a .txt file
            return 'Please input a text file'
        return None

    def perform_string_operation(self, last_line,lines_file) -> None:
        """Performs string operation by matching last line with each line in the file and does some regex filtering to avoid numerical,special characters. 
        Returns
        print statement."""
        for line in lines_file[:-1]: #this for loop go through all the lines except the last line in the file
            if last_line in line: #sub string matching using python "in"
                clean_line = re.sub(r'[^a-zA-Z\s]+', ' ', line) #more filters can be added here
                print(f'[{clean_line.strip()}]')
        return None

    def run(self) -> None:
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