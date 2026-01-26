# [frp packages](https://github.com/awfufu/frp-pkgs)

English | [简体中文](README_cn.md)

Auto package build for [fatedier/frp](https://github.com/fatedier/frp), tracking the official releases.

![Build Status](https://github.com/awfufu/frp-pkgs/actions/workflows/build_publish.yml/badge.svg)

### Installation

#### RHEL / Fedora

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

```bash
# 1. Download and add GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://go-frp.awfufu.com/public.gpg | sudo gpg --dearmor -o /etc/apt/keyrings/go-frp.gpg

# 2. Add repository
echo "deb [arch=amd64,arm64 signed-by=/etc/apt/keyrings/go-frp.gpg] https://go-frp.awfufu.com stable main" | sudo tee /etc/apt/sources.list.d/go-frp.list

# 3. Update and install
sudo apt update
sudo apt install frpc frps
```

### Usage

#### Client (frpc)

1. Configuration

```bash
# Edit the configuration file
sudo vim /etc/frpc/frpc.toml
```

*For multiple instances, you can create separate config files like `/etc/frpc/my-proxy.toml`.*

2. Start Service

```bash
# If using default /etc/frpc/frpc.toml:
sudo systemctl enable --now frpc@frpc

# If using /etc/frpc/my-proxy.toml:
sudo systemctl enable --now frpc@my-proxy
```

3. Check Status

```bash
systemctl status frpc@frpc
```

#### Server (frps)

1. Configuration

```bash
# Edit the configuration file
sudo vim /etc/frps/frps.toml
```

2. Start Service

```bash
sudo systemctl enable --now frps@frps
```

### Notes

- This repository uses [GitHub Actions](https://github.com/awfufu/frp-pkgs/actions) to automatically build RPM and DEB packages for [fatedier/frp](https://github.com/fatedier/frp), and automatically uploads them to the static page [go-frp.awfufu.com](https://go-frp.awfufu.com) hosted by Cloudflare.

- This repository is not officially maintained by [fatedier/frp](https://github.com/fatedier/frp); it only provide automatically built packages. If you encounter any issues, please go to the official repository to submit an Issue.

- After installing the package, to prevent tampering, it is recommended to manually verify the hash of the executable file and compare it with the [official](https://github.com/fatedier/frp/releases) one.

```bash
sha256sum /usr/bin/frpc /usr/bin/frps
```
