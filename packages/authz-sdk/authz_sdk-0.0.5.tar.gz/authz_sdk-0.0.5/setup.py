from distutils.core import setup
setup(
  name = 'authz_sdk',
  packages = ['authz_sdk', 'authz_sdk.interceptor', 'authz_sdk.validate'],
  version = '0.0.5',
  license='MIT',
  description = 'Authz Python SDK',
  author = 'Vincent Composieux',
  author_email = 'authz@composieux.fr',
  url = 'https://github.com/eko/authz-python-sdk',
  download_url = 'https://github.com/eko/authz-python-sdk/archive/refs/tags/v0.0.5.tar.gz',
  keywords = ['authorization', 'authz', 'sdk', 'abac', 'rbac'],
  install_requires=[
          'grpcio',
          'protobuf',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.10',
  ],
)