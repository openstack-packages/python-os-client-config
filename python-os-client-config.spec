# Created by pyp2rpm-1.1.1
%global pypi_name os-client-config

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        OpenStack Client Configuration Library

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx

# compat for previous Delorean Trunk package
Provides:       os-client-config

Requires:       PyYAML >= 3.1.0
Requires:       python-appdirs
# soft dep
Requires:       python-keystoneclient >= 1.1.0


%description
os-client-config is a library for collecting client configuration for
using an OpenStack cloud in a consistent and comprehensive manner.
It will find cloud config for as few as 1 cloud and as many as you want
to put in a config file. It will read environment variables and config
files, and it also contains some vendor specific default values so that
you don't have to know extra info to use OpenStack.


%prep
%setup -q -n %{pypi_name}-%{upstream_version}


%build
%{__python2} setup.py build

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%license LICENSE
%doc html README.rst
%{python2_sitelib}/os_client_config
%{python2_sitelib}/*.egg-info

%changelog
