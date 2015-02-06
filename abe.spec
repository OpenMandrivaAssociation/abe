%define	name	abe
%define	version	1.1
%define release	9
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
Patch1:		abe-1.1-drop-x-req.patch
License:	GPL
Group:		Games/Arcade
Summary:	%{Summary}
BuildRequires:	SDL-devel SDL_mixer-devel desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A scrolling, platform-jumping, key-collecting, ancient pyramid
exploring game, vaguely in the style of similar games for the
Commodore+4. The game is intended to show young people all the
cool games they missed.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
autoreconf -fi
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


%changelog
* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 1.1-8mdv2011.0
+ Revision: 635057
- add patch
- drop x req from configure
- rebuild
- tighten BR

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-7mdv2011.0
+ Revision: 609902
- rebuild

* Wed Jan 27 2010 Funda Wang <fwang@mandriva.org> 1.1-6mdv2010.1
+ Revision: 497301
- fix str fmt

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1.1-4mdv2009.0
+ Revision: 218439
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.1-4mdv2008.1
+ Revision: 135813
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Fri Dec 15 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.1-4mdv2007.0
+ Revision: 97207
- fix buildrequires
- add xdg menu to %%files
- add xdg menu (fixes #26326)
  cleanups
- Import abe

* Tue Jun 27 2006 Lenny Cartier <lenny@mandriva.com> 1.1-2mdv2007.0
- use mkrel

* Mon Mar 07 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.1-1mdk
- 1.1
- license changed to GPL
- drop P0 (fixed upstream)

* Fri Aug 27 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0-3mdk
- rebuild for new menu

* Sat Apr 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0-2mdk
- rebuild
- fix summary macro to avoid possible conflicts if we were to build debug package
- fix buildrequires (lib64..)
- don't bzip2 icons in src.rpm

