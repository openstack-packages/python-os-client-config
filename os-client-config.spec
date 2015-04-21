# Created by pyp2rpm-1.1.1
%global pypi_name os-client-config

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        1%{?dist}
Summary:        OpenStack Client Configuation Library

License:        ASL %(TODO: version)s
URL:            http://www.openstack.org/
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-devel
BuildRequires:  python-pbr
BuildRequires:  python-sphinx


%description
===============================
os-client-config
===============================

os-client-config is a library for collecting
client configuration for
using an OpenStack cloud in a consistent and
comprehensive manner. It
will find cloud config for as few as 1 cloud and as
many as you want to
put in a config file. It will read environment variables
and config files,
and it also contains some ...


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# generate html docs 
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}



%files
%doc html README.rst LICENSE
%{python2_sitelib}/ 
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/os_client_config-%{version}-py?.?.egg-info

%changelog
* Tue Apr 21 2015 Alan <apevec@gmail.com> - 0.8.0-1
- Initial package.
