# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'programming docs'
copyright = '2024, trist007'
author = 'trist007'
release = '0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = ["sphinx_rtd_dark_mode"]

templates_path = ['_templates']
exclude_patterns = ['sphinx_rtd_theme']

import sphinx_rtd_theme

default_dark_mode = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only' : True,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'includehidden': True,
    'navigation_depth': 4,
    'titles_only': False
}

html_static_path = ['_static']
