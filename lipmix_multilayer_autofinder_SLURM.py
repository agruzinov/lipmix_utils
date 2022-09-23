import os
import numpy as np
import glob
import itertools
import argparse
import shutil


# =======================================================
# Please check options in "Cluster submission" section
# for the particular cluster in use. Example is written
# based on SLURM submission system.
# =======================================================


def generate_lipmix_submission(l, d, dat):
    n_dist = d
    total_l = l

    directory = dat.split(".dat")[0]
    if not os.path.exists(directory):
        os.makedirs(directory)

    os.chdir(directory)

    for dis in np.arange(1, n_dist + 1):

        list_l = list(np.arange(1, total_l + 1))

        tot_com = 0

        for l in np.arange(1, total_l + 1):

            perm = itertools.combinations(list_l, l)

            for p in perm:
                tot_com = tot_com + 1
                fn = (
                    dat.split(".dat")[0]
                    + "_n_dist_"
                    + str(dis)
                    + "_"
                    + str(list(p)).replace(", ", "_")
                    + "_"
                    + str(tot_com)
                )

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
                f.write("0.2000   !! System concentration\n")
                f.write("DIFFUSE\n")
                f.write(
                    "   0.50    0.0000    100.000    !! Volume fraction of the bilayer component\n"
                )
                f.write(
                    "   2.131   1.421     2.141      !! Peak1 position (positive density)\n"
                )
                f.write(
                    "   0.245     0.245     0.245     !! Width of peak1 position (positive density)\n"
                )
                f.write(
                    "   1.900     1.500     2.350    !! Peak2 position (positive density)\n"
                )
                f.write(
                    "   0.200     0.100     0.750     !! Width of peak2 position (positive density)\n"
                )
                f.write(
                    "   0.000     0.000     0.00     !! Amplitude ratio (Peak2/Peak1) (positive density)\n"
                )
                f.write(
                    "   0.300     0.300     0.300     !! Width of peak3 position (negative density)\n"
                )
                f.write(
                    "   0.833     0.833     0.833     !! Amplitude ratio (Peak3/Peak1) (negative density)\n"
                )
                f.write("   0.05    0.01      0.20       !! Callie parameter\n")

                f.write(
                    "   "
                    + str(len(p))
                    + "        "
                    + str(len(p))
                    + "       "
                    + str(len(p))
                    + "       "
                    + "!! Total Number of multilayer vesicles (always FIXED)\n"
                )
                for pi in p:
                    f.write(
                        "   "
                        + str(pi)
                        + "       "
                        + str(pi)
                        + "       "
                        + str(pi)
                        + "       "
                        + "!! Number of layers for vesicle type"
                        + str(pi)
                        + "\n"
                    )
                    print(
                        f.write(
                            "   1.0      0.0       1.0       !! Weight contribution of vesicle type "
                            + str(pi)
                            + "\n"
                        )
                    )

                for dis in np.arange(1, dis + 1):
                    f.write("    SPHERE\n")
                    f.write(
                        "   0.500    0.00100    1.0000    !! Volume fraction of the component (vesicle/micelle)\n"
                    )
                    f.write(
                        "   0.0000    0.0000    0.0000    !! Inner (core) radius of the sphere\n"
                    )
                    f.write(
                        "   0.0000    0.0000    0.0000    !! Inner (core) contrast of the sphere\n"
                    )
                    f.write(
                        "  50.0   1.0   500.0    !! Outer (core+shell) radius of the sphere\n"
                    )
                    f.write(
                        "   1.0000    1.0000    1.0000    !! Outer (shell) contrast of the sphere\n"
                    )
                    f.write(
                        "   50.0    1.0   200.3839    !! Polydisperstiry on the sphere radius\n"
                    )
                    f.write(
                        "  86.9196   86.9196   86.9196    !! Hard-sphere radius (for interactions only)\n"
                    )
                    f.write(
                        "2                                !! Schulz distribution 2 (Gauss distribution 1)\n"
                    )
                    f.write(
                        "   0.0000    0.0000    0.0000    !! stickiness parameter (for interactions only)\n"
                    )

                f.write("SPHERE\n")
                f.write(
                    "   0.0050    0.0000    1.0000    !! Volume fraction of the component (vesicle/micelle)\n"
                )
                f.write(
                    "   0.0000    0.0000    0.0000    !! Inner (core) radius of the sphere\n"
                )
                f.write(
                    "   0.0000    0.0000    0.0000    !! Inner (core) contrast of the sphere\n"
                )
                f.write(
                    "   0.4630    0.3307    0.6614    !! Outer (core+shell) radius of the sphere\n"
                )
                f.write(
                    "   1.0000    1.0000    1.0000    !! Outer (shell) contrast of the sphere\n"
                )
                f.write(
                    "   0.1653    0.1323    0.1984    !! Polydisperstiry on the sphere radius\n"
                )
                f.write(
                    "  13.2278   13.2278   13.2278    !! Hard-sphere radius (for interactions only)\n"
                )
                f.write(
                    "2                                !! Schulz distribution 2 (Gauss distribution 1)\n"
                )
                f.write(
                    "   0.0000    0.0000    0.0000    !! stickiness parameter (for interactions only)\n"
                )
                f.write(" 2                      !! ASCII format file\n")
                f.write(dat + "        !! Experimental data file\n")
                f.write(dat.split(".dat")[0] + "        !! Output prefix name\n")
                f.write(
                    "1                       !! Angular scale (1/2/3/4) as in GNOM\n"
                )
                f.write(
                    "1.0                     !! Exp. data portion to fit (from beginning)\n"
                )
                f.write(
                    'meth sb                 !! Minimization method sb - "simple bounds"\n'
                )
                f.write("loa maxit 1000           !! Maximum number of iterations\n")
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

                # ====================
                # Cluster submission.
                # ====================

                f2 = open(fn + "_clust.sh", "w")
                f2.write("#! /bin/bash\n")
                f2.write("#SBATCH --export=ALL\n")
                f2.write("#SBATCH --error=%x.stderrn")
                f2.write("#SBATCH --output=%x.stdout\n")
                f2.write("#SBATCH --mail-type=END,FAIL\n")
                f2.write("#SBATCH --mail-user=agruzinov@embl-hamburg.de\n")
                f2.write("source /apps/prod/atsas/atsas-env latest\n")
                f2.write("cd ${SLURM_SUBMIT_DIR}\n")
                f2.write("lipmix < " + fn + "\n")
                f2.close()
                os.system("sbatch " + fn + "_clust.sh")

                # ================================

                os.chdir("../")
    os.chdir("../")


# Arguments parser
parser = argparse.ArgumentParser(
    description="Wrap-up script to generate multiple input files for LIPMIX with "
    "iterative number of layers. Example: "
    "python "
    "lipmix_multilayer_autofinder.py -i test_lipmix_MLV.dat -l 1 -d 1"
)
parser.add_argument(
    "-l",
    "--layers",
    default=1,
    required=True,
    type=int,
    help="Total expected number of layers.",
)
parser.add_argument(
    "-d",
    "--distr",
    default=1,
    required=True,
    type=int,
    help="Total expected number of distributions.",
)
parser.add_argument(
    "-i",
    "--input",
    nargs="+",
    required=True,
    default="input.dat",
    type=str,
    help="Input dat file",
)
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
