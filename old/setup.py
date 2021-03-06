from setuptools import setup, find_packages

setup(
    name='cB4S2',
    version='2015.12.14',
    url='',
    license='Creative Commons Attribution-ShareAlike 4.0 International License',
    author='André Hollstein',
    author_email='andre.hollstein@gfz-potsdam.de',
    description='',
    scripts=['cB4S2.py'],
    packages=[],
    install_requires=['glymur', 'numpy', 'scipy', 'dill', 'gdal', 'psutil',
                      'matplotlib', 'matplotlib','stopit']
)
