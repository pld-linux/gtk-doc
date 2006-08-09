#
%include	/usr/lib/rpm/macros.perl
#
Summary:	API documentation generation tool for GTK+ and GNOME
Summary(es):	El generador de documentación del GTK
Summary(pl):	Narzêdzie do generowania dokumentacji API do GTK+ i GNOME
Summary(pt_BR):	O gerador de documentação do GTK
Name:		gtk-doc
Version:	1.7
Release:	2
License:	GPL v2+
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/gnome/sources/gtk-doc/1.7/%{name}-%{version}.tar.bz2
# Source0-md5:	2543a3f5a7b5347fb135855ca55adea1
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
BuildRequires:	scrollkeeper
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
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# architecture-independant pkgconfig dir
%define		_pkgconfigdir	%{_datadir}/pkgconfig

%description
gtk-doc is a tool for generating API reference documentation. It is
used for generating the documentation for GTK+, GLib and GNOME.

%description -l pl
gtk-doc jest narzêdziem do generowania dokumentacji API. Jest u¿ywany
do generowania dokumentacji GLib, GTK+ i GNOME.

%package common
Summary:	Common directories for documetation generated using gtk-doc
Summary(pl):	Katalogi na dokumentacjê wygenerowan± za pomoc± gtk-doc
Group:		Development

%description common
Common directories for API documentation for various packages,
generated using gtk-doc.

%description common -l pl
Katalogi na dokumentacjê API do ró¿nych pakietów, wygenerowan± za
pomoc± gtk-doc.

%package automake
Summary:	Automake macros for gtk-doc
Summary(pl):	Makra dla automake do gtk-doc
Group:		Development/Tools
Requires:	automake
Conflicts:	gtk-doc < 0:1.4-3

%description automake
Automake macros for gtk-doc.

%description automake -l pl
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
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/gtk-doc/html \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS TODO README doc/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gtk-doc
%{_pkgconfigdir}/%{name}.pc
%{_datadir}/sgml/%{name}
%{_examplesdir}/%{name}-%{version}
%{_omf_dest_dir}/%{name}

%files common
%defattr(644,root,root,755)
%dir %{_defaultdocdir}/gtk-doc
%dir %{_defaultdocdir}/gtk-doc/html

%files automake
%defattr(644,root,root,755)
%{_aclocaldir}/*
