# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'valorant.py'
copyright = '2021, frissyn'
author = 'frissyn'

# The full version, including alpha/beta/rc tags
release = "1.0.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'karma_sphinx_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# This is a function linkcode_resolve(domain, info), which should return the
# URL to source code corresponding to the object in given domain with given 
# information. The function should return None if no link is to be added.

intersphinx_mapping = {
    'py': ('https://docs.python.org/3', None),
    'aio': ('https://docs.aiohttp.org/en/stable/', None),
    'req': ('https://docs.python-requests.org/en/latest/', None)
}


def linkcode_resolve(domain, info):
    if domain != "py": return None
    if not info["module"]: return None
    
    name = info['fullname'].split('.')[0]
    base = "https://github.com/frissyn/valorant.py/blob/master"

    return base + {
        "Client": "/valorant/client.py",
        "AsyncClient": "/valorant/threads.py",
        "LocalClient": "/valorant/local.py"
    }[name]


def setup(app):
    if app.config.language == 'ja':
        app.config.intersphinx_mapping['py'] = ('https://docs.python.org/ja/3', None)
