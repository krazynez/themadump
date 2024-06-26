#!/usr/bin/env python3

import argparse

from psptool.pack import pack_btcnf
from psptool.prx import encrypt

parser = argparse.ArgumentParser(description="Infinity Boot Config Packer")
parser.add_argument('input', type=argparse.FileType('rb'),
                    help='The raw text file to pack')
parser.add_argument('--vanity', type=str,
                    help='Some vanity text in the executable header')
parser.add_argument('output', type=str,
                    help='The output to write the packed text')
args = parser.parse_args()

executable = args.input.read()
executable = encrypt(pack_btcnf(executable,
                              psptag=0x00000000), vanity=args.vanity)

with open(args.output, 'wb') as f:
    f.write(executable)
