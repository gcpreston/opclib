from setuptools import setup, find_packages

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name='opclib',
    version='0.0.6',
    author='Graham Preston',
    author_email='graham.preston@gmail.com',
    description='A wrapper library for Open Pixel Control.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gcpreston/opclib',
    packages=find_packages(exclude=('opclib.tests',)),
    package_dir={'opclib': 'opclib'},
    package_data={'opclib': ['bin/fcserver*']},
    include_package_data=True,
    zip_safe=False,
    # python_requires='>=3.7',  # TODO: Test other Python versions
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    project_urls={
        'Source': 'https://github.com/gcpreston/opclib',
    }
)
