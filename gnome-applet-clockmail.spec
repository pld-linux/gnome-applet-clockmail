v# $Revision: 1.2 $, $Date: 2003-08-31 21:36:32 $
%define		_realname	clockmail-applet
Summary:	GNOME panel applet, it can display the time, date, mail status, and the message count
Summary(pl):	Aplet panelu GNOME do wyświetlania czasu, daty, stanu poczty i liczby wiadomości
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

%description -l pl
Clockmail jest apletem panelu GNOME, służącym do wyświetlania czasu,
daty, stanu poczty i liczby wiadomości. Dołączono wiele motywów.

%prep
%setup -q -n %{_realname}-%{version}

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure --with-gconf-schema-file-dir=%{_sysconfdir}/schemas
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
%{_sysconfdir}/schemas/clockmail-applet.schemas
%{_libdir}/bonobo/servers/*
%attr(755,root,root) %{_libdir}/clockmail_applet2
%{_datadir}/gnome-2.0/ui/GNOME_ClockmailApplet.xml
%{_pixmapsdir}/*.png
%{_datadir}/clockmail-applet2/*
