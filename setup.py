# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os

setup(
    name='test',
    version="1.0.0",
    packages=['guoshuai'],
    url='https://github.com/guos825/test_package',
    license='MIT',
    author='Guo Shuai',
    author_email='448139528@qq.com',
    description='GS Test SDK for Python',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    long_description=open(
        os.path.join(os.path.dirname(__file__), "README.md"), 'r').read(),
    install_requires=[]
)