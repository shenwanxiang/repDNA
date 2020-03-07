__author__ = 'Fule Liu'

from distutils.core import setup

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

setup(name='repDNA',
      version='1.1.4',
      author='Bin Liu and Fule Liu',
      author_email='bliu@insun.hit.edu.cn and liufule12@gmail.com',
      maintainer='Fule Liu',
      maintainer_email='liufule12@gmail.com',
      url='http://bioinformatics.hitsz.edu.cn/repDNA/',
      description='a Python package to generate various modes of feature vectors for DNA sequences '
                  'by incorporating user-defined physicochemical properties and sequence-order effects',
      long_description=LONG_DESCRIPTION,
      download_url='http://bioinformatics.hitsz.edu.cn/repDNA/download',
      platforms=['MS Windows', 'Mac X', 'Unix/Linux'],
      license='GPL',
      keywords=['repDNA', 'DNA'],
      packages=['repDNA'],
      package_data={
          'repDNA': ['data/*.data', 'doc/*.pdf', 'example/*.*', 'test/*.*',
                     'data/12_trinucleotide_physicochemical_indices/*.txt',
                     'data/38_dinucleotide_physicochemical_indices/*.txt',
                     'data/6_dinucleotide_physicochemical_indices/*.txt']},
      data_files=[('', ['LICENSE', 'README.md', 'News.md'])],
      classifiers=['Intended Audience :: Science/Research',
                   'Intended Audience :: Developers',
                   'Development Status :: 5 - Production/Stable',
                   'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
                   'Natural Language :: English',
                   'Programming Language :: Python',
                   'Topic :: Software Development',
                   'Topic :: Scientific/Engineering',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX',
                   'Operating System :: Unix',
                   'Operating System :: MacOS',
                   'Programming Language :: Python :: 3',
                   'Topic :: Scientific/Engineering :: Bio-Informatics',
                   'Topic :: Software Development :: Libraries :: Python Modules'], )