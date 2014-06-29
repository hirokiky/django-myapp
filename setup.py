import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()


setup(
    name='django-myapp',
    version='0.0',
    packages=['myapp'],
    description='A example django package',
    long_description=README,
    author='Hiroki KIYOHARA',
    author_email='hirokiky@gmail.com',
    url='https://github.com/hirokiky/django-myapp/',
    license='MIT',
    install_requires=[
        'Django>=1.6,<1.7',
    ]
)
