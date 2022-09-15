from setuptools import setup, find_packages

setup(
    name="floyd-recursive",
    version="0.1",
    author="Jason Hadwen",
    author_email="sgjhadwe@liverpool.ac.uk",
    url="https://github.com/jasonshhh/Mid-Module-Assessment",
    py_modules=["mid_module_assessment/floyd_warshall_recursive", "mid_module_assessment/floyd_warshall_iterative"],
    license="Apache 2.0",
    python_version="3.10",
    packages=find_packages(include=['mid_module_assessment'])
)
