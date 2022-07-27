# lipmix_utils

Set of python scripts to extend the capabilities of the LIPMIX software for analyzing small-angle scattering data from lipid systems (as part of the ATSAS package), for example, at cluster systems with SLURM queue management system. 

The scripts are provided "AS IS" and need to be adapted for the particular case, especially the initial parameters of the distributions and electron density peaks. Please refer to the manual of LIPMIX on the official webpage of the ATSAS package: https://www.embl-hamburg.de/biosaxs/manuals/lipmix.html.

If you use results from LIPMIX in your publication, please cite:

[P.V. Konarev, A.Y. Gruzinov, H.D.T. Mertens and D.I. Svergun (2021). Restoring structural parameters of lipid mixtures from small-angle X-ray scattering data. J Appl Cryst. 54, 169-179.](https://journals.iucr.org/j/issues/2021/01/00/fs5188/fs5188.pdf)

# Examples

## Simple example

```
python lipmix_multilayer_autofinder.py -l 1 -d 1 -i test_lipmix_MLV.dat
```

This command will create the simplest fit with one distribution and one bilayer. Data is shown for multilayer vesicles; therefore, the fit will not be optimal. Only for testing purposes.

## Batch example
```
python lipmix_multilayer_autofinder.py -l 3 -d 1 -i *.dat
```
This command will go over the sorted list of *.dat files in the current directory and attempt to fit the data with a maximum of 3 layers and 1 distribution. Results will be saved in a separate directory with the name of the current *.dat file. This task can be run on the local computer and be executed in a reasonable amount of time. Useful for time series or temperature scans.

Example curves are taken from [SASBDB](https://www.sasbdb.org/project/776/) database.

## Cluster example
```
python lipmix_multilayer_autofinder_SLURM.py -l 10 -d 1 -i test_lipmix_MLV.dat
```

This example tries to fit the multilayer vesicles data with up to 10 bilayers in different combinations. Parallel execution is recommended.
Please check the options in the "Cluster submission" section of the code for the particular cluster in use. The example is written based on the SLURM submission system. This example is used only for demonstration purposes and is most suited for the small number of bilayers expected (~3-5).

A total number of permutations for ten bilayers can be calculated as follows:
```
python calc_number_of_permutations.py -l 10 -d 1
Total number of permutations:  1023
```
Other examples:
```
python calc_number_of_permutations.py -l 3 -d 1
Total number of permutations:  7

python calc_number_of_permutations.py -l 5 -d 1
Total number of permutations:  31

python calc_number_of_permutations.py -l 7 -d 1
Total number of permutations:  127

python calc_number_of_permutations.py -l 20 -d 1
Total number of permutations:  1048575

python calc_number_of_permutations.py -l 25 -d 1
Total number of permutations:  33554431

python calc_number_of_permutations.py -l 30 -d 1
Total number of permutations:  1073741823
```
The cluster batch example repeats the following for the local execution for demonstration:
```
python lipmix_multilayer_autofinder_SLURM.py -l 3 -d 1 -i *.dat
```
Since the SLURM submissions are happening one after another, one needs to check the available resources. In the case of ten files and ten expected bilayers, this can result in 10230 simultaneous jobs on the cluster.

