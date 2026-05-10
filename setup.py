from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in kb_customers/__init__.py
from kb_customers import __version__ as version

setup(
	name="kb_customers",
	version=version,
	description="Custom module for KB Customers in ERPNext",
	author="Your Name",
	author_email="your.email@example.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)