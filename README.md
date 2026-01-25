# FRP RPM Packages for Fedora

Auto RPM build for [frp](https://github.com/fatedier/frp) (Fast Reverse Proxy), tracking the official releases.

**Features:**
- **Automated**: Builds are triggered daily to check for new upstream releases.
- **Native**: Built natively for **Fedora 41, 42, 43**.
- **Multi-Arch**: Supports both **x86_64** (AMD64) and **aarch64** (ARM64).
- **Split Packages**: Separate `frpc` and `frps` packages.
- **Systemd Integration**: Includes `frpc@.service` and `frps@.service` templates.

### Installation

Add the repository to your system to receive automatic updates.

```bash
sudo dnf config-manager addrepo --from-repofile=https://awfufu.github.io/frp-pkgs/go-frp.repo

# For older DNF versions:
# sudo dnf config-manager --add-repo https://awfufu.github.io/frp-pkgs/go-frp.repo

sudo dnf install frpc frps
```

#### Debian / Ubuntu

Add the repository to known lists.

```bash
# Add repository
echo "deb https://awfufu.github.io/frp-pkgs/deb/ ./" | sudo tee /etc/apt/sources.list.d/go-frp.list

# Update and install
sudo apt update
sudo apt install frpc frps
```

### Usage

#### Client (frpc)

1. **Configuration**: Edit the configuration file:
   ```bash
   sudo vim /etc/frpc/frpc.toml
   ```
   *For multiple instances, you can create separate config files like `/etc/frpc/my-proxy.toml`.*

2. **Start Service**:
   ```bash
   # If using default /etc/frpc/frpc.toml:
   sudo systemctl enable --now frpc@frpc

   # If using /etc/frpc/my-proxy.toml:
   sudo systemctl enable --now frpc@my-proxy
   ```

3. **Check Status**:
   ```bash
   systemctl status frpc@frpc
   ```

#### Server (frps)

1. **Configuration**: Edit `/etc/frpc/frps.toml`.
2. **Start Service**:
   ```bash
   sudo systemctl enable --now frps@frps
   ```

#### Build Status

| Type | Status |
|------|--------|
| RPM  | ![Build Status](https://github.com/awfufu/frp-pkgs/actions/workflows/build_rpm.yml/badge.svg) |
| DEB  | ![Build Status](https://github.com/awfufu/frp-pkgs/actions/workflows/build_deb.yml/badge.svg) |
