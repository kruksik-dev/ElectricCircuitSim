# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Electric Circuit Simulator"
copyright = "2025, Maciej Krakowiak"
author = "Maciej Krakowiak"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "breathe",
]

templates_path = ["_templates"]
exclude_patterns = exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "src/cpp/src/*",
    "src/cpp/include/*",
]

autodoc_typehints = "description"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
    "style_external_links": True,
}
html_static_path = ["_static"]

breathe_projects = {"Electric Circuit Simulator": "./xml"}  # Update this path if needed
breathe_default_project = "Electric Circuit Simulator"
