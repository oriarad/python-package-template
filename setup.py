from setuptools import setup

setup(name='mypackage',
      version='0.1',
      description='A description of mypackage',
      url='http://github.com/oriarad/python-package-template',
      author='Ori Arad',
      author_email='aradori@hotmail.com',
      license='MIT',
      packages=['mypackage'],
      install_requires=[
          'requests',
      ],
      include_package_data=True,      
      zip_safe=False)
