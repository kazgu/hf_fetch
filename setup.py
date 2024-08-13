#!/usr/bin/env python


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
    'requests',
    'beautifulsoup4'
]


setuptools.setup(
    name="hf_fetch",
    version="0.1.0",
    author="kazgu",
    author_email="hasanjan@outlook.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kazgu/hf_fetch",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    package=['hf_fetch'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # scripts=['easyml/cortex/main.py'],
    entry_points={  # Optional
    'console_scripts': [
         'hf-fetch=hf_fetch.hf_fetch:main',
         'hf-fetchm=hf_fetch.hf_fetch:main2',
    ],
},
package_data={}

)
