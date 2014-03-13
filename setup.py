from distutils.core import setup

setup(
    name='EdmodoApi',
    version='0.1.0',
    author='',
    author_email='',
    packages=['edmodoapi'],
    description='Simple wrapper for the Edmodo API',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests>= 2.2.1",
    ],
)
