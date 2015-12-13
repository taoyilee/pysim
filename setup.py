try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'pysim',
    'author': 'Tao-Yi Lee',
    'url': 'https://github.com/taoyilee/pysim',
    'download_url': 'https://github.com/taoyilee/pysim',
    'author_email': 'tylee@ieee.org',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['pysim'],
    'scripts': [],
    'name': 'pysim'
}

setup(**config)
