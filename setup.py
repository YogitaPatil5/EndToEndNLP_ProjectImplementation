from setuptools import find_packages, setup

setup(
    name="hate-speech-classification",
    version="0.0.1",
    author="Yogita",
    author_email="yogitarajput.04@gmail.com",
    packages=find_packages(),
    install_requires=[],
)







#Use pyproject.toml: The preferred way to specify editable installations is by creating a pyproject.toml file. This will provide a more modern and standardized way to handle your package installations.

#Use --use-pep517: This flag tells pip to use PEP 517 to build the package, which is the new standard for building Python packages. You can try installing your package using the following command:
# 
#pip install --use-pep517 -e .

#Use --config-settings editable_mode=compat: This flag tells pip to use the editable mode with the compatibility option. You can try installing your package using the following command:
#pip install --config-settings editable_mode=compat -e .

