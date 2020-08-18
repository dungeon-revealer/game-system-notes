#! /usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, glob, re, validators, argparse
from frontmatter import Frontmatter

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("dir", help="path to files")
args = parser.parse_args()
path = args.dir

print("dungeon-revealer note validator\n")

# Check if path is accessible
if not os.path.isdir(path):
    print("{path} is not accessible!\n".format(path=path))
    sys.exit(-1)

# Required attributes in notes frontmatter
required_attrs = ["id", "title", "is_entry_point"]

# Formatted error strings
attr_err_str = "\nError: Invalid Frontmatter\n  Attribute {attr} is {err}\n  File: {file}\n  Frontmatter:\n    ---{fm}---\n"
link_err_str = "\n{err}\n  File: {file}\n  Line: {line}\n  Link: {link}\n"
id_err_str   = "\nError: {err}\n  id: {id}\n  Files:\n    {f1}\n    {f2}\n"

def check_frontmatter(fmatter):
    num_errs = 0
    has_required_attrs = True
    fm = fmatter['frontmatter'].replace('\n','\n    ')
    for x in required_attrs:
        if x not in fmatter['attributes']: # Check for required attributes
            print(attr_err_str.format(file=fname, attr=x, err="missing", fm=fm))
            has_required_attrs = False
            num_errs += 1

    # Skip the rest of checks if missing required attributes
    if has_required_attrs:
        if not re.match('^[-\w]+$', fmatter['attributes']["id"]): # Check for invalid id string
            print(attr_err_str.format(file=fname, attr="id", err="invalid\n  id must contain only alphanumeric, hyphen(-), or underscore(_)", fm=fm))
            num_errs += 1

        if fmatter['attributes']["title"] is None: # Check for empty attribute
            print(attr_err_str.format(file=fname, attr="title", err="invalid", fm=fm))
            num_errs += 1

        if not isinstance(fmatter['attributes']["is_entry_point"] , bool) : # Check for non-boolean attribute
            print(attr_err_str.format(file=fname, attr="is_entry_point", err="invalid", fm=fm))
            num_errs += 1

    return num_errs


errs = 0
dict = {}
ids = []
print("Checking notes frontmatter...\n")
for fname in glob.glob(path + "/**/*", recursive=True): # Find all files and subdirectories
    # Skip directories
    if os.path.isdir(fname):
        continue

    # Parse file's front matter
    fmatter = Frontmatter.read_file(fname)
    err = check_frontmatter(fmatter)
    errs += err
    if err == 0:
        id = fmatter['attributes']["id"]
        if id in dict: # Check if id already exists
            print(id_err_str.format(err="id already exists", id=id, f1=dict[id]["filename"], f2=fname))
            errs += 1
        else:
            with open(fname,"r") as file: # Build dictionary of file frontmatters
                link_list = []
                line_num = 0
                for line in file:
                    line_num += 1
                    links = re.findall('\[[^\[\]\)\(]*\]\([^\[\]\)\(]*\)', line) # Find all markdown links on the line
                    if links != []:
                        link_list.append([line_num, links]) # [ [line_num, [link1, link2, ...]], ... ]

            dict[id] = { "filename": fname, "links": link_list }

# Check for invalid links
if errs == 0:
    print("Checking notes links...\n")
    for id in dict:
        for line in dict[id]["links"]:
            for link in line[1]:
                link_id = re.match('.*\((.*)\)', link).group(1) # Extract link id
                if link_id not in dict:
                    if not validators.url(link_id): # Check if invalid external link
                        print(link_err_str.format(err="Error: Invalid Link", file=dict[id]["filename"], line=line[0], link=link))
                        errs += 1
                    else: # Valid external link
                        print(link_err_str.format(err="Warning: External Link", file=dict[id]["filename"], line=line[0], link=link))
else:
    print("Skipped notes links checks...\n")


if errs != 0:
    print("\nTotal number of errors: {n}".format(n=errs))
else:
    print("\nNo errors found")

sys.exit(errs)
