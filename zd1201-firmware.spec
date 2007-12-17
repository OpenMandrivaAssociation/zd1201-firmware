%define module zd1201
%define name %{module}-firmware
%define version 0.14
%define distname %{module}-%{version}-fw
%define release %mkrel 1

Summary: Firmware files for the ZD1201 chip
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/linux-lc100020/%{distname}.tar.bz2
License: As-Is
Group: System/Kernel and hardware
Url: http://linux-lc100020.sourceforge.net/
BuildArch: noarch

%description
This package contains the firmware needed for the zd1201 devices to work.

This package contains two files, zd1201.fw is the firmware file for
using the device as a normal 802.11b client. The file zd1201-ap.fw is
used to put the device in access point mode.

%prep
%setup -q -n %{distname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware
install -m644 %{module}*.fw $RPM_BUILD_ROOT/lib/firmware/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/lib/firmware/%{module}*.fw
