import re

from setuptools import setup


with open('requirements.txt', 'r') as fp:
    install_requires = [re.split(r'[<>=]', line)[0]
                        for line in fp if line.strip()]


with open('ironic_discoverd/__init__.py', 'rb') as fp:
    exec(fp.read())


setup(
    name = "ironic-discoverd",
    version = __version__,
    description = open('README.rst', 'r').readline().strip(),
    author = "Dmitry Tantsur",
    author_email = "dtantsur@redhat.com",
    url = "https://pypi.python.org/pypi/ironic-discoverd",
    packages = ['ironic_discoverd'],
    install_requires = install_requires,
    entry_points = {'console_scripts': [
        "ironic-discoverd = ironic_discoverd.main:main"
    ]},
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: OpenStack',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
    ],
    license = 'APL 2.0',
)
