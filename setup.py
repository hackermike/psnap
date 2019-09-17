import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='psnap',  
     version='0.1',
     scripts=['scripts/psnap', 'scripts/psnap_example'] ,
     author="Michael Frandsen",
     author_email="wfrandsen@gmail.com",
     description="Snapshot script output to json and expand keywords in source file.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/mikefrandsen/psnap",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
