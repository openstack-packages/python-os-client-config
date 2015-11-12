%{!?_licensedir:%global license %%doc}
%global pypi_name os-client-config

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        OpenStack Client Configuration Library
License:        ASL 2.0
URL:            https://github.com/openstack/%{pypi_name}
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
The os-client-config is a library for collecting client configuration for
using an OpenStack cloud in a consistent and comprehensive manner. It
will find cloud config for as few as 1 cloud and as many as you want to
put in a config file. It will read environment variables and config files,
and it also contains some vendor specific default values so that you don't
have to know extra info to use OpenStack

* If you have a config file, you will get the clouds listed in it
* If you have environment variables, you will get a cloud named `envvars`
* If you have neither, you will get a cloud named `defaults` with base defaults

%package -n python2-%{pypi_name}
Summary:        OpenStack Client Configuation Library
%{?python_provide:%python_provide python2-%{pypi_name}}
Obsoletes: python-%{pypi_name} < 1.7.3
# compat for previous Delorean Trunk package
Provides:       os-client-config

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr

BuildRequires:  python-appdirs
BuildRequires:  python-fixtures
BuildRequires:  python-glanceclient >= 0.18.0
BuildRequires:  python-jsonschema >= 2.0.0
BuildRequires:  python-keystoneauth1
BuildRequires:  python-keystoneclient >= 1.6.0
BuildRequires:  python-mock
BuildRequires:  python-oslotest >= 1.10.0
BuildRequires:  PyYAML

Requires:       python-setuptools
Requires:       python-fixtures
Requires:       python-appdirs
# TODO soft-deps
#Requires:       python-glanceclient >= 0.18.0
#Requires:       python-keystoneauth1
#Requires:       python-keystoneclient >= 1.6.0
Requires:       PyYAML

%description -n python2-%{pypi_name}
The os-client-config is a library for collecting client configuration for
using an OpenStack cloud in a consistent and comprehensive manner. It
will find cloud config for as few as 1 cloud and as many as you want to
put in a config file. It will read environment variables and config files,
and it also contains some vendor specific default values so that you don't
have to know extra info to use OpenStack

* If you have a config file, you will get the clouds listed in it
* If you have environment variables, you will get a cloud named `envvars`
* If you have neither, you will get a cloud named `defaults` with base defaults

%package  -n python2-%{pypi_name}-doc
Summary:        Documentation for OpenStack os-client-config library
%{?python_provide:%python_provide python2-%{pypi_name}-doc}

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx

%description -n python2-%{pypi_name}-doc
Documentation for the os-client-config library.


%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        OpenStack Client Configuation Library
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires:       python3-setuptools
Requires:       python3-fixtures
Requires:       python3-appdirs

%description -n python3-%{pypi_name}
The os-client-config is a library for collecting client configuration for
using an OpenStack cloud in a consistent and comprehensive manner. It
will find cloud config for as few as 1 cloud and as many as you want to
put in a config file. It will read environment variables and config files,
and it also contains some vendor specific default values so that you don't
have to know extra info to use OpenStack

* If you have a config file, you will get the clouds listed in it
* If you have environment variables, you will get a cloud named `envvars`
* If you have neither, you will get a cloud named `defaults` with base defaults

%package -n    python3-%{pypi_name}-doc
Summary:       Documentation for OpenStack os-client-config library
%{?python_provide:%python_provide python3-%{pypi_name}-doc}
Obsoletes: python-%{pypi_name}-doc < 1.7.3

BuildRequires: python3-sphinx
BuildRequires: python3-oslo-sphinx

%description -n python3-%{pypi_name}-doc
Documentation for the os-client-config library.
%endif

%prep
%setup -qc -n %{pypi_name}-%{upstream_version}

mv %{pypi_name}-%{upstream_version} python2

pushd python2

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

cp -p LICENSE ChangeLog CONTRIBUTING.rst PKG-INFO README.rst ../
popd

%if 0%{?with_python3}
cp -a python2 python3
%endif

%build
pushd python2
%py2_build
popd
%if 0%{?with_python3}
pushd python3
%py3_build
popd
%endif

%install
pushd python2
%py2_install
export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees   source build/html
# Fix hidden-file-or-dir warnings
rm -fr build/html/.buildinfo

# Fix this rpmlint warning
sed -i "s|\r||g" build/html/_static/jquery.js
popd
popd

%if 0%{?with_python3}
pushd python3
%py3_install
export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build-3 -b html -d build/doctrees   source build/html

# Fix hidden-file-or-dir warnings
rm -fr build/html/.buildinfo

# Fix this rpmlint warning
sed -i "s|\r||g" build/html/_static/jquery.js
popd
popd
%endif

%check
pushd python2
%{__python2} setup.py test
popd

%if 0%{?with_python3}
pushd python3
%{__python3} setup.py test
popd
%endif

%files -n python2-%{pypi_name}
%doc ChangeLog CONTRIBUTING.rst PKG-INFO README.rst
%license LICENSE
%{python2_sitelib}/os_client_config
%{python2_sitelib}/*.egg-info

%files -n python2-%{pypi_name}-doc
%license LICENSE
%doc python2/doc/build/html

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc ChangeLog CONTRIBUTING.rst PKG-INFO README.rst
%license LICENSE
%{python3_sitelib}/os_client_config
%{python3_sitelib}/*.egg-info

%files -n python3-%{pypi_name}-doc
%license LICENSE
%doc python3/doc/build/html
%endif

%changelog