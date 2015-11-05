%global upname pyezminc
%{!?__python2: %global __python2 %__python}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name:           python-pyezminc
Version:        1.0
Release:        1%{?dist}
Summary:        Python interface to MINC , using cython and EZminc library
License:        GPLv2
URL:            https://github.com/BIC-MNI/pyezminc
Source0:        %{upname}.tar.gz
BuildRequires:  python-devel, zlib-devel,i numpy, scipy, Cython, Cython >= 0.17, minc-toolkit >= 0.3.16
%description
PYEZMINC is a python module to read and write MINC files.

%prep
%setup -n %{upname}

%build
%py2_build

%install
%py2_install

%files
%doc
%{python2_sitelib}/*
%{python2_sitearch}/*

%changelog
* Wed Nov  4 2015 Adrian Alves <alvesadrian@fedoraproject.org> 1.0-1
- Initial Build
