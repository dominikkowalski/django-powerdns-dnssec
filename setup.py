#!/usr/bin/env python

import json
import os
try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages


with open(
    os.path.join(os.path.dirname(__file__), 'README.rst'),
    encoding='utf-8'
) as f:
    long_description = f.read()

with open('version.json') as f:
    version = '.'.join(str(part) for part in json.load(f))

setup(
    name = 'django-powerdns-dnssec',
    version = version,
    url = 'https://github.com/allegro/django-powerdns-dnssec',
    license = 'BSD',
    description = 'PowerDNS administration app for Django',
    long_description = long_description,
    author = 'Peter Nixon, Łukasz Langa, Dominik Kowalski, Krzysztof Zygmunt, pylabs Team',
    author_email = 'pylabs@allegro.pl',
    packages = [p for p in find_packages() if not p.startswith('example')],
    include_package_data = True,
    platforms = 'any',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: Name Service (DNS)',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires = [
        'cov-core==1.15.0',
        'coverage==4.1',
        'dj.choices==0.10.0',
        'django-auth-ldap==1.2.8',
        'django-autocomplete-light==2.3.3',
        'django-extensions==1.6.7',
        'django-filter==0.15.2',
        'django-nose==1.4.4',
        'django-rest-swagger==0.3.8',
        'django-threadlocals==0.8',
        'django-jsonfield==1.0.0',
        'Django==1.8.17',
        'djangorestframework==3.3.2',
        'docutils==0.12',
        'factory-boy==2.7.0',
        'fake-factory==0.5.8',
        'gunicorn==19.6.0',
        'IPy==0.83',
        'jira==1.0.3',
        'mysqlclient==1.3.7',
        'nose==1.3.7',
        'nose-cov==1.6',
        'oauthlib==1.1.2',
        'pyhermes==0.2.0',
        'python-dateutil==2.5.3',
        'PyYAML==3.11',
        'raven==5.20.0',
        'requests==2.10.0',
        'requests-oauthlib==0.6.1',
        'requests-toolbelt==0.6.2',
        'rules==1.1.1',
        'setuptools==24.0.2',
        'six==1.10.0',
        'tlslite==0.4.9',
        'typing==3.5.2.2',
        'wheel==0.29.0'
    ],
    extras_require = {
        'docs': [
            'docutils>=0.12',
        ],
        'dnsaas': [
            'Django==1.8.17',
            'django-extensions==1.6.7',
            # 3.3.3 includes bug, https://github.com/rtfd/readthedocs.org/issues/2101
            'djangorestframework==3.3.2',
            'django-rest-swagger==0.3.8',
            'django-filter==0.15.2',
            'mysqlclient==1.3.7',
            'raven==5.20.0'
        ],
        # https://github.com/pypa/pip/issues/1197#issuecomment-228939212
        'tests': [
            'django-nose>=1.4',
            'nose-cov>=1.6',
            'factory_boy>=2.5.2',
        ]
    },
    tests_require = [
        'django-powerdns-dnssec[dnsaas]',
        'django-powerdns-dnssec[tests]',
    ],
    zip_safe = False,  # if only because of the readme file
)
