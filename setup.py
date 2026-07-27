from setuptools import setup, find_packages

setup(
    name="Demand_IQ",
    version="0.1.0",
    author="Husnain Khalid",
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    install_requires=[],
)

