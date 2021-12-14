#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyotp
Version  : 2.6.0
Release  : 26
URL      : https://github.com/pyauth/pyotp/archive/v2.6.0/pyotp-2.6.0.tar.gz
Source0  : https://github.com/pyauth/pyotp/archive/v2.6.0/pyotp-2.6.0.tar.gz
Summary  : Python One Time Password Library
Group    : Development/Tools
License  : MIT
Requires: pyotp-license = %{version}-%{release}
Requires: pyotp-python = %{version}-%{release}
Requires: pyotp-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
PyOTP - The Python One-Time Password Library
============================================

%package license
Summary: license components for the pyotp package.
Group: Default

%description license
license components for the pyotp package.


%package python
Summary: python components for the pyotp package.
Group: Default
Requires: pyotp-python3 = %{version}-%{release}

%description python
python components for the pyotp package.


%package python3
Summary: python3 components for the pyotp package.
Group: Default
Requires: python3-core
Provides: pypi(pyotp)

%description python3
python3 components for the pyotp package.


%prep
%setup -q -n pyotp-2.6.0
cd %{_builddir}/pyotp-2.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1612488675
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyotp
cp %{_builddir}/pyotp-2.6.0/LICENSE %{buildroot}/usr/share/package-licenses/pyotp/7d4c495b3c3598bb8c23eeb5a4e964a04bdb257f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyotp/7d4c495b3c3598bb8c23eeb5a4e964a04bdb257f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
