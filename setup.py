import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='easytello',
    version='0.0.6',
    author='Ezra Fielding',
    author_email='ezra.fielding@gmail.com',
    description='An easy framework to support DJI Tello scripting in Python 3',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Virodroid/easyTello',
    packages=setuptools.find_packages(),
    install_requires=[
        'opencv-python'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)