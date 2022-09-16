from distutils.core import setup

setup(
    name='FloydWarshallRecursive',
    version='0.1.0',
    author = 'Jason Hadwen',
    packages=['floydWarshall', 'tests',],
    scripts = ['floyd_warshall_imperative.py', 'floyd_warshall_recursive.py'],
    url = 'https://github.com/jasonshhh/Mid-Module-Assessment',
    license='Apache 2.0',
    description = 'Rewriting the Floyd Warshall Algorithm to use recursion',
    long_description=open('README.md').read(),
    install_requires = "python >= 3.1.0",
)
