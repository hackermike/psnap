import setuptools
import os.path
import sys

try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements

script_dir = os.path.dirname(os.path.realpath(__file__))

def load_requirements(fname):
    reqs = parse_requirements(fname, session="test")
    return [str(ir.req) for ir in reqs]

with open("README.md", "r") as fh:
    long_description = fh.read()
    if sys.version_info[0] == 2 and sys.version_info[1] >= 7:
        install_requires = load_requirements("{}/requirements-python2.txt".format(script_dir)),
    elif sys.version_info[0] > 3 or (sys.version_info[0] == 3 and sys.version_info[1] >= 5):
        install_requires = load_requirements("{}/requirements.txt".format(script_dir)),
    else:
        raise Exception("Must be using Python 2.7+ or 3.5+")
setuptools.setup(
     name='psnap',  
     version='0.7.1',
     scripts=['scripts/psnap', 'scripts/psnap_example', 'scripts/psnap_example2'] ,
     author="Michael Frandsen",
     author_email="wfrandsen@gmail.com",
     description="Snapshot script output to json and expand keywords in source file.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/hackermike/psnap",
     packages=setuptools.find_packages(),
     install_requires=install_requires,
     classifiers=[
         "Programming Language :: Python :: 2",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
