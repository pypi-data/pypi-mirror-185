#!/usr/bin/env python
import libcagen
import argparse


parser = argparse.ArgumentParser(prog = "cagen", description="static site generator for cmpalgorithms project")
parser.add_argument("source", type=str, help="the source markdown file")
parser.add_argument("to", type=str, help="destination file")
parser.add_argument("template", type=str, help="cheetah 3 template file path")
parser.add_argument("--syntax", type=str, default='html5', help="syntax of destination file. By default 'html5'")
args = parser.parse_args()

# Conversion
entry = libcagen.Entry(args.source)
with open(args.to, "w") as f:
    f.write(entry.to(mytemplatepath=args.template, destsyntax=args.syntax))

print("{} -> {} ({}) using {}".format(args.source, args.to, args.syntax, args.template))
