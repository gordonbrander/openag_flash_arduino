import os
import sys
from setuptools import setup, find_packages

if sys.version_info < (2,7) or sys.version_info.major > 2:
    sys.exit('Only Python 2.7 is supported')

readme_path = os.path.join(os.path.dirname(__file__), "README.rst")
with open(readme_path) as f:
    readme = f.read()

setup(
    name='openag_flash_arduino',
    version='0.0.1',
    author='Open Agriculture Initiative',
    description='Tools for flashing Arduino with OpenAg firmware',
    long_description=readme,
    license="GPL",
    url="https://github.com/OpenAgInitiative/openag_flash_arduino",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 2.7",
    ],
    packages=find_packages(exclude=("tests", "tests.*")),
    install_requires=[
        'openag',
        'click>=6.6'
    ],
    include_package_data=True,
    entry_points={
        # 'console_scripts': [
        #     'openag=openag.cli:main'
        # ]
    }
)
