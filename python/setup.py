import os
import re
from setuptools import setup, find_packages


PACKAGE_NAME = 'seek_frame'
PACKAGE_DIR = os.path.dirname(__file__)
SCRIPT_DIR = os.path.join(PACKAGE_DIR, 'bin')


def read(fname):
    with open(fname, 'r') as f:
        return f.read()


def get_version(package):
    init_py_path = os.path.join(package, '__init__.py')
    init_py = read(init_py_path)
    # if __version__ isn't set, this will error out
    return re.search(r'''__version__ = ['"]([^'"]+)['"]''', init_py).group(1)


def get_script_path(name):
    return os.path.join(SCRIPT_DIR, name)


setup(
    name=PACKAGE_NAME,
    version=get_version(PACKAGE_NAME),
    author='Chuck Bassett',
    author_email='3101367+chucksmash@users.noreply.github.com',
    description='Match images against layers in a TIFF image',
    license='MIT',
    url='https://github.com/chucksmash/amnh-hack-2019.git',
    keywords='bse tiff amnh ct',
    packages=find_packages(exclude=['tests']),
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        # see requirements.txt yo
    ],
    scripts=[
        get_script_path('run-seek-frame'),
    ],
)
