%define 	modulename pam_sessionlog
Summary:	PAM module for session log
Summary(pl):	Modu³ PAM do logowania sesji
Name:		pam-%{modulename}
Version:	2001.12.10
Release:	1
License:	GPL
Group:		Base
Vendor:		Pawel Boguslawski <bogi@ibnet.pl>
Source0:	%{modulename}-%{version}.tar.gz
Patch1:		%{modulename}-char.patch
URL:		http://www.ibnet.pl/programy/english.html
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	%{modulename}
Obsoletes:	%{modulename}

%description
PAM module which login session to wmtp base.

%description -l pl
Modu³ PAM loguj±cy sesje do bazy wtmp

%prep
%setup -q -n %{modulename}-%{version}
patch -p2 < sessionlog-patch
%patch1 -p0 

%build
%{__cc} %{rpmcflags} -fPIC -c %{modulename}/%{modulename}.c
ld -shared -x -o %{modulename}.so %{modulename}.o -lpam

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/security

install %{modulename}.so $RPM_BUILD_ROOT/lib/security

gzip -9nf README INSTALL

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) /lib/security/%{modulename}.so
