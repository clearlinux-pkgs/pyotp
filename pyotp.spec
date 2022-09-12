#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyotp
Version  : 2.7.0
Release  : 27
URL      : https://github.com/pyauth/pyotp/archive/v2.7.0/pyotp-2.7.0.tar.gz
Source0  : https://github.com/pyauth/pyotp/archive/v2.7.0/pyotp-2.7.0.tar.gz
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
%setup -q -n pyotp-2.7.0
cd %{_builddir}/pyotp-2.7.0
pushd ..
cp -a pyotp-2.7.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1662997431
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyotp
cp %{_builddir}/pyotp-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pyotp/7d4c495b3c3598bb8c23eeb5a4e964a04bdb257f || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
