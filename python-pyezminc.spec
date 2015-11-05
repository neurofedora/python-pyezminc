%global modname pyezminc
%global commit 4f7a4e5f28a7a8e44a5633d6f50018537fb46d9b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{modname}
Version:        1.0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Python interface to MINC, using cython and EZminc library
License:        GPLv2+
URL:            https://github.com/BIC-MNI/pyezminc
Source0:        https://github.com/BIC-MNI/pyezminc/archive/%{commit}/%{modname}-%{shortcommit}.tar.gz

BuildRequires:  zlib-devel
BuildRequires:  gcc-c++

%description
PYEZMINC is a python module to read and write MINC files.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel Cython
# Test deps
BuildRequires:  python2-nose
BuildRequires:  numpy scipy
Requires:       numpy scipy

%description -n python2-%{modname}
PYEZMINC is a python module to read and write MINC files.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel python3-Cython
# Test deps
BuildRequires:  python3-nose
BuildRequires:  python3-numpy python3-scipy
Requires:       python3-numpy python3-scipy

%description -n python3-%{modname}
PYEZMINC is a python module to read and write MINC files.

Python 3 version.

%prep
%autosetup -n %{modname}-%{commit}
# no RPATH
sed -i -e '/runtime_library_dirs/d' setup.py
# sheband forbidden for modules
sed -i -e '1d' minc.py
# path to test data from MINC
sed -i -e "/DATA_PATH/s/'.*'/'%{_datadir}/minc/icbm152_model_09c'/" test_pyezminc.py

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
nosetests-%{python2_version} -v
nosetests-%{python3_version} -v

%files -n python2-%{modname}
%license COPYING
%doc README
#{python2_sitearch}/%{modname}*

%files -n python3-%{modname}
%license COPYING
%doc README
#{python3_sitearch}/%{modname}*

%changelog
* Thu Nov 05 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0-0.1.git4f7a4e5
- Many fixes

* Wed Nov  4 2015 Adrian Alves <alvesadrian@fedoraproject.org> 1.0-0
- Initial Build
