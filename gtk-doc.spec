Summary:	API documentation generation tool for GTK+ and GNOME
Name:		gtk-doc
Version:	0.4b1
Release:	1
License:	LGPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-pubid.patch
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
URL:		http://www.gtk.org/rdp
BuildPrereq:	docbook-utils
BuildPrereq:	openjade
Requires:	docbook-utils
Requires:	openjade

%description
gtk-doc is a tool for generating API reference documentation. It is
used for generating the documentation for GTK+, GLib and GNOME.

%prep

%setup -q
%patch -p1 -b .pubid
# Move this doc file to avoid name collisions
mv doc/README doc/README.docs

%build
%configure --enable-public-id
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%doc AUTHORS README doc/* examples

%attr(755,root,root) %{_bindir}/*
%{_datadir}/gtk-doc/
