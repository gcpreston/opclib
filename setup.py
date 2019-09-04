from setuptools import setup, find_packages

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name='opclib',
    version='0.0.4',
    author='Graham Preston',
    author_email='graham.preston@gmail.com',
    description='A wrapper library for Open Pixel Control.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gcpreston/opclib',
    packages=find_packages(),
    package_dir={'opclib': 'opclib'},
    package_data={'opclib': ['bin/fcserver*']},
    zip_safe=False,
)
