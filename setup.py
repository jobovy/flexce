import os, os.path
from setuptools import setup

NAME = 'flexCE'
# do not use x.x.x-dev.  things complain.  instead use x.x.xdev
VERSION = '1.0.1dev'
RELEASE = 'dev' not in VERSION

yld_files= []
os.chdir('flexCE')
for (dirpath, dirnames, filenames) in os.walk(os.path.join('data')):
    yld_files+= [os.path.join(dirpath,file) for file in filenames]
os.chdir('..')

setup(name=NAME,
      version=VERSION,
      description='Flexible Galactic Chemical Evolution Model',
      author='Brett Andrews',
      author_email='brett.h.andrews@gmail.com',
      url='https://github.com/bretthandrews/flexCE',
      license='MIT',
      packages=['flexCE','flexCE.fileio'],
      package_data={'flexCE': yld_files})
