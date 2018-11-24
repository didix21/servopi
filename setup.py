from setuptools import setup

setup(name='servopi',
      version='1.0.0',
      license='MIT',
      author='Didac Coll',
      author_email='didaccoll_93@hotmail.com',
      maintainer='Didac Coll',
      maintainer_email='didaccoll_93@hotmail.com',
      description='This Python package contains a tool that allows to control servo motors in raspberry pi. '
                  'You can define a servo motor in a easy way without worrying about setting the raspberry pi PWM.'
                  ' Moreover, you can move your servo motor using angles.',
      long_description=open('./doc/source/README.rst').read(),
      platforms=['Python 3.6'],
      packages=['servopi'],
      include_package_data=True,
      zip_safe=False,
      url='https://github.com/didix21/servopi',
      project_urls={
        'Documentation': 'https://github.com/didix21/servopi',
        'Say Thanks!': 'https://github.com/didix21/',
        'Source': 'https://github.com/didix21/servopi',
      },
      classifiers=['Development Status :: 4 - Beta',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3.0',
                   'Programming Language :: Python :: 3.1',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.6',
                   'Topic :: Utilities',
                   'License :: OSI Approved :: MIT License'])
