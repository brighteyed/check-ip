from setuptools import setup

setup(
    name="check_ip",
    version="0.1",
    py_modules=["main"],
    install_requires=[
        "requests",
        "colorama",
    ],
    entry_points={
        "console_scripts": [
            "check_ip=main:main",
        ],
    },
)