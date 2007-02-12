%define		_name justgreen
Summary:	X11 cursor theme - justgreen
Summary(pl.UTF-8):	Notyw kursorów dla X11 - justgreen
Name:		XcursorTheme-%{_name}
Version:	0.1a
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/content/files/10500-%{_name}-%{version}.tar.bz2
# Source0-md5:	5baec2e85980a292310a045e3ef597f1
URL:		http://www.kde-look.org/content/show.php?content=10500
BuildRequires:	XFree86 >= 4.3
BuildArch:	noarch
Requires:	XFree86 >= 4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A gradiented, green/gray cursor theme.

%description -l pl.UTF-8
Zielono-szary motyw kursorów z gradientem.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}
%{__tar} xfj %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}/
mv -f  $RPM_BUILD_ROOT%{_iconsdir}/%{_name}{-%{version},}
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/%{_name}/{*.sh,sshot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/%{_name}
