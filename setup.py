"""Setup file for ams-ml-python-course."""

from setuptools import setup

PACKAGE_NAMES = ['module_4']

KEYWORDS = [
    'machine learning', 'deep learning', 'artificial intelligence',
    'data mining', 'weather', 'meteorology', 'thunderstorm', 'wind', 'tornado'
]

SHORT_DESCRIPTION = 'Python library for AMS 2019 short course.'

LONG_DESCRIPTION = (
    'Python library for short course (Machine Learning in Python for '
    'Environment) at 2019 AMS (American Meteorological Society) annual meeting.'
)

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7'
]

if __name__ == '__main__':
    setup(name='ams2019_short_course',
          version='0.1',
          description=SHORT_DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license='MIT',
          author='Ryan Lagerquist',
          author_email='ryan.lagerquist@ou.edu',
          url='https://github.com/thunderhoser/ams2019_short_course',
          packages=PACKAGE_NAMES,
          scripts=[],
          keywords=KEYWORDS,
          classifiers=CLASSIFIERS,
          include_package_data=True,
          zip_safe=False)
