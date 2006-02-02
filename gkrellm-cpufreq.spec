Summary:	CPU Frequency plugin for Gkrellm 2.x
Summary(pl):	Wtyczka czêstotliwo¶ci CPU dla Gkrellma 2.x
Name:		gkrellm-cpufreq
Version:	0.5.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://iacs.epfl.ch/~winkelma/gkrellm2-cpufreq/gkrellm2-cpufreq-%{version}.tar.gz
# Source0-md5:	c7fd073c1fd4d32cb76ab131cf29e1fe
URL:		http://iacs.epfl.ch/~winkelma/gkrellm2-cpufreq/
BuildRequires:	gkrellm-devel >= 2.0
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	pkgconfig
Requires:	gkrellm >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A plugin for displaying and manipulating CPU frequency.

You might want to add the following to /etc/sudoers:
<user> ALL = (root) NOPASSWD: /usr/sbin/cpufreqset [0-9]*
<user> ALL = (root) NOPASSWD: /usr/sbin/cpufreqsetgovernor [a-z]
<user> ALL = (root) NOPASSWD: /usr/sbin/cpufreqnextgovernor

%description -l pl
Wtyczka do wy¶wietlania i manipulowania czêstotliwo¶ci± CPU.

Aby zezwoliæ u¿ytkownikowi <user> na zmianê czêstotliwo¶ci CPU,
nale¿y dodaæ poni¿sze linie do pliku /etc/sudoers:

<user> ALL = (root) NOPASSWD: /usr/sbin/cpufreqset [0-9]*
<user> ALL = (root) NOPASSWD: /usr/sbin/cpufreqsetgovernor [a-z]
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
install cpufreqset $RPM_BUILD_ROOT%{_sbindir}
install cpufreqnextgovernor $RPM_BUILD_ROOT%{_sbindir}
install cpufreqsetgovernor $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/cpufreq.so
%attr(755,root,root) %{_sbindir}/*
