# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['RPA', 'RPA.Cloud.AWS']

package_data = \
{'': ['*']}

install_requires = \
['amazon-textract-response-parser>=0.1.33,<0.2.0',
 'boto3>=1.24.76,<2.0.0',
 'robotframework-pythonlibcore>=4.0.0,<5.0.0',
 'robotframework>=4.0.0,!=4.0.1,<6.0.0',
 'rpaframework-core>=10.0.0,<11.0.0']

setup_kwargs = {
    'name': 'rpaframework-aws',
    'version': '5.2.6',
    'description': 'AWS library for RPA Framework',
    'long_description': 'rpaframework-aws\n================\n\nThis library enables Amazon Web Services (AWS) for `RPA Framework`_\nlibraries, such as Textract.\n\n.. _RPA Framework: https://rpaframework.org\n',
    'author': 'RPA Framework',
    'author_email': 'rpafw@robocorp.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://rpaframework.org/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
