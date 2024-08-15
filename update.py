import requests

china_list_url = "https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/accelerated-domains.china.conf"
apple_list_url = "https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/apple.china.conf"
out_file = "smartdns-domains.china.conf"


def fetch_and_extract_domains(url):
    response = requests.get(url)
    lines = response.text.splitlines()
    domains = set()
    for line in lines:
        line = line.strip()
        if line.startswith("server=/"):
            domain = line.split("/")[1]
            domains.add(domain)
    return domains


def write_domains_to_file(domains, file_path):
    with open(file_path, "w") as f:
        for domain in sorted(domains):
            f.write(domain + "\n")


def main():
    china_domains = fetch_and_extract_domains(china_list_url)
    apple_domains = fetch_and_extract_domains(apple_list_url)

    all_domains = china_domains.union(apple_domains)

    write_domains_to_file(all_domains, out_file)


if __name__ == "__main__":
    main()
