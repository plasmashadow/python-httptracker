
from setuptools import setup
import os


def Readme():
    return open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r').read()

setup(
    name='httptrack',
    packages=['httptrack'],
    version='0.0.5',
    description='',
    long_description=Readme(),
    author='plasmashadow',
    author_email='plasmashadowx@gmail.com',
    url='https://github.com/plasmashadow/python-httptrack.git',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Intended Audience :: Developers'
    ],
    install_requires=['six', 'bittorrent-bencode', 'requests'],
    include_package_data=True,
    license='BSD License',
)
