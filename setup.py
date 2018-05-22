#from distutils.core import setup, find_packages
from setuptools import setup, find_packages
setup(
  name = 'sticks',
  packages = find_packages(),
   entry_points={
         'console_scripts': [
             'sticks = sticks.__init__:main',
    ],
         },

#  packages = ['sticks'], # this must be the same as the name above
  version = '0.1',
  description = 'A game application',
  author = 'ganesh',
  author_email = 'ganeshhubale03@gmail.com',
  url = 'https://github.com/ganeshhubale/sticks', 
 # download_url = 'https://github.com/peterldowns/mypackage/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['testing', 'logging', 'sticks'], # arbitrary keywords
  py_modules=['sticks.__init__'],
  )

