#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, shutil, re, argparse, json
from codecs import open
from itertools import izip
from collections import defaultdict, Counter



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name')
    parser.add_argument('infiles', nargs='+')
    parser.add_argument('outfile')
    args = parser.parse_args()
    
    entries = []
    for filename in args.infiles:
        with open(filename, 'r', 'utf8') as fin:
            data = json.load(fin)
            for x in data['results'].values():
                printouts = x['printouts']
                entries.append({key: (value[0] if value else '0') for (key, value) in printouts.iteritems()})
    entries.sort(key=lambda x: x['English name'])

    with open(args.outfile, 'w', 'utf8') as fout:
        fout.write('var ' + args.name + ' = ')
        json.dump(entries, fout, separators=(',', ':'), ensure_ascii=False)
        fout.write(';\n')
    print >> sys.stderr, 'Wrote {} entries'.format(len(entries))


if __name__ == '__main__':
    main()

