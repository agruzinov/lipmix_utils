#! /bin/bash
#SBATCH --partition=ps
#SBATCH --error=%x.stderrn#SBATCH --output=%x.stdout
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=andrey.gruzinov@desy.de
cd ${SLURM_SUBMIT_DIR}
/software/atsas/3.0.4/bin/lipmix < SASDG82_n_dist_1_[2]_2
