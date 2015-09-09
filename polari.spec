%define url_ver %(echo %{version}|cut -d. -f1,2)

%global __provides_exclude libpolari.*\\.so$
%global __requires_exclude libpolari.*\\.so$|libtelepathy-glib\\.so\\.0\\(.*
%define __noautoreqfiles gjs-console

Name:		polari
Version:	3.16.1
Release:	3
Summary:	Internet Relay Chat client for GNOME
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
URL:		https://wiki.gnome.org/Apps/Polari
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		polari-3.14.0-fix-typelibdir.patch
BuildRequires:	intltool
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 1.35.9
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.9.12
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	gsettings-desktop-schemas
BuildRequires:	desktop-file-utils
BuildRequires:	gjs
Requires:	gsettings-desktop-schemas
Requires:	telepathy-logger
Requires:	telepathy-mission-control
Requires:	telepathy-idle


%description
Polari is an Internet Relay Chat client for the GNOME desktop.

%prep
%setup -q
%apply_patches

%build
autoreconf -vfi
%configure
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING AUTHORS NEWS
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_libdir}/girepository-1.0/Polari-1.0.typelib
%{_datadir}/dbus-1/services/org.gnome.Polari.service
%{_datadir}/applications/org.gnome.Polari.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/%{name}/
%{_iconsdir}/*/*/*/*
%{_datadir}/appdata/org.gnome.Polari.appdata.xml
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Polari.service
%{_datadir}/telepathy/clients/Polari.client

