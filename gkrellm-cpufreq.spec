Summary:	CPU Frequency plugin for Gkrellm 2.x
Summary(pl):	Wtyczka częstotliwości CPU dla Gkrellma 2.x
Name:		gkrellm-cpufreq
Version:	0.5.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://iacs.epfl.ch/~winkelma/gkrellm2-cpufreq/gkrellm2-cpufreq-%{version}.tar.gz
# Source0-md5:	9be9b733b19790cab2fd155b54f686ef
URL:		http://iacs.epfl.ch/~winkelma/gkrellm2-cpufreq/
BuildRequires:	gkrellm-devel >= 2.0
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	pkgconfig
Requires:	gkrellm >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A plugin for displaying and manipulating CPU frequency.

%description -l pl
Wtyczka do wyświetlania i manipulowania częstotliwością CPU.

%prep
%setup -q -n gkrellm2-cpufreq-%{version}

%build
%{__make} \
	FLAGS="%{rpmcflags} -fPIC `pkg-config gtk+-2.0 --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins

install cpufreq.so $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/cpufreq.so
