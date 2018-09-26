# CmdPy

This is a Python app to run terminal commands on a file line by line and can store output to file if needed

## Usage
	$ python CmdPy.py [ options ] 
	
	[ options ]
      -h, --help                          show this help message and exit
	  -f <FILE>, --file <FILE>            File to read -- Requires -c if used
	  -c <COMMAND>, --command <COMMAND>   Command to execute against file -- Requires -f if used
	  -o <OUTPUT>, --output <OUTPUT>      Exec Output file  -- optional
	  -ow, --overwrite                    OverWrite if file existing  -- optional
	  -v, --version                       show program's version number
 
 ### Example Usage
 
 In this example i'm running echo command against each line in the file called input.txt below shows various tests that can be done,
 The example file used input.txt is present in repo change it to your file name with location.
 
 1. To run bash command 'echo' against each line file input.txt
 
        $ python CmdPy.py -f input.txt -c echo
    
 2. To Create Output File called output.txt this appends output of command of each line in file if file exists
 
        $ python CmdPy.py -f input.txt -c echo -o output.txt
    
 3. Same as 2. OverWrite Output File  if exists
 
        $ python CmdPy.py -f input.txt -c echo -o output.txt -ow
        
        
        
 ## License

    Copyright 2018 - Sujaykumar.Hublikar <hello@sujaykumarh.com>

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
