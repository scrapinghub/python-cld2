#!/usr/bin/python

from distutils.core import setup, Extension
import distutils.core
import platform
import subprocess
import sys
import os

# Setup some define macros for compilation.
defines = [('CLD_WINDOWS', None)]
if platform.system() == 'Windows':
  defines.append(('WIN32', None))

# Test suite
class cldtest(distutils.core.Command):
    # user_options, initialize_options and finalize_options must be overriden.
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass

    def run(self):
        errno = subprocess.call([sys.executable, 'tests/cld_test.py'])
        raise SystemExit(errno)

module = Extension('cld',
                   language='c++',
                   include_dirs = ["/usr/include/cld2/public"],
                   library_dirs = "/usr/lib",
                   define_macros = defines,
                   libraries = ['cld'],
                   sources=['src/pycldmodule.cc'],
                   )

setup(name='chromium_compact_language_detector',
      version='0.2',
      author='Michael McCandless',
      author_email='mail@mikemccandless.com',
      description='Python bindings around Google Chromium\'s embedded compact language detection library',
      requires=['cld2'],
      ext_modules = [module],
      license = 'BSD',
      url = 'http://code.google.com/p/chromium-compact-language-detector/',
      classifiers = [
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: C++',
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic'
        ],
      cmdclass = {'test': cldtest},
      )
