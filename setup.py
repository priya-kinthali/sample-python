from setuptools import setup, find_packages, __version__, __version_tuple__, release
 
setup(
    name='samplepython02',
    version=__version__,    
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages()
)
