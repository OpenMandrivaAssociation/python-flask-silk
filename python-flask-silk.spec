%global mod_name	Flask-Silk

Name:		python-flask-silk
Version:	0.1.1
Release:	4
Summary:	Adds silk icons to your Flask application or module, or extension
License:	BSD
URL:		http://github.com/mitsuhiko/flask-silk/
Source0:	http://pypi.python.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	python-flask
BuildRequires:	python-setuptools
Requires:	python-flask

%description
Adds silk icons to your Flask application or module, or extension.

%prep
%setup -q -n %{mod_name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root $RPM_BUILD_ROOT

%files
%doc PKG-INFO README
%{python_sitelib}/*-nspkg.pth
%{python_sitelib}/*.egg-info/
%{python_sitelib}/flaskext/silk
