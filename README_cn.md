# [frp packages](https://github.com/awfufu/frp-pkgs)

[English](README.md) | 简体中文

为 [fatedier/frp](https://github.com/fatedier/frp) 自动构建的软件包，紧跟官方发布版本。

![Build Status](https://github.com/awfufu/frp-pkgs/actions/workflows/build_publish.yml/badge.svg)

### 安装

#### RHEL / Fedora

```bash
# 添加仓库
sudo dnf config-manager addrepo --from-repofile=https://go-frp.awfufu.com/go-frp.repo

# 对于旧版本 dnf
# sudo dnf config-manager --add-repo https://go-frp.awfufu.com/go-frp.repo

# 更新并安装
sudo dnf update
sudo dnf install frpc frps
```

#### Debian / Ubuntu

```bash
# 1. 下载并添加 GPG 密钥
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://go-frp.awfufu.com/public.gpg | sudo gpg --dearmor -o /etc/apt/keyrings/go-frp.gpg

# 2. 添加仓库
echo "deb [arch=amd64,arm64 signed-by=/etc/apt/keyrings/go-frp.gpg] https://go-frp.awfufu.com stable main" | sudo tee /etc/apt/sources.list.d/go-frp.list

# 3. 更新并安装
sudo apt update
sudo apt install frpc frps
```

### 用法

#### 客户端 (frpc)

1. 配置

```bash
# 编辑配置文件
sudo vim /etc/frpc/frpc.toml
```

*对于多个实例，您可以创建单独的配置文件，例如 `/etc/frpc/my-proxy.toml`。*

2. 启动服务

```bash
# 如果使用默认的 /etc/frpc/frpc.toml：
sudo systemctl enable --now frpc
# 或者 (模板版本)
# sudo systemctl enable --now frpc@frpc

# 如果使用 /etc/frpc/my-proxy.toml：
sudo systemctl enable --now frpc@my-proxy
```

3. 查看状态

```bash
systemctl status frpc@frpc
```

#### 服务端 (frps)

1. 配置

```bash
# 编辑配置文件
sudo vim /etc/frps/frps.toml
```

2. 启动服务

```bash
sudo systemctl enable --now frps
# 或者 (模板版本)
sudo systemctl enable --now frps@frps
```

### 使用说明

- 本仓库使用 [GitHub Actions](https://github.com/awfufu/frp-pkgs/actions) 自动构建 [fatedier/frp](https://github.com/fatedier/frp) 的 RPM 和 DEB 软件包，并自动上传到由 Cloudflare 托管的静态页面 [go-frp.awfufu.com](https://go-frp.awfufu.com)。

- 本仓库不由 [fatedier/frp](https://github.com/fatedier/frp) 官方维护，仅提供自动打包的软件包。如果您遇到任何问题，请前往官方仓库提交 Issue。

- 安装软件包后，为了防止篡改，建议手动校验可执行文件的哈希值，并与[官方](https://github.com/fatedier/frp/releases)比对。

```bash
sha256sum /usr/bin/frpc /usr/bin/frps
```

