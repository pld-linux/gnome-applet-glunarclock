Summary:	Displays the current phase of the Moon
Summary(pl):	Wy�wietla bie��c� faz� Ksi�yca
Name:		gnome-applet-glunarclock
Version:	0.32.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/sourceforge/glunarclock/glunarclock-%{version}.tar.gz
# Source0-md5:	63e1d989581e6bf95cec82ff1bbc56ef
Patch0:		%{name}-i18n.patch
URL:		http://glunarclock.sourceforge.net/
BuildRequires:	gnome-panel-devel >= 2.0
BuildRequires:	libxklavier-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Lunar Clock Applet displays the current phase of the Moon as an
applet for the gnome panel.

%description -l pl
Applet Zegara Ksi�ycowego GNOME wy�wietla bie��c� faz� Ksi�yca jako
aplet na panelu GNOME.


%define         _gnomehelpdir   %{_datadir}/gnome/help


%prep
%setup -q -n glunarclock-%{version}
%patch0 -p1

%build
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang glunarclock --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%gconf_schema_install glunarclock.schemas


%preun
%gconf_schema_uninstall glunarclock.schemas


%postun
%scrollkeeper_update_postun


%files -f glunarclock.lang
%defattr(644,root,root,755)
# COPYING contains only note about images
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/glunarclock-applet-2
%{_libdir}/bonobo/servers/*.server
%{_sysconfdir}/gconf/schemas/glunarclock.schemas
%{_datadir}/glunarclock
%{_datadir}/gnome-2.0/ui/*.xml
%{_omf_dest_dir}/glunarclock
%{_pixmapsdir}/glunarclock*