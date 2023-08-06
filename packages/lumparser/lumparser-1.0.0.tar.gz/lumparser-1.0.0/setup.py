from distutils.core import setup
from setuptools import find_namespace_packages


setup(
    name='lumparser',
    packages=find_namespace_packages(where="src"),
    package_dir={'': 'src'},
    version='1.0.0',
    include_package_data=True,
    requires=['numpy', 'scipy', 'matplotlib']
)
