from setuptools import setup, find_packages

setup(
    name='csv-summarizer',
    version='1.0.1',
    packages=find_packages(),
    description='Package for summarizing csv files',
    tests_require=['test'],
    author='Tadikonda, Vamsi',
    author_email='vamsitadikonda99@gmail.com',
    url='https://github.com/vamsitadikonda/csv-summarizer',
    python_requires='>=3.8',
    classifiers=[
        "License :: OSI Approved :: BSD 2-Clause",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Topic :: Homework2345",
    ],
    license='BSD 2-Clause'
)
