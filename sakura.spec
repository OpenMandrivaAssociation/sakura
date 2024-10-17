Name: sakura
Summary: A lightweight terminal emulator with very few dependencies
Version: 3.0.4
Release: 2
License: GPLv2
Group: Terminals
Url: https://www.pleyades.net/david/sakura.php
Source0: http://launchpad.net/sakura/trunk/%{version}/+download/%{name}-%{version}.tar.bz2
BuildRequires: cmake
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(vte-2.90)

%description
sakura is a terminal emulator based on GTK and VTE. It's a terminal emulator
with few dependencies, so you don't need a full GNOME desktop installed to have
a decent terminal emulator. Current terminal emulators based on VTE are
gnome-terminal, XFCE Terminal, TermIt and a small sample program included in
the vte sources. The differences between sakura and the last one are that it
uses a notebook to provide several terminals in one window and adds a
contextual menu with some basic options. No more no less. 

%prep
%setup -q
%autopatch -p1

%build
%cmake \
	-DLOCALE_INSTALL_DIR=%{_datadir}/locale \
	-DLIB_INSTALL_DIR=%{_libdir}

%make

%install
%makeinstall_std -C build
%find_lang %{name}

%files -f %{name}.lang
%doc INSTALL
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/man1/sakura.1*



%changelog
* Sun May 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.0.4-1
+ Revision: 798596
- BR: gtk+3-devel
- version update 3.0.4

* Tue Feb 14 2012 Matthew Dawkins <mattydaw@mandriva.org> 2.4.2-2
+ Revision: 773907
- added patch to fix desktop icon
- cleaned up spec

* Wed Oct 26 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.4.2-1
+ Revision: 707367
- new version 2.4.2

* Thu Aug 26 2010 Shlomi Fish <shlomif@mandriva.org> 2.3.8-1mdv2011.0
+ Revision: 573365
- import sakura

