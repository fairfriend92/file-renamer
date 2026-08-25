import os
import unidecode
from argparse import ArgumentParser

def rename(path, recursive):    
    for filename in os.listdir(path):
        name, ext = os.path.splitext(filename)
        name = name.replace(" ", "-")
        name = name.replace("_", "-")
        name_ascii = unidecode.unidecode(name)
        old_name = path + filename
        new_name = path + name_ascii.lower() + ext
        if old_name != new_name:
            print(old_name + " -> " + new_name)
            os.rename(old_name, new_name)
        if recursive and os.path.isdir(new_name):
            rename(new_name + "/", recursive)            

parser = ArgumentParser(prog="FileRenamer",
                        description="Rename files in a given folder")
parser.add_argument("-p", "--path",
                    help="Specify path to folder")
parser.add_argument("-r", "--recursive", action="store_true",
                    help="Recursively rename subfolders",)
args = parser.parse_args()
root = "." if args.path is None else args.path

rename(root, args.recursive)
