try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

config = {
    'description': 'Game Test Ex47',
    'author': 'Joe Y',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'noreason_2@hotmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'projectname'
    }

setup(**config)
