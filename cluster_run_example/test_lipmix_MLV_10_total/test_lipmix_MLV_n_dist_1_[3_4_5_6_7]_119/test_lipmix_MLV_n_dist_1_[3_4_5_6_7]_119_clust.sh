#! /bin/bash
#SBATCH --export=ALL
#SBATCH --error=%x.stderrn#SBATCH --output=%x.stdout
#SBATCH --mail-type=ALL
#SBATCH --mail-user=agruzinov@embl-hamburg.de
source /apps/prod/atsas/atsas-env latest
cd ${SLURM_SUBMIT_DIR}
../../lipmix <test_lipmix_MLV_n_dist_1_[3_4_5_6_7]_119