from setuptools import setup

setup(
    name='clipit',
    version='1.0',
    py_modules=['clipboard'],  # clipboard.py nevű fájl
    entry_points={
        'console_scripts': [
            'clipit=clipboard:main',  # parancsnév=modul:függvény
        ],
    },
)
