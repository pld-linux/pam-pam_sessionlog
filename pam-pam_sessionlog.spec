%define 	modulename pam_sessionlog
Summary:	PAM module for session log
Summary(pl.UTF-8):	Moduł PAM do logowania sesji
Name:		pam-%{modulename}
Version:	2001.12.10
Release:	4
Epoch:		1
License:	GPL
Group:		Base
Vendor:		Pawel Boguslawski <bogi@ibnet.pl>
# http://bogi.ibnet.pl/cgi/download?object=pam_sessionlog
Source0:	%{modulename}-%{version}.tar.gz
# Source0-md5:	0a36d2a5c4e37eb29c0a7996c57c7efe
Patch1:		%{name}-char.patch
URL:		http://www.ibnet.pl/programy/english.html
BuildRequires:	pam-devel
Obsoletes:	pam_sessionlog
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PAM module which logs session to wmtp base.

%description -l pl.UTF-8
Moduł PAM logujący sesje do bazy wtmp.

%prep
%setup -q -n %{modulename}-%{version}
patch -p2 < sessionlog-patch
%patch1 -p0

%build
%{__cc} %{rpmcflags} -fPIC -c %{modulename}/%{modulename}.c
ld -shared -x -o %{modulename}.so %{modulename}.o -lpam

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_lib}/security

install %{modulename}.so $RPM_BUILD_ROOT/%{_lib}/security

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README INSTALL
%attr(755,root,root) /%{_lib}/security/%{modulename}.so
