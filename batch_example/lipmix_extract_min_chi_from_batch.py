import glob
import os
import sys
import time
import re


def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


os.system("mkdir result")

file_to_search = "."
dirlist = []

for filename in os.listdir(file_to_search):
    if os.path.isdir(os.path.join(file_to_search, filename)):
        dirlist.append(filename)

# Walk over the directories in the current folder.
for _dir_ in natural_sort(dirlist):

    if _dir_ == "result":
        pass
    else:
        os.chdir(_dir_)

        file_to_search = "."
        dirlist = []

        for filename in os.listdir(file_to_search):
            if os.path.isdir(os.path.join(file_to_search, filename)):
                dirlist.append(filename)

        chi_val = {}
        chi_val_inv = {}
        chi_ = []

        for dir_ in natural_sort(dirlist):
            if dir_ == "result":
                pass
            else:
                try:
                    f = open(dir_ + "/" + dir_.split("_n_dist_")[0] + ".fit")
                    lines = f.readlines()
                    f.close()
                except:
                    pass
                else:
                    for line in lines:
                        if "Chi^2 =" in line:
                            chi_val[float(line.split("Chi^2 =")[1])] = dir_
                            chi_val_inv[dir_] = float(line.split("Chi^2 =")[1])
                            chi_.append(float(line.split("Chi^2 =")[1]))

        print("Min chi:", min(chi_), chi_val[min(chi_)])

        os.system("cd " + str(chi_val[min(chi_)]) + "&& cp * ../../result")
        os.chdir("..")
