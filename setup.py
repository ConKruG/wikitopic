import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '1.1'
PACKAGE_NAME = 'wikitopic'
AUTHOR = 'Arash Kia and Finbarr Murphy'
AUTHOR_EMAIL = 'arash.nkia@gmail.com'
URL = 'https://github.com/ConKruG/wikitopic'

LICENSE = 'GNU GPL v3.0'
DESCRIPTION = 'Explicit online topic extraction for documents from Wikipedia'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'nltk',
      'wikipedia'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )
