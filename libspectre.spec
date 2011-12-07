Name:           libspectre
Version:        0.2.4
Release:        1%{?dist}
Summary:        A library for rendering PostScript(TM) documents

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://libspectre.freedesktop.org
Source0:        http://libspectre.freedesktop.org/releases/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: ghostscript-devel >= 8.61

%description
%{name} is a small library for rendering PostScript(TM) documents. 
It provides a convenient easy to use API for handling and rendering 
PostScript documents.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc ChangeLog
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libspectre.pc


%changelog
* Mon Mar 22 2010  Marek Kasik <mkasik@redhat.com> - 0.2.4-1
- Update to 0.2.4
- Resolves: #575899

* Fri Jan  8 2010  Marek Kasik <mkasik@redhat.com> - 0.2.3-1
- Update to 0.2.3
- Fix mixed use of spaces and tabs in spec file
- Related: #543948

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.2.2-3.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec  3 2008  Matthias Clasen <mclasen@redhat.com> - 0.2.2-1
- Update to 0.2.2

* Sun Aug 10 2008  Matthias Clasen <mclasen@redhat.com> - 0.2.1-1
- Update to 0.2.1

* Sat Feb  9 2008  Matthias Clasen <mclasen@redhat.com> - 0.2.0-2
- Rebuild for gcc 4.3

* Tue Jan 29 2008  Matthias Clasen <mclasen@redhat.com> - 0.2.0-1
- Initial packaging 
