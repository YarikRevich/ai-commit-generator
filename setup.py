from distutils.core import setup

setup(
    name='ai-commit-generator',
    version='1.0',
    description='Git extension, which uses AI model to generate commit messages',
    author='Yaroslav Svitlytskyi',
    author_email='yariksvitlitskiy81@gmail.com',
    packages=['openai'],
)