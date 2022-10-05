from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in compact_theme_for_frappe_13/__init__.py
from compact_theme_for_frappe_13 import __version__ as version

setup(
	name="compact_theme_for_frappe_13",
	version=version,
	description=" Compact Theme For Frappe 13",
	author="Fintechsys",
	author_email="info@fintechsys.net",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
