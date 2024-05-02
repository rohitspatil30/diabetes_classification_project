import setuptools

with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

SRC_REPO = 'diabetes_classification_project'
AUTHOR_USER_NAME = 'rohitspatil30'
AUTHOR_EMAIL = 'rohitspatil30@gmail.com'
REPO_NAME = 'diabetes_classification_project'

setuptools.setup(
    name=SRC_REPO,
    version='0.0.0',
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='This is a diabetes classification project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rohitspatil30/diabetes_classification_project',
    packages=setuptools.find_packages(where='src'),
    project_urls={
        'Bug tracker': 'https://github.com/rohitspatil30/diabetes_classification_project/issues',
    },
    package_dir={'': 'src'},

)

# error in setup.py: No matching '(' in 'setuptools.setup'-> solution: setup.py: 