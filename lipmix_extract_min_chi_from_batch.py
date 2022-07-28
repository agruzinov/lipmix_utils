import os
import re

def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('(\d+)', key)]
    return sorted(l, key=alphanum_key)

directory = "result"
if not os.path.exists(directory):
    os.makedirs(directory)

#Find all the directories
file_to_search = "."
dirlist = []
for filename in os.listdir(file_to_search):
    if os.path.isdir(os.path.join(file_to_search, filename)):
        dirlist.append(filename)

# Walk over the directories in the current folder.
for _dir_ in natural_sort(dirlist):
    # print(dirlist)

    if _dir_ != "result" and _dir_.find(".") != 0:

        chi_val = {}
        chi_val_inv = {}
        chi_ = []

        f = open(_dir_ + "/" + _dir_.split("_n_dist_")[0] + ".fit")
        lines = f.readlines()
        f.close()
        for line in lines:
            if "Chi^2 =" in line:
                chi_val[float(line.split("Chi^2 =")[1])] = _dir_
                chi_val_inv[_dir_] = float(line.split("Chi^2 =")[1])
                chi_.append(float(line.split("Chi^2 =")[1]))
    else:
        pass
print('Min chi:', min(chi_), chi_val[min(chi_)])
os.system("cd " + str(chi_val[min(chi_)]) + "&& cp * ../result")
