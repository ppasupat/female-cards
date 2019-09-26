#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, shutil, re, argparse, json
from collections import defaultdict, Counter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name')
    parser.add_argument('infiles', nargs='+')
    parser.add_argument('outfile')
    args = parser.parse_args()
    
    entries = []
    for filename in args.infiles:
        with open(filename) as fin:
            data = json.load(fin)
            for x in data['results'].values():
                printouts = x['printouts']
                entries.append({key: (value[0] if value else '0') for (key, value) in printouts.items()})
    entries.sort(key=lambda x: x['English name'])

    if args.outfile == '-':
        # Print TSV instead
        for entry in entries:
            print('{}\t{}\t{}'.format(
                entry['Password'],
                entry['English name'],
                entry['Japanese name'],
            ))
        return

    with open(args.outfile, 'w') as fout:
        fout.write('var ' + args.name + ' = ')
        json.dump(entries, fout, separators=(',', ':'), ensure_ascii=False)
        fout.write(';\n')
    print('Wrote {} entries'.format(len(entries)), file=sys.stderr)


if __name__ == '__main__':
    main()

