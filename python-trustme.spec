%define module trustme
%bcond_with test

Name:		python-trustme
Version:	1.2.1
Release:	1
Summary:	#1 quality TLS certs while you wait, for the discerning tester
URL:		https://github.com/python-trio/trustme
License:	MIT OR Apache-2.0
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/t/trustme/trustme-%{version}.tar.gz

BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(cryptography)
BuildRequires:	python%{pyver}dist(idna)
# tests
BuildRequires:	python%{pyver}dist(attrs)
BuildRequires:	python%{pyver}dist(cffi)
BuildRequires:	python%{pyver}dist(coverage)
BuildRequires:	python%{pyver}dist(iniconfig)
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(pluggy)
BuildRequires:	python%{pyver}dist(pyasn1)
BuildRequires:	python%{pyver}dist(pycparser)
BuildRequires:	python%{pyver}dist(pyopenssl)
BuildRequires:	python%{pyver}dist(types-pyOpenSSL)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(service-identity)


%description
You wrote a cool network client or server. It encrypts connections using TLS.
Your test suite needs to make TLS connections to itself.

Uh oh. Your test suite probably doesn’t have a valid TLS certificate. Now what?

trustme is a tiny Python package that does one thing: it gives you a fake
certificate authority (CA) that you can use to generate fake TLS certs to use
in your tests. Well, technically they’re real certs, they’re just signed by
your CA, which nobody trusts. But you can trust it. Trust me.


%prep
%autosetup -n %{module}-%{version} -p1
# correct README.rst non-Unix EOL encoding.
sed -i 's/\r$//' README.rst

%build
%py_build

%install
%py_install

# tests run locally, disabled for abf.
%if %{with test}
%check
%{__python} -m pytest tests/
%endif

%files
%{python3_sitelib}/%{module}/*.py
%{python3_sitelib}/%{module}/*.typed
%{python3_sitelib}/%{module}/*/*.pyc
%{python3_sitelib}/%{module}-%{version}.dist-info
%doc README.rst
%license LICENSE