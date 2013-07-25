%define __noautoreq '.*/bin/awk|.*/bin/gawk'
%define	pkgname oct2mat
%define name	octave-%{pkgname}
%define version 1.0.7

Summary:	Convert Octave scripts into MATLAB-compatible style
Name:		%{name}
Version:	%{version}
Release:        3
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/oct2mat/
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 2.9.7
BuildRequires:  octave-devel >= 2.9.9
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildArch:	noarch

%description
Convert Octave scripts into a MATLAB-compatible coding style.

%prep
%setup -q -c %{pkgname}-%{version}
cp %SOURCE0 .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %SOURCE0 
mv %{pkgname}-%{version}/COPYING .
mv %{pkgname}-%{version}/DESCRIPTION .

%clean

%post
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%postun
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%files
%defattr(-,root,root)
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}



%changelog
* Thu Aug 18 2011 Lev Givon <lev@mandriva.org> 1.0.7-1mdv2012.0
+ Revision: 695103
- import octave-oct2mat


