Summary:	API documentation generation tool for GTK+ and GNOME
Summary(es):	El generador de documentación del GTK
Summary(pl):	Narzêdzie do generowania dokumentacji API do GTK+ i GNOME
Summary(pt_BR):	O gerador de documentação do GTK
Name:		gtk-doc
Version:	1.3
Release:	2
License:	LGPL
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/gnome/sources/gtk-doc/1.3/%{name}-%{version}.tar.bz2
# Source0-md5:	d105d5b28e7e023ab1b7e85fb65e45c3
Patch0:		%{name}-colon.patch
URL:		http://www.gtk.org/rdp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-utils
BuildRequires:	openjade
BuildRequires:	libxslt-progs
BuildRequires:	docbook-dtd412-xml >= 1.0-10
BuildRequires:	docbook-style-xsl
BuildRequires:	perl-base >= 5.6.0
Requires:	docbook-dtd412-xml >= 1.0-10
Requires:	docbook-style-dsssl >= 1.77
Requires:	docbook-style-xsl >= 1.55.0-3
Requires:	docbook-utils >= 0.6.10
Requires:	gnome-doc-tools >= 1.0-4
Requires:	libxslt-progs
Requires:	openjade
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtk-doc is a tool for generating API reference documentation. It is
used for generating the documentation for GTK+, GLib and GNOME.

%description -l pl
gtk-doc jest narzêdziem do generowania dokumentacji API. Jest u¿ywany
do generowania dokumentacji GLib, GTK+ i GNOME.

%package common
Summary:	Common directories for documetation generated using gtk-doc
Summary(pl):	Katalogi na dokumentacjê wygenerowan± za pomoc± gtk-doc
# ???
Group:		Documentation

%description common
Common directories for API documentation for various packages,
generated using gtk-doc.

%description common -l pl
Katalogi na dokumentacjê API do ró¿nych pakietów, wygenerowan± za
pomoc± gtk-doc.

%prep
%setup -q
%patch0 -p1
mv -f doc/README doc/README.docs

%build
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS TODO README doc/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gtk-doc
%{_pkgconfigdir}/%{name}.pc
%{_aclocaldir}/*
%{_datadir}/sgml/%{name}
%{_examplesdir}/%{name}-%{version}

%files common
%defattr(644,root,root,755)
%dir %{_defaultdocdir}/gtk-doc
%dir %{_defaultdocdir}/gtk-doc/html
