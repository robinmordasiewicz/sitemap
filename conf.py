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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import f5_sphinx_theme


# -- Project information -----------------------------------------------------

project = 'Home'
copyright = '2022, Robin Mordasiewicz'
author = 'Robin Mordasiewicz'

# The full version, including alpha/beta/rc tags
release = '202202152222'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = [
#]
extensions = [
    "sphinxcontrib.youtube",
    'sphinx_copybutton'
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
#html_theme = ''

#html_sidebars = {'**': ['searchbox.html', 'localtoc.html', 'globaltoc.html']}

#html_theme_options = {
#                        'site_name': 'Solutions',
#                        'next_prev_link': True,
#                        'html_last_updated_fmt': '%Y-%m-%d %H:%M:%S'
#                        # 'base_url' = ''                            \\ DEFAULTS TO '/'
#                     }


html_theme = "f5_sphinx_theme"
html_theme_path = f5_sphinx_theme.get_html_theme_path()
html_sidebars = {"**": ["searchbox.html", "localtoc.html", "globaltoc.html"]}
html_theme_options = {
    "site_name": "Sitemap",
    "next_prev_link": True
}

#html_last_updated_fmt = "%Y-%m-%d %H:%M:%S"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_copy_source = False
