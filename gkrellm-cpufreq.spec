Summary:	CPU Frequency plugin for Gkrellm 2.0
Name:		gkrellm-cpufreq
Version:	0.5.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://iacs.epfl.ch/~winkelma/gkrellm2-cpufreq/gkrellm2-cpufreq-%{version}.tar.gz
# Source0-md5:	9e77035a79ea6c8d1fd9f85645a37bb3
URL:		http://iacs.epfl.ch/~winkelma/gkrellm2-cpufreq/
BuildRequires:	gkrellm-devel >= 2.0
Requires:	gkrellm >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A plugin for displaying and manipulating CPU frequency.

%prep
%setup -q -n gkrellm2-cpufreq-%{version}

%build
%{__make} FLAGS="%{rpmcflags} -fPIC `pkg-config gtk+-2.0 --cflags`"

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
