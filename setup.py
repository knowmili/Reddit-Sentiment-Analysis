from setuptools import setup, find_packages

setup(
    name='reddit_sentiment_analysis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'praw',
        'nltk',
        'textblob',
        'matplotlib',
        'wordcloud'
    ],
    entry_points={
        'console_scripts': [
            'reddit-sentiment=reddit_sentiment_analysis.main:main',
        ],
    },
    author='Milind',
    description='A CLI tool for Reddit sentiment analysis and visualizations.',
    python_requires='>=3.7',
)