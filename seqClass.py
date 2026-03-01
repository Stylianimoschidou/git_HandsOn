#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

# Create argument parser
parser = ArgumentParser(description='Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif")

# Show help if no arguments provided
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# Normalize sequence to uppercase
args.seq = args.seq.upper()

# Validate allowed characters
if not re.search('^[ACGTU]+$', args.seq):
    print("The sequence is not DNA nor RNA")
    sys.exit(0)

# Classification logic
has_T = 'T' in args.seq
has_U = 'U' in args.seq

# If both T and U appear, sequence is invalid
if has_T and has_U:
    print("Invalid sequence: contains both T and U")
elif has_T:
    print("The sequence is DNA")
elif has_U:
    print("The sequence is RNA")
else:
    print("The sequence can be DNA or RNA")

# Optional motif search
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end='')
    if re.search(args.motif, args.seq):
        print("YES FOUND")
    else:
        print("YES NOT FOUND")
