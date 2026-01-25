%global debug_package %{nil}
%global __os_install_post %{nil}

%if "%{_target_cpu}" == "x86_64"
%global goarch amd64
%endif
%if "%{_target_cpu}" == "aarch64"
%global goarch arm64
%endif

Name:           frp
Version:        %{_version}
Release:        %{_release}
Summary:        A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet.
License:        Apache-2.0
URL:            https://github.com/fatedier/frp
Source0:        https://github.com/fatedier/frp/releases/download/v%{version}/frp_%{version}_linux_%{goarch}.tar.gz
Source1:        frpc@.service
Source2:        frps@.service

BuildRequires:  systemd-rpm-macros

%description
frp is a fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet.

%package -n frpc
Summary:        Client for frp
Requires:       systemd

%description -n frpc
Client for frp (Fast Reverse Proxy).

%package -n frps
Summary:        Server for frp
Requires:       systemd

%description -n frps
Server for frp (Fast Reverse Proxy).

%prep
%setup -q -n frp_%{version}_linux_%{goarch}

%build
# Binaries are already compiled in the release tarball

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_sysconfdir}/frpc
install -d -m 755 %{buildroot}%{_sysconfdir}/frps
install -d -m 755 %{buildroot}%{_unitdir}

install -m 755 frpc %{buildroot}%{_bindir}/frpc
install -m 755 frps %{buildroot}%{_bindir}/frps

install -m 644 frpc.toml %{buildroot}%{_sysconfdir}/frpc/frpc.toml
install -m 644 frps.toml %{buildroot}%{_sysconfdir}/frps/frps.toml

# Install systemd service templates
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/frpc@.service
install -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/frps@.service

%files -n frpc
%license LICENSE
%{_bindir}/frpc
%dir %{_sysconfdir}/frpc
%config(noreplace) %{_sysconfdir}/frpc/frpc.toml
%{_unitdir}/frpc@.service

%files -n frps
%license LICENSE
%{_bindir}/frps
%dir %{_sysconfdir}/frps
%config(noreplace) %{_sysconfdir}/frps/frps.toml
%{_unitdir}/frps@.service

%changelog
* %{date} awfufu <me@awfufu.com> - %{version}-%{release}
- Automated build
