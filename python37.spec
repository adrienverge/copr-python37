# Copyright 2020 Adrien Vergé
# Inspired from official 'python36' spec file for EPEL7 (but greatly simplified)

%define _disable_source_fetch 0
%define __os_install_post %{nil}
%define __requires_exclude /usr/local/bin/python

Name: python37
Version: 3.7.7
Release: 1%{?dist}
Summary: Unofficial Python 3.7 package for CentOS 7
License: Python
URL: https://www.python.org
Source: https://www.python.org/ftp/python/%{version}/Python-%{version}.tar.xz

BuildRequires: bzip2-devel
BuildRequires: gcc
BuildRequires: libffi-devel
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig
BuildRequires: readline-devel

Patch102: 00102-lib64.patch

%description
Unofficial Python 3.7 package for CentOS 7

%prep
%setup -q -c -n %{name}-%{version}
cd Python-%{version}
%if "%{_lib}" == "lib64"
%patch102 -p1
%endif

%build
cd Python-%{version}
%configure --enable-optimizations
%make_build build_all

%install
cd Python-%{version}
%make_install
rm %{buildroot}%{_mandir}/man1/python3.1*

%files
%{_bindir}/2to3*
%{_bindir}/easy_install-3*
%{_bindir}/idle3*
%{_bindir}/pip3*
%{_bindir}/pydoc3*
%{_bindir}/python3*
%{_bindir}/pyvenv*
%{_exec_prefix}/lib/python3.7
%{_exec_prefix}/%{_lib}/python3.7
%{_exec_prefix}/%{_lib}/libpython3.7m.a
%{_exec_prefix}/%{_lib}/pkgconfig/python*.pc
%{_includedir}/python3.7m
%{_mandir}/man1/python3.7.*

%changelog
* Tue Mar 17 2020 Adrien Vergé <adrienverge@gmail.com> 3.7.7-1
- Initial RPM release
