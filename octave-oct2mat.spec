%define octpkg oct2mat

Summary:	Convert Octave scripts into MATLAB-compatible style
Name:		octave-%{octpkg}
Version:	1.0.7
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 2.9.7

Requires:	octave(api) = %{octave_api}
Requires:	octave-io >= 1.0.0

Requires(post): octave
Requires(postun): octave

%description
ConConvert Octave scripts into a MATLAB-compatible coding style.

This package is part of unmantained Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkgdir}
%{octpkgdir}/*
#%doc %{octpkg}-%{version}/NEWS
%doc %{octpkg}-%{version}/COPYING

