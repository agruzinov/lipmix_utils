#! /bin/bash
#SBATCH --export=ALL
#SBATCH --error=%x.stderrn#SBATCH --output=%x.stdout
#SBATCH --mail-type=END
#SBATCH --mail-user=agruzinov@embl-hamburg.de
source /apps/prod/atsas/atsas-env latest
cd ${SLURM_SUBMIT_DIR}
../../lipmix <test_lipmix_MLV_n_dist_1_[2_5_8_10]_304
