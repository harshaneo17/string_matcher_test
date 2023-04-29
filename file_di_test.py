#test for deeper insights

import logging as log
import sys
from argparse import ArgumentParser, SUPPRESS
from pathlib import Path

def build_argparser():
    #takes arguements as file path
    parser = ArgumentParser(add_help=False)
    args = parser.add_argument_group('Options')
    args.add_argument('-h','--help',action='help',help = 'Show this help message and exit')
    args.add_argument('-f','--input_file',required=True,help = 'Reqruired. Path to an .txt file')
    return parser

def main():
    args = build_argparser().parse_args()
    string_case = args.input_file
    f = open(string_case, "r")
    print(f.read())

if __name__ == main():
    main()