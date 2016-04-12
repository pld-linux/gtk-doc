#
# Conditional build:
%bcond_with	tests	# build regression tests programs
%bcond_without	gnome	# build without gtk-doc-manual in GNOME help format
#
%include	/usr/lib/rpm/macros.perl
#
Summary:	API documentation generation tool for GTK+ and GNOME
Summary(es.UTF-8):	El generador de documentación del GTK
Summary(pl.UTF-8):	Narzędzie do generowania dokumentacji API do GTK+ i GNOME
Summary(pt_BR.UTF-8):	O gerador de documentação do GTK
Name:		gtk-doc
Version:	1.25
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtk-doc/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	0dc6570953112a464a409fb99258ccbc
Patch0:		%{name}-noarch.patch
URL:		http://www.gtk.org/rdp/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-style-xsl >= 1.74.0
%{?with_tests:BuildRequires:	glib2-devel >= 1:2.6.0}
%{?with_tests:BuildRequires:	libtool}
BuildRequires:	libxslt-progs >= 1.1.15
BuildRequires:	perl-base >= 1:5.18.0
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	python >= 1:2.3
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.446
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%{?with_gnome:BuildRequires:	yelp-tools}
Requires:	%{name}-automake = %{version}-%{release}
Requires:	docbook-dtd43-xml
Requires:	docbook-style-dsssl >= 1.77
Requires:	docbook-style-xsl >= 1.74.0
Requires:	docbook-utils >= 0.6.10
Requires:	libxslt-progs >= 1.1.15
Requires:	openjade
Requires:	perl-base >= 1:5.18.0
Requires:	source-highlight
Conflicts:	pkgconfig < 1:0.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtk-doc is a tool for generating API reference documentation. It is
used for generating the documentation for GTK+, GLib and GNOME.

%description -l pl.UTF-8
gtk-doc jest narzędziem do generowania dokumentacji API. Jest używany
do generowania dokumentacji GLib, GTK+ i GNOME.

%package automake
Summary:	Automake macros for gtk-doc
Summary(pl.UTF-8):	Makra automake'a do gtk-doc
Group:		Development/Tools
Requires:	automake
Conflicts:	gtk-doc < 0:1.4-3
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description automake
Automake macros for gtk-doc.

%description automake -l pl.UTF-8
Makra automake'a do gtk-doc.

%package common
Summary:	Common directories for documetation generated using gtk-doc
Summary(pl.UTF-8):	Katalogi na dokumentację wygenerowaną za pomocą gtk-doc
Group:		Development
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description common
Common directories for API documentation for various packages,
generated using gtk-doc.

%description common -l pl.UTF-8
Katalogi na dokumentację API do różnych pakietów, wygenerowaną za
pomocą gtk-doc.

%prep
%setup -q
%{!?with_tests:%patch0 -p1}
mv -f doc/README doc/README.docs

%build
%{?with_tests:%{__libtoolize}}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	HIGHLIGHT="%{_bindir}/source-highlight" \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_gtkdocdir} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%if %{with gnome}
%find_lang gtk-doc-manual --with-gnome
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files %{?with_gnome:-f gtk-doc-manual.lang}
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS TODO README doc/*
%attr(755,root,root) %{_bindir}/gtkdoc-*
%attr(755,root,root) %{_bindir}/gtkdocize
%dir %{_libdir}/cmake/GtkDoc
%{_libdir}/cmake/GtkDoc/GtkDocConfig.cmake
%{_libdir}/cmake/GtkDoc/GtkDocConfigVersion.cmake
%{_libdir}/cmake/GtkDoc/GtkDocScanGObjWrapper.cmake
%{_datadir}/gtk-doc
%{_npkgconfigdir}/gtk-doc.pc
%{_datadir}/sgml/%{name}
%{_examplesdir}/%{name}-%{version}

%files automake
%defattr(644,root,root,755)
%{_aclocaldir}/gtk-doc.m4

%files common
%defattr(644,root,root,755)
%dir %{_docdir}/gtk-doc
%dir %{_gtkdocdir}
