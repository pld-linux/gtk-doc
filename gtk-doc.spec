Summary:	API documentation generation tool for GTK+ and GNOME
Summary(pl):	Narzêdzie do generowania dokumentacji API do GTK+ i GNOME
Name:		gtk-doc
Version:	0.4b1
Release:	3
License:	LGPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	ftp://ftp.gtk.org/pub/gtk/v1.1/docs/rdp/%{name}-%{version}.tar.gz
Patch0:		%{name}-pubid.patch
URL:		http://www.gtk.org/rdp/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	docbook-utils
BuildRequires:	openjade
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	docbook-utils
Requires:	openjade

%description
gtk-doc is a tool for generating API reference documentation. It is
used for generating the documentation for GTK+, GLib and GNOME.

%description -l pl
gtk-doc jest narzêdziem do generowania dokumentacji API. Jest u¿ywany
do generowania dokumentacji GLib, GTK+ i GNOME.

%prep
%setup -q
%patch -p1 -b .pubid
# Move this doc file to avoid name collisions
mv -f doc/README doc/README.docs

%build
aclocal
autoconf
%configure \
	--enable-public-id
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS README doc/* examples/gnome*/* examples/[MRc]*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.gz README.gz doc/* examples
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gtk-doc
