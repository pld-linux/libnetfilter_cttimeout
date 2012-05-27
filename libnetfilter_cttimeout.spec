Summary:	A userspace library for Netfilter/conntrack timeout policy tuning
Summary(pl.UTF-8):	Biblioteka przestrzeni użytkownika do zmiany parametrów limitów czasu Netfiltra/conntracka
Name:		libnetfilter_cttimeout
Version:	1.0.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://www.netfilter.org/projects/libnetfilter_cttimeout/files/%{name}-%{version}.tar.bz2
# Source0-md5:	7697437fc9ebb6f6b83df56a633db7f9
URL:		http://www.netfilter.org/projects/libnetfilter_cttimeout/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6
BuildRequires:	libmnl-devel >= 1.0.0
BuildRequires:	libtool >= 2:2.0
BuildRequires:	pkgconfig >= 1:0.9.0
Requires:	libmnl >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libnetfilter_cttimeout is a userspace library allowing timeout
policy tuning for Netfilter/conntrack. This infrastructure allows you
to define fine-grain timeout policies per flow.

%description -l pl.UTF-8
libnetfilter_cttimeout to biblioteka przestrzeni użytkownika
pozwalająca na strojenie polityki limitów czasu dla
Netfiltra/conntracka. Ta infrastruktura pozwala na definiowanie
szczegółowych polityk limitów czasu dla poszczególnych przepływów
danych.

%package devel
Summary:	Header files for libnetfilter_cttimeout library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libnetfilter_cttimeout
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libmnl-devel >= 1.0.0

%description devel
Header files for libnetfilter_cttimeout library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libnetfilter_cttimeout.

%package static
Summary:	Static libnetfilter_cttimeout library
Summary(pl.UTF-8):	Statyczna biblioteka libnetfilter_cttimeout
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnetfilter_cttimeout library.

%description static -l pl.UTF-8
Statyczna biblioteka libnetfilter_cttimeout.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libnetfilter_cttimeout.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnetfilter_cttimeout.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnetfilter_cttimeout.so
%{_libdir}/libnetfilter_cttimeout.la
%{_includedir}/libnetfilter_cttimeout
%{_pkgconfigdir}/libnetfilter_cttimeout.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnetfilter_cttimeout.a
