Summary:	Secure TCP/IP port forwarder		
Summary(pl):	Bezpieczny forwarder portow TCP/IP 
Name:		mmtcpfwd	
Version:	0.7
Release:	1
Group:		Networking/Daemons
Group(pl):	-
License:	GPL	
Source0:	http://mmondor.rubiks.net/software/linux/mmtcpfwd-0.7.tar.gz
URL:		http://mmondor.rubiks.net/software.html	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Secure TCP/IP port forwarder, MASQ fake ident and FTP passive proxy superserver intended for linux firewalls with anti-DoS features
      
%description -l pl
Bezpieczny forwarder portow TCP/IP

%prep
%setup  -q

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sbindir}  $RPM_BUILD_ROOT%{_sysconfdir}

install mmtcpfwd $RPM_BUILD_ROOT%{_sbindir}
install mmtcpfwd.conf $RPM_BUILD_ROOT%{_sysconfdir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(4750,root,icmp) %{_sbindir}/*
%doc README*

%changelog
* %{date} PLD Team <pld-list@pld.org.pl>
All persons listed below can be reached at <cvs_login>@pld.org.pl

$Log: mmtcpfwd.spec,v $
Revision 1.1  2001-02-08 17:04:31  areq
- initial release NFY
