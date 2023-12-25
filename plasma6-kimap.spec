%define major 6
%define libname %mklibname KF6IMAP
%define devname %mklibname KF6IMAP -d

Name: plasma6-kimap
Version:	24.01.85
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/kimap-%{version}.tar.xz
Summary: KDE library for accessing IMAP servers
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Test)
BuildRequires: sasl-devel
BuildRequires: boost-devel
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant
Requires: %{libname} = %{EVRD}

%description
KDE library for accessing IMAP servers.

%package -n %{libname}
Summary: KDE library for accessing IMAP servers
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for accessing IMAP servers.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1 -n kimap-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libkimap5

%files -f libkimap5.lang
%{_datadir}/qlogging-categories6/kimap.categories
%{_datadir}/qlogging-categories6/kimap.renamecategories

%files -n %{libname}
%{_libdir}/*.so*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/cmake/*
# kimaptest is built only as a static lib
%{_libdir}/*.a
