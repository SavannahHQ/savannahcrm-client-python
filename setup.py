import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='savannahcrm-client',  
    version='0.1',
    author="Michael Hall",
    author_email="info@savannahhq.com",
    description="A client library for Savannah CRM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SavannahHQ/savannahcrm-client-python",
    packages=setuptools.find_packages(exclude=("tests")),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests',
    ],
)