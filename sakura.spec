Name: sakura
Summary: A lightweight terminal emulator with very few dependencies
Version: 2.3.8
Release: %mkrel 1
License: GPL
Url: http://www.pleyades.net/david/sakura.php
Group: Terminals
Source: %{name}-%{version}.tar.bz2

# patches in the form amarok-version-r<relnum> are referent to the KDE
# commit numbered as <relnum>
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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

%files -f build/%{name}.lang
%defattr(-,root,root) 
%doc INSTALL
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/man1/sakura.1.lzma

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake -DLOCALE_INSTALL_DIR=%{_datadir}/locale -DLIB_INSTALL_DIR=%{_libdir}

%make

%install
rm -rf %buildroot
cd build
%{makeinstall_std}
%find_lang %{name}

%clean
rm -rf %buildroot

