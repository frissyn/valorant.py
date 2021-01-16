import setuptools

from valorant import __version__

with open("docs/about.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="valorant",
    version=__version__,
    author="IreTheKID",
    author_email="author@example.com",
    description="An unofficial synchronous client package for interacting with Riot Games' Valorant API endpoints.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IreTheKID/valorant.py",
    packages=["valorant"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
