%define url_ver %(echo %{version}|cut -d. -f1,2)

%global __provides_exclude libpolari.*\\.so$
%global __requires_exclude libpolari.*\\.so$|libtelepathy-glib\\.so\\.0\\(.*

Name:		polari
Version:	3.16.1
Release:	1
Summary:	Internet Relay Chat client for GNOME
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
URL:		https://wiki.gnome.org/Apps/Polari
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		polari-3.14.0-fix-typelibdir.patch
BuildRequires:	intltool
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
%configure --disable-static
%make

%install
%makeinstall_std

find %{buildroot} -name '*.la' -delete

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


%changelog
* Wed Oct 15 2014 umeabot <umeabot> 3.14.1-2.mga5
+ Revision: 740177
- Second Mageia 5 Mass Rebuild

* Tue Oct 14 2014 ovitters <ovitters> 3.14.1-1.mga5
+ Revision: 738729
- new version 3.14.1

* Wed Sep 24 2014 wally <wally> 3.14.0-5.mga5
+ Revision: 724211
- update requires/provides excludes

* Tue Sep 23 2014 wally <wally> 3.14.0-4.mga5
+ Revision: 722582
- another rebuild with new g-ir-dep-tool

* Tue Sep 23 2014 wally <wally> 3.14.0-3.mga5
+ Revision: 722507
- rebuild with new g-ir-dep-tool

* Tue Sep 23 2014 wally <wally> 3.14.0-2.mga5
+ Revision: 722478
- add patch to move .typelib file to a better location

* Mon Sep 22 2014 ovitters <ovitters> 3.14.0-1.mga5
+ Revision: 719238
- new version 3.14.0

* Wed Sep 17 2014 ovitters <ovitters> 3.13.92-1.mga5
+ Revision: 692843
- new version 3.13.92

  + umeabot <umeabot>
    - Mageia 5 Mass Rebuild

  + tv <tv>
    - auto convert _exclude_files_from_autoreq

* Wed Aug 20 2014 ovitters <ovitters> 3.13.90-1.mga5
+ Revision: 665900
- new version 3.13.90
- dropped merged patch 2
- dropped merged patch 1

* Fri Aug 01 2014 ovitters <ovitters> 3.13.2-3.mga5
+ Revision: 658877
- add another patch for username tranparency

* Fri Aug 01 2014 ovitters <ovitters> 3.13.2-2.mga5
+ Revision: 658873
- add upstream patch to ensure text is visible

* Wed May 28 2014 ovitters <ovitters> 3.13.2-1.mga5
+ Revision: 627115
- new version 3.13.2

* Wed May 14 2014 ovitters <ovitters> 3.12.2-1.mga5
+ Revision: 622750
- new version 3.12.2

* Tue Apr 15 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 615215
- new version 3.12.1

* Tue Mar 25 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 608632
- new version 3.12.0

* Wed Feb 05 2014 ovitters <ovitters> 3.11.2-2.mga5
+ Revision: 583732
- fix requirement

* Wed Feb 05 2014 ovitters <ovitters> 3.11.2-1.mga5
+ Revision: 583719
- imported package polari

