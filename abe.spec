%define	name	abe
%define	version	1.1
%define	release	%mkrel 6
%define	Summary	Abe's Amazing Adventure!!

Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://abe.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		abe-1.1-fix-str-fmt.patch
License:	GPL
Group:		Games/Arcade
Summary:	%{Summary}
BuildRequires:	SDL-devel SDL_mixer-devel X11-devel desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A scrolling, platform-jumping, key-collecting, ancient pyramid
exploring game, vaguely in the style of similar games for the
Commodore+4. The game is intended to show young people all the
cool games they missed.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x	--bindir=%{_gamesbindir} \
		--with-data-dir=%{_gamesdatadir}/abe
%make

%install
rm -rf %{buildroot}
%makeinstall_std
install -d %{buildroot}%{_gamesdatadir}/%{name}
cp -a {images,sounds,maps} %{buildroot}%{_gamesdatadir}/%{name}


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{Summary}
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README
%{_gamesdatadir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%defattr(755,root,root,755)
%{_gamesbindir}/*
