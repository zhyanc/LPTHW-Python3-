try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

config = {
    'description': 'MakingSentence',
    'author': 'Joe YANG',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'noreason_2@hotmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex49'],
    'scripts': [],
    'name': 'MakingSentence_test_ex48'
    }

setup(**config)
