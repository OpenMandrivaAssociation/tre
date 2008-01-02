%define name	tre
%define version	0.7.5
%define release	%mkrel 1

%define major 4
%define libname	%mklibname %{name} %{major}

Summary:	Lightweight, robust, and efficient POSIX compliant regexp matching library
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Libraries
Source0:	http://laurikari.net/tre/%{name}-%{version}.tar.bz2
URL:		http://ville.laurikari.net/tre/
BuildRequires:	libltdl-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
TRE is a lightweight, robust, and efficient POSIX compliant regexp
matching library with some exciting features such as approximate
matching. 

%package -n	%{libname}
Summary:	Lightweight, robust, and efficient POSIX compliant regexp matching library
Group:		System/Libraries

%description -n %{libname}
TRE is a lightweight, robust, and efficient POSIX compliant regexp
matching library with some exciting features such as approximate
matching. 

%package -n	agrep
Summary:	Approximate matching
Group:		File tools
Requires:	%{libname} = %{version}

%description -n agrep
Approximate pattern matching allows matches to be approximate,
that is, allows the matches to be close to the searched pattern
under some measure of closeness. TRE uses the edit-distance
measure (also known as the Levenshtein distance) where characters
can be inserted, deleted, or substituted in the searched text in
order to get an exact match. Each insertion, deletion, or
substitution adds the distance, or cost, of the match. TRE can
report the matches which have a cost lower than some given
threshold value. TRE can also be used to search for matches with
the lowest cost.

TRE includes a version of the agrep command line tool for
approximate regexp matching in the style of grep.  Unlike other
agrep implementations (like the one by Sun Wu and Udi Manber from
University of Arizona available) TRE agrep allows full regexps of
any length, any number of errors, and non-uniform costs for
insertion, deletion and substitution.

%package -n	%{libname}-devel
Summary:	Header files and libraries for developing apps with %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n	%{libname}-devel
TRE is a lightweight, robust, and efficient POSIX compliant regexp
matching library with some exciting features such as approximate
matching. 

%package -n	%{libname}-static-devel
Summary:	Static libraries for developing apps with %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{name}-devel = %{version}

%description -n %{libname}-static-devel
TRE is a lightweight, robust, and efficient POSIX compliant regexp
matching library with some exciting features such as approximate
matching. 

%prep

%setup -q

%build

./configure \
    --prefix=%{_prefix} \
    --datadir=%{_datadir} \
    --mandir=%{_mandir} \
    --libdir=%{_libdir} \
    --enable-static \
    --disable-rpath

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

%find_lang %name

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%doc doc/tre-syntax.html
%{_libdir}/*.so.*

%files -n agrep -f %name.lang
%defattr(-,root,root)
%{_bindir}/agrep
%{_mandir}/man1/*

%files -n %{libname}-devel
%defattr(-, root, root)
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/tre.pc
%{_includedir}/tre

%files -n %{libname}-static-devel
%defattr(-, root, root)
%{_libdir}/*.a


