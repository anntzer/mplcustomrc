# find_namespace_packages itself bounds support to setuptools>=40.1.
from setuptools import find_namespace_packages, setup


setup(
    name="mplcustomrc",
    description="",
    long_description=open("README.rst", encoding="utf-8").read(),
    author="Antony Lee",
    author_email="",
    url="",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    cmdclass={},
    py_modules=[],
    packages=find_namespace_packages("lib"),
    package_dir={"": "lib"},
    package_data={},
    python_requires=">=3.8",
    setup_requires=["setuptools_scm"],
    use_scm_version=lambda: {
        "version_scheme": "post-release",
        "local_scheme": "node-and-date",
    },
    install_requires=[
    ],
    entry_points={
        "console_scripts": [],
        "gui_scripts": [],
    },
)
