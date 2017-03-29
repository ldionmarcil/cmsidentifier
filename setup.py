from setuptools import setup

setup(
    name = 'pentets',
    version = '0.1',
    url = 'https://github.com/ldionmarcil/LOG515',
    license = 'MIT',
    author = '*',
    author_email='*',
    description='CMS Spider',
    packages=['pentets', 'tests'],
    test_suite='tests',
    install_requires=[
        'PyYAML>=3.12',
        'pycurl>=7.43',
        'testfixtures>=4.13',
    ]
)
