from setuptools import setup

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False

except ImportError:
    bdist_wheel = None


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
    cmdclass={'bdist_wheel': bdist_wheel},
)
