%define pkgname 	FiraCode

%define fontname 	fira-code
%define fontdir		%{_datadir}/fonts/TTF/%{fontname}
%define fontconfdir	%{_sysconfdir}/X11/fontpath.d

Summary:	Monospaced font with programming ligatures
Name:		fonts-ttf-fira-code
Version:	2
Release:	1
License:	OFL
Group:		System/Fonts/True type
URL:		https://github.com/tonsky/FiraCode
Source0:	https://github.com/tonsky/FiraCode/archive/%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	mkfontscale
BuildRequires:	mkfontdir

%description
Monospaced font with programming ligatures

%prep
%setup -qn %{pkgname}-%{version}

%build


%install
install -dm 0755 %{buildroot}/%{fontdir}/
install -m 644 distr/ttf/*.ttf %{buildroot}%{_xfontdir}/TTF/fira-code
mkfontscale %{buildroot}%{fontdir}/
mkfontdir %{buildroot}%{fontdir}/
mkdir -p %{buildroot}%{fontconfdir}/
ln -s ../../..%{buildroot}%{fontdir} %{buildroot}%{fontconfdir}/ttf-%{fontname}:pri=50


%files
%dir %{fontdir}
%{fontconfdir}/ttf-%{fontname}:pri=50
%{fontdir}/*.ttf
%verify(not mtime)%{fontdir}/fonts.dir
%{fontdir}/fonts.scale
%doc LICENSE
