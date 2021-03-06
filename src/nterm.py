#!/usr/bin/env python3

from note import *


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()

    group.add_argument("-n", "--note", action=CreateNote, nargs=2, metavar=("Title", "Text"), help="Creates a Note")
    group.add_argument("-e", "--encrypt", action=CreateEncryptedNote, nargs=3, metavar=("Title", "Text", "Password"),
                       help="Creates an encrypted note")
    group.add_argument("-d", "--decrypt", action=DecryptNote, nargs=2, metavar=("ID", "Password"),
                       help="Decrypts a note selected by ID")
    group.add_argument("-m", "--modify", action=ModifyNote, metavar="ID", help="Modifies a note selected by Id")
    group.add_argument("-s", "--show", action=ShowNote, metavar="ID",
                       help="Shows a note selected by ID")
    group.add_argument("-l", "--list", action=ListAll, nargs=0, help="Lists every note available")
    group.add_argument("-r", "--remove", action=RemoveNote, nargs='+', metavar="ID",
                       help="Removes n notes selected by ID")
    group.add_argument("-R", "--remove-all", action=RemoveAll, nargs=0, help="Removes Everything")

    parser.parse_args()


if __name__ == '__main__':
    main()
