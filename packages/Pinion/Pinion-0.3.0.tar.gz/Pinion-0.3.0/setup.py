# -*- coding: utf-8 -*-

import setuptools
import versioneer

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Pinion",
    python_requires='>=3.7',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Jan Mrázek",
    author_email="email@honzamrazek.cz",
    description="Create interactive pinout diagrams for KiCAD PCBs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yaqwsx/Pinion",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "click>=7.1",
        "ruamel.yaml",
        "pcbdraw>=1.0",
        "pcbnewTransition >= 0.2, <=0.4"
    ],
    setup_requires=[
        "versioneer"
    ],
    zip_safe=False,
    include_package_data=True,
    entry_points = {
        "console_scripts": [
            "pinion=pinion.ui:cli"
        ],
    }
)
