Name: cppunit
Version: 1.12.1
Release: 2

Summary: C++ Port of JUnit Testing Framework
License: LGPL
Group: Development/Libraries
Url: http://cppunit.sourceforge.net/
Source: ftp://download.sourceforge.net/pub/sourceforge/cppunit/cppunit-%version.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
CppUnit is the C++ port of the famous JUnit framework for unit testing.
Test output is in XML for automatic testing and GUI based for supervised tests.

%package doc
Summary: HTML formatted API documention for Log for C++
Group: Development/Libraries
Requires: %name = %version

%description doc
The %name-doc package contains HTML formatted API documention generated by
the popular doxygen documentation generation tool.

%prep
%setup -q

%build
%configure --enable-doxygen
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT/%{_datadir}/cppunit

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/cppunit-config
%{_bindir}/DllPlugInTester
%{_includedir}/cppunit/*
%{_mandir}/man1/*
%{_datadir}/aclocal/*
%{_libdir}/libcppunit*.so.*
%{_libdir}/libcppunit.so
%{_libdir}/libcppunit.a
%doc AUTHORS COPYING INSTALL NEWS README THANKS ChangeLog TODO BUGS doc/FAQ

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig
 
%files doc
%doc doc/html/*

%changelog
* Mon Jul  4 2005 Patrice Dumas <dumas@centre-cired.fr>  
- update using the fedora template  
* Sat Apr 14 2001 Bastiaan Bakker <bastiaan.bakker@lifeline.nl>
- Initial release
