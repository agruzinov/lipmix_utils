import os
import numpy as np
import glob
import itertools
import argparse
import shutil
import re


def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('(\d+)', key)]
    return sorted(l, key=alphanum_key)


def generate_lipmix_submission(l, d, dat):
    # l - number of bilayers
    # d - number of distributions

    directory = dat.split(".dat")[0]
    if not os.path.exists(directory):
        os.makedirs(directory)

    n_dist = d

    total_l = l

    os.chdir(directory)

    for dis in np.arange(1, n_dist + 1):

        list_l = list(np.arange(1, total_l + 1))

        tot_com = 0

        for l in np.arange(1, total_l + 1):

            perm = itertools.combinations(list_l, l)

            for p in perm:
                tot_com = tot_com + 1
                fn = dat.split(".dat")[0] + "_n_dist_" + str(dis) + "_" + str(list(p)).replace(", ", "_") + "_" + str(
                    tot_com)

                directory = fn
                if not os.path.exists(directory):
                    os.makedirs(directory)

                os.chdir(directory)
                shutil.copy2("../../" + dat, "../" + directory)

                f = open(fn, "w")

                f.write("i\n")
                f.write("!!!!!!!!!!!!!!!\n")
                f.write("pro us\n")
                f.write("Series titles\n")
                f.write("Partial data titles\n")
                f.write("EXPERIMENT\n")
                f.write(str(dis + 2) + "           !! Number of components\n")
                f.write("0.5000   !! System concentration\n")
                f.write("DIFFUSE                         !! Type of the DIFFUSE Phase (SFF approximation)\n")
                f.write("0.50    0.0000    100.000       !! Volume fraction of the bilayer component\n")
                f.write("3.531   1.421     6.141         !! Peak1 position (positive density)\n")
                f.write("0.313   0.103     0.523         !! Width of peak1 position (positive density)\n")
                f.write("1.650   1.440     2.560         !! Peak2 position (positive density)\n")
                f.write("0.329   0.120     0.340         !! Width of peak2 position (positive density)\n")
                f.write("0.172   0.000     1.780         !! Amplitude ratio (Peak2/Peak1) (positive density)\n")
                f.write("0.196   0.080     0.450         !! Width of peak3 position (negative density)\n")
                f.write("0.884   0.270     3.890         !! Amplitude ratio (Peak3/Peak1) (negative density)\n")
                f.write(
                    "0.01    0.01      0.020         !! Callie parameter (measure for the bilayer bending "
                    "fluctuations)\n")

                f.write("   " + str(len(p)) + "        " + str(len(p)) + "       " + str(
                    len(p)) + "       " + "!! Total Number of multilayer vesicles (always FIXED)\n")
                for pi in p:
                    f.write("   " + str(pi) + "       " + str(pi) + "       " + str(
                        pi) + "       " + "!! Number of layers for vesicle type" + str(pi) + "\n")
                    print(f.write(
                        "   1.0      0.0       1.0       !! Weight contribution of vesicle type " + str(pi) + "\n"))

                for dis in np.arange(1, dis + 1):
                    f.write("SPHERE                          !! Type of the SPHERE Phase (SFF approximation)\n")
                    f.write("0.5000    0.0000    100.000     !! Volume fraction of the component (vesicle/micelle)\n")
                    f.write("0.0000    0.0000    0.0000      !! Inner (core) radius of the sphere\n")
                    f.write("0.0000    0.0000    0.0000      !! Inner (core) contrast of the sphere\n")
                    f.write("40.4598   1.7678   80.1518    !! Outer (core+shell) radius of the sphere\n")
                    f.write("1.0000    1.0000    1.0000      !! Outer (shell) contrast of the sphere\n")
                    f.write("1.6920    0.1730   17.3839      !! Polydisperstiry on the sphere radius\n")
                    f.write("400.000   400.000   400.000     !! Hard-sphere radius (for interactions only)\n")
                    f.write("2                               !! Schulz distribution 2 (Gauss distribution 1)\n")
                    f.write("0.0000    0.0000    0.0000      !! stickiness parameter (for interactions only)\n")

                f.write("SPHERE\n")
                f.write("   0.0050    0.0000    1.0000    !! Volume fraction of the component (vesicle/micelle)\n")
                f.write("   0.0000    0.0000    0.0000    !! Inner (core) radius of the sphere\n")
                f.write("   0.0000    0.0000    0.0000    !! Inner (core) contrast of the sphere\n")
                f.write("   0.4630    0.3307    0.6614    !! Outer (core+shell) radius of the sphere\n")
                f.write("   1.0000    1.0000    1.0000    !! Outer (shell) contrast of the sphere\n")
                f.write("   0.01653    0.01323    0.1984    !! Polydisperstiry on the sphere radius\n")
                f.write("  1.2278   1.2278   1.2278    !! Hard-sphere radius (for interactions only)\n")
                f.write("2                                !! Schulz distribution 2 (Gauss distribution 1)\n")
                f.write("   0.0000    0.0000    0.0000    !! stickiness parameter (for interactions only)\n")
                f.write(" 2                      !! ASCII format file\n")
                f.write(dat + "        !! Experimental data file\n")
                f.write(dat.split(".dat")[0] + "        !! Output prefix name\n")
                f.write("1                       !! Angular scale (1/2/3/4) as in GNOM\n")
                f.write("1.0                     !! Exp. data portion to fit (from beginning)\n")
                f.write("meth sb                 !! Minimization method sb - \"simple bounds\"\n")
                f.write("loa maxit 1000          !! Maximum number of iterations\n")
                f.write("run\n")
                f.write("y\n")
                f.write("y\n")
                f.write("mess 15\n")
                f.write("eva\n")
                f.write("mes 1\n")
                f.write("ex\n")
                f.write("y\n")
                f.write("y\n")

                f.close()

                os.system("lipmix <" + fn)
                os.chdir("../")
    os.chdir("../")


# Arguments parser
parser = argparse.ArgumentParser(description='Wrap-up script to generate multiple input files for LIPMIX with '
                                             'iterative number of layers. Example: python '
                                             'lipmix_multilayer_autofinder.py -i test_lipmix_MLV.dat -l 1 -d 1')
parser.add_argument('-l', '--layers', default=1, required=True, type=int, help="Total expected number of layers.")
parser.add_argument('-d', '--distr', default=1, required=True, type=int, help="Total expected number of distributions.")
parser.add_argument('-i', '--input', nargs='+', required=True, default="input.dat", type=str, help="Input dat file")
args = parser.parse_args()

# Main part
matched_files = []
for file in args.input:
    if glob.escape(file) != file:
        matched_files.extend(glob.glob(file))
    else:
        matched_files.append(file)

        for file in matched_files:
            print(file)
            generate_lipmix_submission(args.layers, args.distr, file)
