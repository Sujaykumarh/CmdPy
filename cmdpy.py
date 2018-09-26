#!/usr/bin/python
import argparse, subprocess

_appName = "CmdPy"  # App Name
_appVer = "0.0.1"  # App Version

_input_file = ''  # Global Variable for input file location
_output_file = ''  # Global Variable for output file location
_command = ''  # Global Variable for command
_overwrite_file = False  # GLobal Variable  for OverWriting file if exists


class AssignArgs(argparse.Action):  # Assign Argument value to Golbal variable
    def __call__(self, parser, namespace, values, option_string=None):
        if option_string == '-f':
            global _input_file
            _input_file = values  # Assign input file name to global var

        if (option_string == '-c'):
            global _command
            _command = values  # Assign command to global var

        if (option_string == '-o'):
            global _output_file
            _output_file = values  # Assign output file name to global var


def runCommand():  # function to run Command
    lines = [line.rstrip('\n') for line in open(_input_file)]  # Read line one by one

    if(_overwrite_file and _output_file != ''): # if overwrite used overwrite existing file
        f = open(_output_file, "w+")
        f.write("")

    for line in lines:
        output = subprocess.run([_command, line], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        print(output)  # Print Output of command
        if (_output_file != ''):
            f = open(_output_file, "a")
            f.write(output + "\n")


def main():
    parser = argparse.ArgumentParser(prog=_appName, description='Tool to run commands against list of values in a file')
    parser.add_argument('-f', '--file', action=AssignArgs, help="File to read", required='-c')
    parser.add_argument('-c', '--command', action=AssignArgs, help="Command to execute against file", required='-f')
    parser.add_argument('-o', '--output', action=AssignArgs, help="Exec Output file")
    parser.add_argument('-ow', '--overwrite', action='store_true', dest='_overwrite_file', help="OverWrite if file existing")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s v{version}'.format(version=_appVer))
    args = parser.parse_args()
    globals().update(args.__dict__)
    _overwrite_file = args._overwrite_file
    # Run Commands on each line in the file
    runCommand()


if __name__ == '__main__':
    main()  # Run Main Function
