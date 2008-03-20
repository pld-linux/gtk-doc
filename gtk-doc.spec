#
%include	/usr/lib/rpm/macros.perl
#
Summary:	API documentation generation tool for GTK+ and GNOME
Summary(es.UTF-8):	El generador de documentación del GTK
Summary(pl.UTF-8):	Narzędzie do generowania dokumentacji API do GTK+ i GNOME
Summary(pt_BR.UTF-8):	O gerador de documentação do GTK
Name:		gtk-doc
Version:	1.10
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtk-doc/1.10/%{name}-%{version}.tar.bz2
# Source0-md5:	cbd4be396b0cf8b8ce1fc9b927cdf451
URL:		http://www.gtk.org/rdp/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml >= 1.0-10
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-utils
BuildRequires:	gnome-common >= 2.12.0-3
BuildRequires:	libxslt-progs >= 1.1.15
BuildRequires:	openjade
BuildRequires:	perl-base >= 5.6.0
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	scrollkeeper >= 1:0.3.5
Requires(post,postun):	scrollkeeper
Requires:	%{name}-automake = %{version}-%{release}
Requires:	docbook-dtd412-xml >= 1.0-10
Requires:	docbook-style-dsssl >= 1.77
Requires:	docbook-style-xsl >= 1.55.0-3
Requires:	docbook-utils >= 0.6.10
Requires:	gnome-doc-tools >= 1.0-4
Requires:	libxslt-progs >= 1.1.15
Requires:	openjade
Conflicts:	pkgconfig < 1:0.19
#BuildArch:	noarch (rejected by autoconf)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# architecture-independant pkgconfig dir
%define		_pkgconfigdir	%{_datadir}/pkgconfig

%description
gtk-doc is a tool for generating API reference documentation. It is
used for generating the documentation for GTK+, GLib and GNOME.

%description -l pl.UTF-8
gtk-doc jest narzędziem do generowania dokumentacji API. Jest używany
do generowania dokumentacji GLib, GTK+ i GNOME.

%package common
Summary:	Common directories for documetation generated using gtk-doc
Summary(pl.UTF-8):	Katalogi na dokumentację wygenerowaną za pomocą gtk-doc
Group:		Development

%description common
Common directories for API documentation for various packages,
generated using gtk-doc.

%description common -l pl.UTF-8
Katalogi na dokumentację API do różnych pakietów, wygenerowaną za
pomocą gtk-doc.

%package automake
Summary:	Automake macros for gtk-doc
Summary(pl.UTF-8):	Makra dla automake do gtk-doc
Group:		Development/Tools
Requires:	automake
Conflicts:	gtk-doc < 0:1.4-3

%description automake
Automake macros for gtk-doc.

%description automake -l pl.UTF-8
Makra dla automake do gtk-doc.

%prep
%setup -q
mv -f doc/README doc/README.docs

%build
%{__gnome_doc_common}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_gtkdocdir} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS TODO README doc/*
%attr(755,root,root) %{_bindir}/gtkdoc-*
%attr(755,root,root) %{_bindir}/gtkdocize
%{_datadir}/gtk-doc
%{_pkgconfigdir}/%{name}.pc
%{_datadir}/sgml/%{name}
%{_examplesdir}/%{name}-%{version}

%files common
%defattr(644,root,root,755)
%dir %{_docdir}/gtk-doc
%dir %{_gtkdocdir}

%files automake
%defattr(644,root,root,755)
%{_aclocaldir}/gtk-doc.m4
