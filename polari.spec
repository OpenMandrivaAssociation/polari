%define url_ver %(echo %{version}|cut -d. -f1,2)

%global __provides_exclude libpolari.*\\.so$
%global __requires_exclude libpolari.*\\.so$|libtelepathy-glib\\.so\\.0\\(.*
%define __noautoreqfiles org.gnome.Polari$

Name:		polari
Version:	3.30.1
Release:	1
Summary:	Internet Relay Chat client for GNOME
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
URL:		https://wiki.gnome.org/Apps/Polari
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
#Patch0:		polari-3.14.0-fix-typelibdir.patch
BuildRequires:	intltool
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 1.35.9
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.9.12
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	gsettings-desktop-schemas
BuildRequires:	desktop-file-utils
BuildRequires:	gjs
BuildRequires:	appstream-util
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(telepathy-logger-0.2)
BuildRequires:	gnome-common
BuildRequires:	yelp-devel
BuildRequires:	itstool
BuildRequires:	meson

Requires:	gsettings-desktop-schemas
Requires:	telepathy-logger
Requires:	telepathy-mission-control
Requires:	telepathy-idle


%description
Polari is an Internet Relay Chat client for the GNOME desktop.

%prep
%setup -q
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -delete

%find_lang %{name} --with-gnome --all-name


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
%{_datadir}/metainfo/org.gnome.Polari.appdata.xml
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Polari.service
%{_datadir}/telepathy/clients/Polari.client

