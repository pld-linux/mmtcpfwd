Summary:	Secure TCP/IP port forwarder		
Summary(pl):	Bezpieczny forwarder portow TCP/IP 
Name:		mmtcpfwd	
Version:	0.1.0
Release:	1
Epoch:          2
License:	GPL	
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	http://mmondor.rubiks.net/software/linux/%{name}-%{version}.tar.gz
Source1:	%{name}.init
Source2:	%{name}.conf
URL:		http://mmondor.rubiks.net/software.html	
Prereq:		rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Secure TCP/IP port forwarder, MASQ fake ident and FTP passive proxy
superserver intended for linux firewalls with anti-DoS features.

%description -l pl
Bezpieczny forwarder portow TCP/IP.

%prep
%setup  -q

%build
cd src
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_sysconfdir},/etc/rc.d/init.d}

install src/mmtcpfwd 	$RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE2}	$RPM_BUILD_ROOT%{_sysconfdir}/mmtcpfwd.conf
install %{SOURCE1}	$RPM_BUILD_ROOT/etc/rc.d/init.d/mmtcpfwd

gzip -9nf README*

%clean
rm -rf $RPM_BUILD_ROOT

%post
DESC="%{name} daemon"; %chkconfig_add

%preun
%chkconfig_del

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(750,root,root) %{_sbindir}/*
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mmtcpfwd.conf 
%attr(754,root,root) %{_sysconfdir}/rc.d/init.d/mmtcpfwd
