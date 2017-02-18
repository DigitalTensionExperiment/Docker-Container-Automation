from setuptools import setup

setup(
    name='PyFlask Task',
    version='1.0',
    py_modules=['dockcli'],
    install_requires=[
        'click',
        'docker',
        'docker-py',
    ],
    entry_points='''
        [console_scripts]
        dockcli=dockcli:cli
    ''',
)