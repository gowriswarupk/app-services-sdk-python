"""
    Red Hat Openshift SmartEvents Fleet Manager

    The API exposed by the fleet manager of the SmartEvents service.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: openbridge-dev@redhat.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "rhoas-smart-events-mgmt-sdk"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="Red Hat Openshift SmartEvents Fleet Manager",
    author="Development Team",
    author_email="openbridge-dev@redhat.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Red Hat Openshift SmartEvents Fleet Manager"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description="""\
    The API exposed by the fleet manager of the SmartEvents service.  # noqa: E501
    """
)
