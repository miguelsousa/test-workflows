from setuptools import setup

setup(
    name="dummy",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    author="Miguel Sousa",
    author_email="msousa@adobe.com",
    description="Dummy project",
    url="https://github.com/miguelsousa",
    license="MIT",
    platforms=["Any"],
    package_dir={'': 'lib'},
    packages=['dummy'],
    python_requires='>=3.6',
    install_requires=['fontTools[woff]>=3.1.0'],
)
