%define major 5
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	Lightweight, robust, and efficient POSIX compliant regexp matching library
Name:		tre
Version:	0.8.0
Release:	2
License:	GPL
Group:		System/Libraries
Source0:	http://laurikari.net/tre/%{name}-%{version}.tar.bz2
URL:		https://laurikari.net/tre/
BuildRequires:	libltdl-devel

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

%package -n	%{develname}
Summary:	Header files and libraries for developing apps with %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{EVRD}
Provides:	lib%{name}-devel = %{EVRD}

%description -n	%{develname}
TRE is a lightweight, robust, and efficient POSIX compliant regexp
matching library with some exciting features such as approximate
matching. 

%prep
%setup -q

%build
%configure \
    --disable-static \
    --disable-rpath

%make

%install
%makeinstall_std

%find_lang %name

%files -n %{libname}
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%doc doc/tre-syntax.html
%{_libdir}/*.so.%{major}*

%files -n agrep -f %name.lang
%{_bindir}/agrep
%{_mandir}/man1/*

%files -n %{develname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/tre.pc
%{_includedir}/tre
