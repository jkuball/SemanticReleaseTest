import setuptools

from test import __version__

setuptools.setup(
    name="Test", # Replace with your own username
    version=__version__,
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description="No long desc",
    long_description_content_type="text/plain",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
