Summary:	API documentation generation tool for GTK+ and GNOME
Summary(es):	El generador de documentación del GTK
Summary(pl):	Narzêdzie do generowania dokumentacji API do GTK+ i GNOME
Summary(pt_BR):	O gerador de documentação do GTK
Name:		gtk-doc
Version:	0.9
Release:	5
License:	LGPL
Group:		Development/Tools
Source0:	ftp://ftp.gtk.org/pub/gtk/v1.1/docs/rdp/%{name}-%{version}.tar.bz2
Patch0:		%{name}-xml.patch
URL:		http://www.gtk.org/rdp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-utils
BuildRequires:	openjade
BuildRequires:	libxslt-progs
Requires:	docbook-utils >= 0.6.10
Requires:	openjade
BuildArch:	noarch
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
Katalogi na dokumetacjê API do ró¿nych pakietów, wygenerowan± za
pomoc± gtk-doc.

%prep
%setup -q
%patch0 -p1
mv -f doc/README doc/README.docs

%build
rm -f missing
aclocal
%{__autoconf}
%{__automake}
%configure \
	--enable-public-id
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/gtk-doc/html

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README doc/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gtk-doc

%files common
%defattr(644,root,root,755)
%dir %{_defaultdocdir}/gtk-doc
%dir %{_defaultdocdir}/gtk-doc/html
