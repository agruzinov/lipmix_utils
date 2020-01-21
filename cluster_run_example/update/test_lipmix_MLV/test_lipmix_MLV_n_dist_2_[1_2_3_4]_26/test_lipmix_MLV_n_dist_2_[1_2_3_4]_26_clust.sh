#! /bin/bash
#SBATCH --export=ALL
#SBATCH --error=%x.stderrn#SBATCH --output=%x.stdout
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=agruzinov@embl-hamburg.de
source /apps/prod/atsas/atsas-env latest
cd ${SLURM_SUBMIT_DIR}
lipmix < test_lipmix_MLV_n_dist_2_[1_2_3_4]_26
