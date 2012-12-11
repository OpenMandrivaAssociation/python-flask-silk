%global mod_name	Flask-Silk

Name:		python-flask-silk
Version:	0.1.1
Release:	1
Summary:	Adds silk icons to your Flask application or module, or extension
Group:		Development/Python
License:	BSD
URL:		http://github.com/mitsuhiko/flask-silk/
Source0:	http://pypi.python.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-flask
Requires:	python-flask
%py_requires -d

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


%changelog
* Fri Aug 17 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1.1-1
+ Revision: 815260
- Import python-flask-silk
- Import python-flask-silk

