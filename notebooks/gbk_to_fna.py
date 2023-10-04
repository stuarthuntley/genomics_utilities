#!/usr/bin/env/ python
""" Convert genbank format file to fasta

This utility creates a new fasta format file containing the sequence
data from a given genbank input file. The new file will bear the same
name as the input file, with the suffix changed to '.fa'

Usage:
./gbk_to_fna.py file.gbk

Author: Stuart Huntley stuhuntley@gmail.com

Created: 2023-09-26

License:
Copyright (C) 2023  Stuart Huntley

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

__author__ = "Stuart Huntley"
__contact__ = "stuhuntley@gmail.com"
__credits__ = ["NA"]
__date__ = "2023-09-26"
__deprecated__ = False
__email__ = "stuhuntley@gmail.com"
__license__ = "GPLv3"
__maintainer__ = "Stuart Huntley"
__status__ = "Development"
__version__ = "0.0.1"

import sys

input_file = sys.argv[1]

def main():



if __name__ == '__main__':
    args = parse_arguments()
    main(input_file)
