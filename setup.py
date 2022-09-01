from setuptools import setup

setup(name='google_images_hunter',
      version='1.0.0',
      license='MIT',
      author='David Romero',
      email='davidromerorodriguez21@gmail.com',
      packages=['google_images_hunter'],
      url='pendiente',
      download_url='pendiente',
      description='Selenium-based web scraper to perform massive image downloads from Google Images search engine.',
      keywords=['web scraping', 'scraping', 'selenium', 'images', 'image scraping'],
      install_requires=[
            'selenium',
            'pandas'],
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Programming Language :: Python",
                   'Programming Language :: Python :: 3',
                   "Topic :: Text Processing :: Markup :: HTML",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   ]
      )