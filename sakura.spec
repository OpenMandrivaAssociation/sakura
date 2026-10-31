Name:		sakura
Summary:	Lightweight terminal emulator with very few dependencies
Version:	3.8.9
Release:	1
License:	GPL-2.0-only
Group:		Terminals
Url:		https://launchpad.net/sakura
Source0:	https://launchpad.net/sakura/trunk/%{version}/+download/%{name}-%{version}.tar.bz2

BuildRequires:	cmake
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(vte-2.91)
BuildRequires:	pkgconfig(x11)

BuildSystem:	cmake

%description
Sakura is a terminal emulator and it's only dependencies are GTK and VTE.
It uses a notebook to provide several terminals in one window and allows
to change configuration options via a contextual menu. No more no less.

%files -f %{name}.lang
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/terminal-tango.svg
%{_mandir}/man1/%{name}.1.zst
