#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-javaproperties
Version  : 0.8.1
Release  : 21
URL      : https://files.pythonhosted.org/packages/68/52/d7db7b671e2d4596c759fb526864837677c1562462e45f0ba46aef9a28c5/javaproperties-0.8.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/68/52/d7db7b671e2d4596c759fb526864837677c1562462e45f0ba46aef9a28c5/javaproperties-0.8.1.tar.gz
Summary  : Read & write Java .properties files
Group    : Development/Tools
License  : MIT
Requires: pypi-javaproperties-license = %{version}-%{release}
Requires: pypi-javaproperties-python = %{version}-%{release}
Requires: pypi-javaproperties-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
.. image:: http://www.repostatus.org/badges/latest/active.svg
:target: http://www.repostatus.org/#active
:alt: Project Status: Active - The project has reached a stable, usable
state and is being actively developed.

%package license
Summary: license components for the pypi-javaproperties package.
Group: Default

%description license
license components for the pypi-javaproperties package.


%package python
Summary: python components for the pypi-javaproperties package.
Group: Default
Requires: pypi-javaproperties-python3 = %{version}-%{release}

%description python
python components for the pypi-javaproperties package.


%package python3
Summary: python3 components for the pypi-javaproperties package.
Group: Default
Requires: python3-core
Provides: pypi(javaproperties)

%description python3
python3 components for the pypi-javaproperties package.


%prep
%setup -q -n javaproperties-0.8.1
cd %{_builddir}/javaproperties-0.8.1
pushd ..
cp -a javaproperties-0.8.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653338381
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-javaproperties
cp %{_builddir}/javaproperties-0.8.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-javaproperties/c2a412dfea07d82b46c697714f9431f34a48eb62
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
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-javaproperties/c2a412dfea07d82b46c697714f9431f34a48eb62

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
