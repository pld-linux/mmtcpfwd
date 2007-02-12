Summary:	Secure TCP/IP port forwarder
Summary(pl.UTF-8):   Bezpieczny forwarder portów TCP/IP
Name:		mmtcpfwd
Version:	0.1.0
Release:	4
Epoch:		2
License:	GPL
Group:		Networking/Daemons
Source0:	http://gobot.accela.net/software/stable/%{name}-%{version}.tar.gz
# Source0-md5:	b1d9ff2aa0059a4df9d4e54ed675be68
Source1:	%{name}.init
Source2:	%{name}.conf
URL:		http://gobot.accela.net/software.html
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Secure TCP/IP port forwarder, MASQ fake ident and FTP passive proxy
superserver intended for Linux firewalls with anti-DoS features.

%description -l pl.UTF-8
Bezpieczny forwarder portow TCP/IP, fałszywy serwer ident dla
maskarady oraz proxy dla pasywnego FTP - przeznaczony dla linuksowych
firewalli z możliwościami zapobiegania DoS.

%prep
%setup -q

%build
%{__make} -C src \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_sysconfdir},/etc/rc.d/init.d}

install src/mmtcpfwd 	$RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE2}	$RPM_BUILD_ROOT%{_sysconfdir}/mmtcpfwd.conf
install %{SOURCE1}	$RPM_BUILD_ROOT/etc/rc.d/init.d/mmtcpfwd

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add mmtcpfwd
%service mmtcpfwd restart "mmtcpfwd daemon"

%preun
if [ "$1" = "0" ]; then
	%service mmtcpfwd stop
	/sbin/chkconfig --del mmtcpfwd
fi

%files
%defattr(644,root,root,755)
%doc README*
%attr(750,root,root) %{_sbindir}/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mmtcpfwd.conf
%attr(754,root,root) /etc/rc.d/init.d/mmtcpfwd
