# flake8: noqa

import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="erratacreator",
    version="0.1",
    author="Eyal Shenitzky",
    author_email="eshenitz@gmail.com",
    description="Tool for creating errata for oVirt products",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eshenitz/erratacreator",
    packages=["erratacreator"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Testing",
    ],
    entry_points = {
        'console_scripts': ['erratacreator=erratacreator.__main__:main'],
    }
)
