from setuptools import setup

setup(
    name='crypto',
    version='1.0',
    packages=['gdax_connector',
              'bitfinex_connector',
              'common_components'],
    url='http://github.com/redbanies3ofthem/crypto',
    license='TBD',
    author='Jonathan',
    author_email='jonathan.m.sadighian@gmail.com',
    description='Connector to record crypto exchange level 3 market data',
    install_requires=['requests', 'asyncio', 'sortedcontainers', 'numpy', 'websockets',
                      'arctic', 'pytz', 'pandas', 'datetime']
)
