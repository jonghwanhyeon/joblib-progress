from setuptools import setup, find_packages

with open('README.md', 'r') as input_file:
    long_description = input_file.read()

setup(
    name='joblib-progress',
    version='1.0.1',
    description='A contextmanager to track progress of joblib execution',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jonghwanhyeon/joblib-progress',
    author='Jonghwan Hyeon',
    author_email='jonghwanhyeon93@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Home Automation',
    ],
    keywords=['joblib', 'progress', 'rich'],
    packages=find_packages(),
    install_requires=['joblib', 'rich'],
)