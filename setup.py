#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for tidalytics.

    This file was generated with PyScaffold 2.5.7, a tool that easily
    puts up a scaffold for your new Python project. Learn more under:
    http://pyscaffold.readthedocs.org/
"""

import sys
from setuptools import setup
import versioneer
setup(version = versioneer.get_version(),
      cmdclass = versioneer.get_cmdclass(),
      entry_points={
          'gui_scripts': [
              'tidalytics = tidalytics.core:main'
          ]
      })

def setup_package():
    needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
    sphinx = ['sphinx'] if needs_sphinx else []
    setup(setup_requires=['six', 'pyscaffold>=2.5a0,<2.6a0'] + sphinx,
          use_pyscaffold=True)


if __name__ == "__main__":
    setup_package()
