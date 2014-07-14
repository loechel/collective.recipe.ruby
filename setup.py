# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pkg_resources import get_distribution, DistributionNotFound

import os

__version__ = '0.0.1'
__name__='collective.recipe.ruby'

setup(
    name=__name__,
    version=__version__,
    url='https://github.com/loechel/collective.recipe.ruby',
    license='Apache Software License v2',
    author='Alexander Loechel',
    author_email='Alexander.Loechel@lmu.de',
    description='',
    long_description=open('README.rst').read() + '\n' + 
                     open(os.path.join('docs', 'HISTORY.rst')).read(),
    keywords='ruby recipe zc ',
    packages=find_packages('src',exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['collective', 'collective.recipe'],
    include_package_data=True,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'collective.recipe.cmmi',
        'ipython',
        'ipdb',
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    entry_points = {
        'zc.buildout': [
            'default = %s:Recipe' % __name__, 
            ]
    },
    )
