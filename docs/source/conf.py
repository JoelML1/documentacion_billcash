# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'BillCash'
copyright = '2025, joel medina, juan salinas, david torres'
author = 'joel medina, juan salinas, david torres'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# Archivos CSS personalizados
html_css_files = [
    'billcash_modern.css',
]

# Configuración del tema Alabaster con colores de BillCash
html_theme_options = {
    'logo': 'billcash_logo.png',
    'logo_name': False,
    'description': 'Sistema de gestión de pagos y facturación',
    'github_user': 'JoelML1',
    'github_repo': 'documentacion_billcash',
    'github_button': True,
    'github_type': 'star',
    'fixed_sidebar': True,
    'page_width': 'auto',
    'sidebar_width': '280px',
    'body_max_width': 'none',
}
