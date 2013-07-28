from os.path import join, dirname
from setuptools import setup, find_packages

this_dir = dirname(__file__)

setup(
    name = 'trix_simplified',
    description = "trix_simplified",
    license = 'TBD',
    author = 'TBD',
    maintainer = 'Jonathan Ringstad',
    maintainer_email = 'jonathri@student.matnat.uio.no',
    packages = find_packages( exclude=['ez_setup'] ),
    install_requires = [ 
        'setuptools',
        'Django',
        'devilry',
        'devilry_theme',
        'devilry_usersearch',
        'devilry_extjsextras',
        'djangorestframework'],
    include_package_data = True,
    long_description = open( join( this_dir, 'README.rst' ) ).read().strip(),
    zip_safe = False,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Indended Audience :: End Users/Desktop',
        'License :: OSI Approved',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
