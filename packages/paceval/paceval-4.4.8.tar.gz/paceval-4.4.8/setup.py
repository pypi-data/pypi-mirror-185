#---------------------------------------------------------------------------
# Copyright 1997-2014. Version 1.x Joerg Koenning - All rights reserved.
# Copyright 2015-2022. Version 2.x, 3.x, 4.x 2015-2022 paceval.[Registered Trade Mark]
#                                            All rights reserved.
# Author(s) : paceval., see http://www.paceval.com
# Reference: https://app.swaggerhub.com/apis/paceval/paceval-service/4.04
# Documentation: https://pypi.org/project/paceval/
#---------------------------------------------------------------------------

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="paceval",                     # This is the name of the package
    version="4.4.8",                        # The initial release version
    author="paceval",                     # Full name of the author
    description="paceval with Python - the Mathematical Engine as a Service (e.g. for multi-party computations)",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["paceval"],             # Name of the python package
    package_dir={'':'paceval/src'},     # Directory of the source code of the package
    install_requires=['requests']                     # Install other dependencies if any
)