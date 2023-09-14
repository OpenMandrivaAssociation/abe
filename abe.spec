Name:		abe
Version:	1.1
Release:	10
URL:		https://abe.sourceforge.net/
Source0:	https://downloads.sourceforge.net/project/abe/abe/abe-%{version}/abe-%{version}.tar.gz
Source10:	https://sourceforge.net/p/abe/patches/_discuss/thread/6c34cb78/0840/attachment/abe.png
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		abe-1.1-fix-str-fmt.patch
Patch1:		abe-1.1-drop-x-req.patch
Patch2:		https://sourceforge.net/p/abe/patches/_discuss/thread/a82d8dea/e8f3/attachment/abe-1.1-doublefree.patch
Patch3:		https://sourceforge.net/p/abe/patches/_discuss/thread/9594a65a/05ce/attachment/abe-1.1-format.patch
Patch4:		https://sourceforge.net/p/abe/patches/3/attachment/abe-1.1-settings.patch
Patch5:		https://sourceforge.net/p/abe/patches/4/attachment/desktop-and-appdata.patch
Patch6:		https://sourceforge.net/p/abe/patches/5/attachment/install-gamedata.patch
License:	GPL
Group:		Games/Arcade
Summary:	Abe's Amazing Adventure - side-scrolling platform jumping game
BuildRequires:	pkgconfig(sdl) 
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	desktop-file-utils


%description
A scrolling, platform-jumping, key-collecting, ancient pyramid
exploring game, vaguely in the style of similar games for the
Commodore+4. The game is intended to show young people all the
cool games they missed.

%prep
%autosetup -p1
cp %{S:10} images/abe.png
autoreconf -fi
%configure2_5x	--bindir=%{_gamesbindir} \
		--with-data-dir=%{_gamesdatadir}/abe

%build
%make_build

%install
%make_install
#install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
#install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
#install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%files
%defattr(644,root,root,755)
%doc README
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%defattr(755,root,root,755)
%{_gamesbindir}/*
%{_datadir}/appdata/abe.appdata.xml
%{_datadir}/pixmaps/abe.png
