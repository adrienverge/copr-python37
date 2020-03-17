# Copyright 2020 Adrien Vergé
# Inspired from official 'python36' spec file for EPEL7 (but greatly simplified)

%define _disable_source_fetch 0
%define __os_install_post %{nil}
%define __requires_exclude /usr/local/bin/python

Name: python37
Version: 3.7.7
Release: 2%{?dist}
Summary: Interpreter of the Python programming language
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

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
Interpreter of the Python programming language

%package libs
Summary: Python runtime libraries
%description libs
Python runtime libraries

%package devel
Summary: Libraries and header files needed for Python development
Requires: %{name} = %{version}-%{release}
%description devel
Libraries and header files needed for Python development

%package pip
Summary: A tool for installing and managing Python3 packages
Requires: %{name} = %{version}-%{release}
%description pip
A tool for installing and managing Python3 packages

%package tkinter
Summary: A GUI toolkit for Python
Requires: %{name} = %{version}-%{release}
%description tkinter
A GUI toolkit for Python

%package idle
Summary: A basic graphical development environment for Python
Requires: %{name} = %{version}-%{release}
%description idle
A basic graphical development environment for Python

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
%{_bindir}/python3*
%{_bindir}/pydoc3*
%{_bindir}/pyvenv*
%{_mandir}/man1/python3.7.*

%files libs
%{_exec_prefix}/lib/python3.7
%{_exec_prefix}/%{_lib}/python3.7
%{_exec_prefix}/%{_lib}/libpython3.7m.a
%{_exec_prefix}/%{_lib}/pkgconfig/python*.pc
%exclude %{_exec_prefix}/lib/python3.7/site-packages/pip
%exclude %{_exec_prefix}/%{_lib}/python3.7/tkinter
%exclude %{_exec_prefix}/%{_lib}/python3.7/idlelib

%files devel
%{_bindir}/2to3*
%{_includedir}/python3.7m

%files pip
%{_bindir}/pip3*
%{_bindir}/easy_install-3*
%{_exec_prefix}/lib/python3.7/site-packages/pip

%files tkinter
%{_exec_prefix}/%{_lib}/python3.7/tkinter

%files idle
%{_bindir}/idle3*
%{_exec_prefix}/%{_lib}/python3.7/idlelib

%changelog
* Tue Mar 17 2020 Adrien Vergé <adrienverge@gmail.com> 3.7.7-2
- Split into multiple packages for -libs, -devel, -pip

* Tue Mar 17 2020 Adrien Vergé <adrienverge@gmail.com> 3.7.7-1
- Initial RPM release
