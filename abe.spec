%define	name	abe
%define	version	1.1
%define	release	%mkrel 4
%define	Summary	Abe's Amazing Adventure!!

Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://abe.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
License:	GPL
Group:		Games/Arcade
Summary:	%{Summary}
BuildRequires:	SDL-devel SDL_mixer-devel X11-devel desktop-file-utils

%description
A scrolling, platform-jumping, key-collecting, ancient pyramid
exploring game, vaguely in the style of similar games for the
Commodore+4. The game is intended to show young people all the
cool games they missed.

%prep
%setup -q

%build
%configure2_5x	--bindir=%{_gamesbindir} \
		--with-data-dir=%{_gamesdatadir}/abe
%make

%install
rm -rf %{buildroot}
%makeinstall_std
install -d %{buildroot}%{_gamesdatadir}/%{name}
cp -a {images,sounds,maps} %{buildroot}%{_gamesdatadir}/%{name}

install -d %{buildroot}%{_menudir}
cat <<EOF > %{buildroot}%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{name}" \
		icon=%{name}.png \
		needs="x11" \
		section="More Applications/Games/Arcade" \
		title="%{Summary}" \
		longtitle="%{Summary}" \
		xdg="true"
EOF

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
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README
%{_gamesdatadir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_menudir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%defattr(755,root,root,755)
%{_gamesbindir}/*


