from setuptools import setup, find_packages

 

classifiers = [

  'Development Status :: 5 - Production/Stable',

  'Intended Audience :: Education',

  'Operating System :: Microsoft :: Windows :: Windows 10',

  'License :: OSI Approved :: MIT License',

  'Programming Language :: Python :: 3'

]

 

setup(

  name='KaniniProjectStructure',

  version='0.0.1',

  description='To create the project structure',

  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),

  url='',  

  author='Sathish Kumar',

  author_email='sathishkumar.sk236@gmail.com',

  license='MIT',

  classifiers=classifiers,

  keywords='Project formater',

  packages=find_packages(),

  install_requires=['']

)