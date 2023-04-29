#test for deeper insights

import logging as log
import sys
from argparse import ArgumentParser, SUPPRESS
from pathlib import Path
import re

class StringMatcher():
    def build_argparser(self) -> object:
        #takes arguements as file path
        parser = ArgumentParser(add_help=False)
        args = parser.add_argument_group('Options')
        args.add_argument('-h','--help',action='help',help = 'This is a help message')
        args.add_argument('file',help = 'Required. Path to an .txt file or csv file')
        return parser
    def run(self):
        args = self.build_argparser().parse_args()
        string_case = args.file
        if args.file.endswith('.txt'):
            log.info('opening a text file')
            with open(string_case, "r") as file:
                lines = file.readlines()
                last_line = lines[-1]
                lines = list(lines)[:-1]
                for line in lines:
                    if re.search(last_line,str(line)):
                        print(line)
                    else:
                        print(None)
        elif args.file.endswith('.csv'):
            log.info('opening a csv file')
            with open(string_case, "r") as file:
                lines = file.read().strip()
                last_line = lines[-1]
                print('easy')
        else:
            log.error(f'Please input a text file or csv file')


def main():
    stringapp = StringMatcher()
    stringapp.run()

if __name__ == main():
    main()