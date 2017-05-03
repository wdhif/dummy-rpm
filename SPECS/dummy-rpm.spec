%global project_version 0.0.24

Name:       dummy
Version:    0.0.1
Release:    noop
Summary:    A fake RPM
License:    AGPLv3+
Source0:    dummy.tar.bz2
BuildArch:  noarch

%description
A fake RPM

%prep
%setup -c -q -T -D -a 0

%build

%install
rm -rf %{buildroot}
# _datadir is typically /usr/share/
install -d -m 0755 %{buildroot}/%{_datadir}/dummy/
echo "This is a dummy RPM." > %{buildroot}/%{_datadir}/dummy/README

%files
%{_datadir}/dummy/README

%changelog
