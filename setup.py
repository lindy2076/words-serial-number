from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='wordlexord',
    version='0.0.2',
    description='This is a python package for having fun with words ordered by length and then lexicographically',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Aleksej Kosolapov',
    author_email='kakaporuqee@gmail.com',
    keywords=['words', 'order', 'ordered', 'lexicographically'],
    url='https://github.com/lindy2076/words-serial-number',
    download_url='https://github.com/lindy2076/words-serial-number/issues'
)

if __name__ == '__main__':
    setup(**setup_args)
