from setuptools import setup

setup(
    name="unlucky",
    entry_points={"console_scripts": ["unlucky = unlucky:cli"]},
    packages=["unlucky"]
)
