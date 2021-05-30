from setuptools import setup
import re
import io

about = {}

__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
    io.open('MayaAutoPackageReloader/__init__.py', encoding='utf_8_sig').read()).group(1)


setup(
    name="MayaAutoPackageReloader",
    version=__version__,
)
