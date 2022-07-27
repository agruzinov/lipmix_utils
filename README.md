# lipmix_utils

Set of python scripts to extend the capabilities of the LIPMIX software for analyzing small-angle scattering data from lipid systems (as part of the ATSAS package) for example at cluster systems with SLURM queue management system.

Please refer to the manual of LIPMIX on the official webpage of the ATSAS package: https://www.embl-hamburg.de/biosaxs/manuals/lipmix.html

If you use results from LIPMIX in your own publication, please cite:

[P.V. Konarev, A.Y. Gruzinov, H.D.T. Mertens and D.I. Svergun (2021). Restoring structural parameters of lipid mixtures from small-angle X-ray scattering data. J Appl Cryst. 54, 169-179.](https://journals.iucr.org/j/issues/2021/01/00/fs5188/fs5188.pdf)

# Examples

## Simple example

```
python lipmix_multilayer_autofinder.py -l 1 -d 1 -i test_lipmix_MLV.dat

```

This command will create the simplest fit with one distribution and one bilayer. Data is shown for multilayer vesicles. Therefore fit will be not optimal. Only for testing purposes.

## Batch example
```
python lipmix_multilayer_autofinder.py -l 3 -d 1 --batch -i *.dat

```
This command will go over the sorted list of *.dat files in the current directory and will attempt to fit the data with maximum of 3 layers and one distribution. Results will be saved in the separate directory with the name of current *.dat file. In case of small amount of bilayers this can be run on the local computer and be executed in the resonable abount of time. Useful for time series or temperature scans.

Example curves are taken from [SASBDB](https://www.sasbdb.org/project/776/) database.



