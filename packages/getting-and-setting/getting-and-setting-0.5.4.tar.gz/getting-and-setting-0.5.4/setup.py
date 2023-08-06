# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['getting_and_setting']

package_data = \
{'': ['*']}

install_requires = \
['keyring>=23.5.1,<24.0.0',
 'requests>=2.27.1,<3.0.0',
 'tabulate>=0.8.9,<0.9.0',
 'typer>=0.4.1,<0.5.0']

entry_points = \
{'console_scripts': ['micli = getting_and_setting.mi_cli:app']}

setup_kwargs = {
    'name': 'getting-and-setting',
    'version': '0.5.4',
    'description': 'An interface to interact with the Ion Mi Api.',
    'long_description': None,
    'author': 'Kim Timothy Engh',
    'author_email': 'kimothy@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
