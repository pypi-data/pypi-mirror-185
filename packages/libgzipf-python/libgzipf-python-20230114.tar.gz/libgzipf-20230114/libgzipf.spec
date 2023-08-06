Name: libgzipf
Version: 20230114
Release: 1
Summary: Library to access the GZIP file format
Group: System Environment/Libraries
License: LGPLv3+
Source: %{name}-%{version}.tar.gz
URL: https://github.com/libyal/libgzipf
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:              zlib
BuildRequires: gcc              zlib-devel

%description -n libgzipf
Library to access the GZIP file format

%package -n libgzipf-static
Summary: Library to access the GZIP file format
Group: Development/Libraries
Requires: libgzipf = %{version}-%{release}

%description -n libgzipf-static
Static library version of libgzipf.

%package -n libgzipf-devel
Summary: Header files and libraries for developing applications for libgzipf
Group: Development/Libraries
Requires: libgzipf = %{version}-%{release}

%description -n libgzipf-devel
Header files and libraries for developing applications for libgzipf.

%package -n libgzipf-python3
Summary: Python 3 bindings for libgzipf
Group: System Environment/Libraries
Requires: libgzipf = %{version}-%{release} python3
BuildRequires: python3-devel

%description -n libgzipf-python3
Python 3 bindings for libgzipf

%package -n libgzipf-tools
Summary: Several tools for reading GZIP files
Group: Applications/System
Requires: libgzipf = %{version}-%{release} fuse-libs
BuildRequires: fuse-devel

%description -n libgzipf-tools
Several tools for reading GZIP files

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=%{_libdir} --mandir=%{_mandir} --enable-python3
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -n libgzipf
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/*.so.*

%files -n libgzipf-static
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/*.a

%files -n libgzipf-devel
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/*.so
%{_libdir}/pkgconfig/libgzipf.pc
%{_includedir}/*
%{_mandir}/man3/*

%files -n libgzipf-python3
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/python3*/site-packages/*.a
%{_libdir}/python3*/site-packages/*.so

%files -n libgzipf-tools
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%changelog
* Sat Jan 14 2023 Joachim Metz <joachim.metz@gmail.com> 20230114-1
- Auto-generated

