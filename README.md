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
