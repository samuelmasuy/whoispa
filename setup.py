from setuptools import setup

setup(
    name='whoispa',
    version='0.1',
    py_modules=['whoispa'],
    install_requires=[
        'Click',
        'requests',
        'simplejson',
        'colorama'
    ],
    entry_points='''
        [console_scripts]
        whoispa=whoispa:main
    ''',
)
