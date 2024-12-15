from setuptools import setup, find_packages

setup(
    name="coffee_machine",
    version="0.1",
    packages=find_packages(),
    install_requires=["PyQt6"],
    entry_points={
        'console_scripts': [
            'coffee-machine = App.main:main',
        ],
    },
)
