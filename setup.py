import setuptools

with open("README.md", mode="r", encoding="utf-8") as fh:
    long_description = fh.read()

REQUIRED_PACKAGES = [
    'jamo',
    'nltk',
    'konlpy',
    'python-mecab-ko',
]

setuptools.setup(
    name="g2pK",
    version="0.9.2",
    author="Kyubyong Park",
    author_email="kbpark.linguist@gmail.com",
    description="g2pK: g2p module for Korean",
    install_requires=REQUIRED_PACKAGES,
    license='Apache License 2.0',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kyubyong/g2pK",
    packages=setuptools.find_packages(),
    package_data={'g2pk': ['g2pk/idioms.txt', 'g2pk/rules.txt', 'g2pk/table.csv']},
    python_requires=">=3.6",
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
