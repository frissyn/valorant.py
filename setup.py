import valorant
import setuptools

readme = open("README.md", "r").read()
url = "https://github.com/frissyn/valorant.py"

setuptools.setup(
    name="valorant",
    license="MIT",
    author="frissyn",
    description=valorant.__doc__,
    version=valorant.__version__,

    url=url,
    project_urls={
        "Source Code": url,
        "Pull Requests": url + "/pulls",
        "Issue Tracker": url + "/issues",
        "Documentation": "https://valorantpy.readthedocs.io/"
    },

    long_description=readme,
    long_description_content_type="text/markdown",

    python_requires=">=3.8.0",

    zip_safe=False,
    packages=["valorant", "valorant/local", "valorant/objects"],

    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development"
    ]
)