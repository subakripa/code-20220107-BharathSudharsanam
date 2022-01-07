from setuptools import setup, find_packages

setup(
    name='BMI_Calculator',
    version='0.1',
    packages=find_packages(),
    license='Proprietary',
    author='Bharath S',
    description='',
    install_requires=[
        "pandas==1.3.5",
        "pytest==6.2.5",
        "Sphinx==1.6.3",
        "sphinx-rtd-theme==0.2.4"
    ]
)
