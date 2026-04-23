#
# Conditional build:
%bcond_with	tests	# regression tests programs
%bcond_without	gnome	# gtk-doc-manual in GNOME help format
#
Summary:	API documentation generation tool for GTK+ and GNOME
Summary(es.UTF-8):	El generador de documentación del GTK
Summary(pl.UTF-8):	Narzędzie do generowania dokumentacji API do GTK+ i GNOME
Summary(pt_BR.UTF-8):	O gerador de documentação do GTK
Name:		gtk-doc
Version:	1.36.1
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	https://download.gnome.org/sources/gtk-doc/1.36/%{name}-%{version}.tar.xz
# Source0-md5:	819b11aa730cf5108f1df3f0eec91cf9
Patch0:		%{name}-noarch.patch
Patch2:		%{name}-struct-end.patch
URL:		https://wiki.gnome.org/DocumentationProject/GtkDoc
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-style-xsl-nons >= 1.74.0
%{?with_tests:BuildRequires:	glib2-devel >= 1:2.68}
BuildRequires:	libxml2 >= 1:2.3.6
BuildRequires:	libxslt-progs >= 1.1.15
BuildRequires:	meson >= 0.64
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-pygments
%{?with_tests:BuildRequires:	python3-parameterized}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%{?with_gnome:BuildRequires:	yelp-tools}
Requires:	%{name}-automake = %{version}-%{release}
Requires:	docbook-dtd43-xml
Requires:	docbook-style-xsl-nons >= 1.74.0
Requires:	libxml2 >= 1:2.3.6
Requires:	libxslt-progs >= 1.1.15
Requires:	python3-pygments
# +for mkhtml2: python3-anytree python3-lxml
Conflicts:	pkgconfig < 1:0.19
BuildArch:	noarch
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
Requires:	pkgconfig
Conflicts:	glib2-devel < 1:2.10.0
Conflicts:	gtk-doc < 0:1.4-3

%description automake
Automake macros for gtk-doc.

%description automake -l pl.UTF-8
Makra automake'a do gtk-doc.

%package common
Summary:	Common directories for documetation generated using gtk-doc
Summary(pl.UTF-8):	Katalogi na dokumentację wygenerowaną za pomocą gtk-doc
Group:		Documentation

%description common
Common directories for API documentation for various packages,
generated using gtk-doc.

%description common -l pl.UTF-8
Katalogi na dokumentację API do różnych pakietów, wygenerowaną za
pomocą gtk-doc.

%prep
%setup -q
%patch -P0 -p1
%patch -P2 -p1

%{__mv} doc/README doc/README.docs

%build
%meson \
	%{!?with_tests:-Dtests=false} \
	%{!?with_gnome:-Dyelp_manual=false}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_gtkdocdir} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%meson_install

cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%if %{with gnome}
%find_lang gtk-doc-manual --with-gnome
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files %{?with_gnome:-f gtk-doc-manual.lang}
%defattr(644,root,root,755)
%doc NEWS README.md doc/*
%attr(755,root,root) %{_bindir}/gtkdoc-*
%attr(755,root,root) %{_bindir}/gtkdocize
%{_datadir}/cmake/GtkDoc
%{_datadir}/gtk-doc
%{_npkgconfigdir}/gtk-doc.pc
%{_examplesdir}/%{name}-%{version}

%files automake
%defattr(644,root,root,755)
%{_aclocaldir}/gtk-doc.m4

%files common
%defattr(644,root,root,755)
%dir %{_docdir}/gtk-doc
%dir %{_gtkdocdir}
