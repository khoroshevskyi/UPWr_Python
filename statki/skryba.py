#!/usr/bin/env python
import os, sys, getopt
import optparse


class Scryba():
    """Scryba"""

    def __init__(self):
        options = vars(self.get_arg())
        file = options['filename']
        self.write_data(file)

    def get_arg(self):
        parser = optparse.OptionParser()

        parser.add_option("-r", "--ruchy", dest="filename", default = 'ruchy.txt',
                            help="File that contains ships positions, earlier generated")

        (options, args) = parser.parse_args()
        return(options)


    def write_data(self, file_name):
        try:
            text = ''
            for line in sys.stdin:
                if line != '':
                    sys.stdout.write(line)
                    break

            file_object  = open(file_name, "a")
            file_object.write(line)
            file_object.close()
            #if line == "koniec":
                #break
        except EOFError as e:
            print(e)

if __name__ == "__main__":
    Scryba()

#.\skryba.py −r ruchy.txt | .\gracz.py −u ustawienia.txt -s | .\skryba.py −r ruchy.txt
