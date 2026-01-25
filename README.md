# FRP RPM Packages for Fedora

Auto RPM build for [fatedier/frp](https://github.com/fatedier/frp) (Fast Reverse Proxy), tracking the official releases.

### Installation

#### RHEL / Fedora

Add the repository to your system to receive automatic updates.

```bash
# Add repository
sudo dnf config-manager addrepo --from-repofile=https://go-frp.awfufu.com/go-frp.repo

# For old dnf
# sudo dnf config-manager --add-repo https://go-frp.awfufu.com/go-frp.repo

# Update and install
sudo dnf update
sudo dnf install frpc frps
```

#### Debian / Ubuntu

Add the repository to known lists.

```bash
# Add repository
echo "deb [trusted=yes] https://go-frp.awfufu.com/ ./" | sudo tee /etc/apt/sources.list.d/go-frp.list

# Update and install
sudo apt update
sudo apt install frpc frps
```

### Usage

#### Client (frpc)

1. Configuration: Edit the configuration file:

```bash
sudo vim /etc/frpc/frpc.toml
```

*For multiple instances, you can create separate config files like `/etc/frpc/my-proxy.toml`.*

2. Start Service:

```bash
# If using default /etc/frpc/frpc.toml:
sudo systemctl enable --now frpc@frpc

# If using /etc/frpc/my-proxy.toml:
sudo systemctl enable --now frpc@my-proxy
```

3. Check Status:

```bash
systemctl status frpc@frpc
```

#### Server (frps)

1. Configuration: Edit `/etc/frpc/frps.toml`.
2. Start Service:

```bash
sudo systemctl enable --now frps@frps
```

### Build Status

| Type | Status |
|------|--------|
| RPM  | ![Build Status](https://github.com/awfufu/frp-pkgs/actions/workflows/build_rpm.yml/badge.svg) |
| DEB  | ![Build Status](https://github.com/awfufu/frp-pkgs/actions/workflows/build_deb.yml/badge.svg) |
