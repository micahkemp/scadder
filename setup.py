from setuptools import setup, find_packages

setup(
    name="scadder",
    packages=find_packages(),
    install_requires=[
        "jinja2",
    ],
    include_package_data=True,
)
