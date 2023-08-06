[![Documentation Status](https://readthedocs.org/projects/rousepull/badge/?version=latest)](https://rousepull.readthedocs.io/en/latest/?badge=latest)

rousepull
=========

An implementation of the Rouse model of polymer dynamics. For [example usage](https://rousepull.readthedocs.org/en/latest/examples/01_Quickstart.html) and the full [API reference](https://rousepull.readthedocs.org/en/latest/rousepull.html) visit our documentation at [ReadTheDocs](https://rousepull.readthedocs.org/en/latest)

When using this code, please cite our original work:

> Keizer et al., Science 377, 2022; DOI: [10.1126/science.abi9810](https://doi.org/10.1126/science.abi9810)

To install `rousepull` you can use the latest stable version from [PyPI](https://pypi.org/project/rousepull)
```sh
$ pip install --upgrade rousepull
```
or the very latest updates right from GitHub:
```sh
$ pip install git+https://github.com/OpenTrajectoryAnalysis/rousepull
```

Developers
----------
Note the `Makefile`, which can be used to build the documentation (using
Sphinx); run unit tests and check code coverage; and build an updated package
for release with GNU `make`.

When editing the example notebooks,
[remember](https://nbsphinx.readthedocs.io/en/sizzle-theme/usage.html#Using-Notebooks-with-Git)
to remove output and empty cells before committing to the git repo.
[nbstripout](https://github.com/kynan/nbstripout) allows to do this
automatically upon commit.
