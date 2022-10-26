from setuptools import setup

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 2.7'
    'Topic :: Software Development :: Libraries',
    'Topic :: Utilities',
]

setup(
    name='merge-requirements',
    version='1.0',
    keywords=['merge requirements', 'merge dependencies'],
    url='https://github.com/victorhos/merge_requirements',
    license='MIT',
    author='victorhos',
    author_email='victor.hos@gmail.com',
    description='simple lib for organize two requirements.txt in a unique requirements.txt file',
    packages=['merge_requirements'],
    scripts=['scripts/merge_requirements'],
    install_requires=['packaging'],
    classifiers=classifiers
)
