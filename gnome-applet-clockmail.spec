%define		_realname	clockmail-applet
Summary:	GNOME panel applet, it can display the time, date, mail status, and the message count
Summary(pl.UTF-8):	Aplet panelu GNOME do wyświetlania czasu, daty, stanu poczty i liczby wiadomości
Name:		gnome-applet-clockmail
Version:	1.9.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gqapplets/%{_realname}-%{version}.tar.gz
# Source0-md5:	8ee00d77149e38842ed66e6cfdd69e47
URL:		http://gqapplets.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gnome-panel-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/gconf

%description
Clockmail is a GNOME panel applet, it can display the time, date, mail
status, and the message count. Many themes are included.

%description -l pl.UTF-8
Clockmail jest apletem panelu GNOME, służącym do wyświetlania czasu,
daty, stanu poczty i liczby wiadomości. Dołączono wiele motywów.

%prep
%setup -q -n %{_realname}-%{version}

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-gconf-schema-file-dir=%{_sysconfdir}/schemas
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog
%attr(755,root,root) %{_libdir}/clockmail_applet2
%{_libdir}/bonobo/servers/*
%{_datadir}/gnome-2.0/ui/GNOME_ClockmailApplet.xml
%{_datadir}/clockmail-applet2
%{_sysconfdir}/schemas/clockmail-applet.schemas
%{_pixmapsdir}/*.png
