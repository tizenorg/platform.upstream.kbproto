%bcond_with x

Name:           kbproto
Version:        1.0.6
Release:        1
License:        MIT
Summary:        X
Url:            http://www.x.org
Group:          Development/System
Source0:        %{name}-%{version}.tar.bz2
Source1001: 	kbproto.manifest

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros)

%if !%{with x}
ExclusiveArch:
%endif

%description
%{summary}.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure --disable-static \
             --libdir=%{_datadir} \
             --without-xmlto

make %{?_smp_mflags}

%install
%make_install

%remove_docs

%files
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/*.h
%{_datadir}/pkgconfig/*.pc
