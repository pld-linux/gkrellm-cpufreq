Summary:	CPU Frequency plugin for Gkrellm 2.x
Summary(pl.UTF-8):	Wtyczka częstotliwości CPU dla Gkrellma 2.x
Name:		gkrellm-cpufreq
Version:	0.6.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://iacs.epfl.ch/~winkelma/gkrellm2-cpufreq/gkrellm2-cpufreq-%{version}.tar.gz
# Source0-md5:	ddbe4e9574ae818697271c39191f737d
URL:		http://iacs.epfl.ch/~winkelma/gkrellm2-cpufreq/
BuildRequires:	gkrellm-devel >= 2.0
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	cpufrequtils-devel
BuildRequires:	pkgconfig
Requires:	gkrellm >= 2.0
Requires:	cpufrequtils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A plugin for displaying and manipulating CPU frequency.

You might want to add the following to /etc/sudoers:

<user> ALL = (root) NOPASSWD: /usr/sbin/cpufreq-set [0-9]*
<user> ALL = (root) NOPASSWD: /usr/sbin/cpufreqnextgovernor

%description -l pl.UTF-8
Wtyczka do wyświetlania i manipulowania częstotliwością CPU.

Aby zezwolić użytkownikowi <user> na zmianę częstotliwości CPU,
należy dodać poniższe linie do pliku /etc/sudoers:

<user> ALL = (root) NOPASSWD: /usr/sbin/cpufreq-set [0-9]*
<user> ALL = (root) NOPASSWD: /usr/sbin/cpufreqnextgovernor

%prep
%setup -q -n gkrellm2-cpufreq-%{version}

%build
%{__make} \
	FLAGS="%{rpmcflags} -fPIC `pkg-config gtk+-2.0 --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins
install -d $RPM_BUILD_ROOT%{_sbindir}

install cpufreq.so $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins
install cpufreqnextgovernor $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/cpufreq.so
%attr(755,root,root) %{_sbindir}/*
