# smartdns-china-domain

适用于 smartdns 的中国网站白名单，内容来自 [felixonmars/dnsmasq-china-list](https://github.com/felixonmars/dnsmasq-china-list)，纯列表，自动更新。

## 使用步骤

1. 添加国内dns服务器, 设置为 `china` 组

```sh
# 都使用udp
电信 202.96.128.86
电信v6 240e:1f:1::1
腾讯 119.29.29.29
腾讯v6 2402:4e00:
阿里 223.5.5.5
阿里v6 2400:3200::1
百度 180.76.76.76
百度v6 2400:da00:6666
```

2. 添加国外dns服务器, 设置为 `gfw` 组, 并从 `default` 排除

```sh
OpenDNS https://208.67.222.222/dns-query
DNS.SB https://185.222.222.222/dns-query
CloudflareDNS https://1.1.1.1/dns-query
Quad9DNS https://9.9.9.9:5053/dns-query
```

3. 添加下载文件 `smartdns-domains.china.conf`

4. SmartDNS 自定义设置

```conf
# 关闭ddns域名的缓存, 域名过期缓存, 设置china组
domain-rules /*-a.example.com/ -no-cache -no-serve-expired -group china

# 加载china域名
domain-set -name china -file /etc/smartdns/domain-set/smartdns-domains.china.conf
# china域名使用china组的dns服务器
nameserver /domain-set:china/china
# 其余使用gfw组的dns服务器
nameserver /./gfw

# 设置缓存路径
cache-file /root/smartdns.cache
```