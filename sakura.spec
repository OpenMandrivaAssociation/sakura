Name: sakura
Summary: A lightweight terminal emulator with very few dependencies
Version: 2.4.2
Release: 2
License: GPLv2
Group: Terminals
Url: http://www.pleyades.net/david/sakura.php
Source0: http://launchpad.net/sakura/trunk/%{version}/+download/%{name}-%{version}.tar.bz2
Patch0:	sakura-2.4.2_desktop-icon.patch

BuildRequires: cmake >= 2.4.5
BuildRequires: libvte-devel >= 0.17.4

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
%apply_patches

%build
%cmake \
	-DLOCALE_INSTALL_DIR=%{_datadir}/locale \
	-DLIB_INSTALL_DIR=%{_libdir}

%make

%install
rm -rf %{buildroot}
cd build
%makeinstall_std
%find_lang %{name}

%files -f build/%{name}.lang
%doc INSTALL
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/man1/sakura.1*

