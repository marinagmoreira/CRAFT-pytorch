from setuptools import setup, find_packages

setup(
    name='craft',
    version='1.0.0',  # Adjust the version number as needed
    packages=find_packages(),
    install_requires=[
        'torch>=0.4.1.post2',
        'torchvision>=0.2.1',
        'opencv-python>=3.4.2.17',
        'scikit-image>=0.14.2',
        'scipy>=1.1.0'
    ],
    python_requires='>=3.6',  # Adjust based on the Python versions supported
)
