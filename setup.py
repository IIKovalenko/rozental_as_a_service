from typing import Optional

from setuptools import setup, find_packages


package_name = 'rozental_as_a_service'


def get_version() -> Optional[str]:
    with open('rozental_as_a_service/__init__.py', 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith('__version__'):
            return line.split('=')[-1].strip().strip("'")


def get_long_description() -> str:
    with open('README.md') as f:
        return f.read()


setup(
    name=package_name,
    description='Package to find typos in russian text.',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    keywords='typos',
    version=get_version(),
    author='Ilya Lebedev',
    author_email='melevir@gmail.com',
    install_requires=['setuptools', 'tabulate>=0.8', 'requests>=2.22.0'],
    entry_points={
        'console_scripts': [
            'rozental = rozental_as_a_service.rozental:main',
        ],
    },
    url='https://github.com/Melevir/rozental_as_a_service',
    license='MIT',
    py_modules=[package_name],
    zip_safe=False,
)
