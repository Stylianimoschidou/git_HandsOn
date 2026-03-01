#!/usr/bin/env python

# Import system utilities and regular expression tools
import sys, re
from argparse import ArgumentParser

# Create a command-line argument parser with a description
parser = ArgumentParser(description='Classify a sequence as DNA or RNA')

# Add a required argument for the input sequence
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")

# Add an optional argument for a motif to search within the sequence
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif")

# If no arguments are provided, show help and exit
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse the provided command-line arguments
args = parser.parse_args()

# Convert the sequence to uppercase to avoid case sensitivity issues
args.seq = args.seq.upper()

# Validate that the sequence contains only nucleotide characters
if re.search('^[ACGTU]+$', args.seq):

    # If the sequence contains T, it must be DNA
    if re.search('T', args.seq):
        print('The sequence is DNA')

    # If the sequence contains U, it must be RNA
    elif re.search('U', args.seq):
        print('The sequence is RNA')

    # If it contains neither T nor U, it could be either DNA or RNA
    else:
        print('The sequence can be DNA or RNA')

# If invalid characters are present, it is not a valid nucleotide sequence
else:
    print('The sequence is not DNA nor RNA')

# If a motif was provided, perform a motif search
if args.motif:
    # Convert motif to uppercase for consistency
    args.motif = args.motif.upper()

    # Announce the motif search
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end='')

    # Search for the motif inside the sequence
    if re.search(args.motif, args.seq):
        print("YES FOUND")
    else:
        print("YES NOT FOUND")
