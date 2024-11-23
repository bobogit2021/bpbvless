class NodeGenerator:
    def __init__(self):
        self.uuid = "89b3cbba-e6ac-485a-9481-976a0415eab9"
        self.base_domain = "visa.cn"
    
    def clean_domain(self, domain):
        """清理域名，删除https://前缀"""
        return domain.replace('https://', '').strip()
    
    def generate_vless_nodes(self, domains1, domains2):
        """生成VLESS节点"""
        results = []
        for d1, d2 in zip(domains1, domains2):
            if not d1.strip() or not d2.strip():
                continue
            d1 = self.clean_domain(d1)
            d2 = self.clean_domain(d2)
            node = (f"vless://{self.uuid}@{self.base_domain}:443?"
                   f"encryption=none&security=tls&sni={d1}&type=ws&"
                   f"host={d2}&path=%3Fed%3D2560#BPB共享节点")
            results.append(node)
        return results
    
    def generate_trojan_nodes(self, domains1, domains2):
        """生成Trojan节点"""
        results = []
        for d1, d2 in zip(domains1, domains2):
            if not d1.strip() or not d2.strip():
                continue
            d1 = self.clean_domain(d1)
            d2 = self.clean_domain(d2)
            node = (f"trojan://bpb-trojan@{self.base_domain}:443?"
                   f"security=tls&sni={d1}&type=ws&"
                   f"host={d2}&path=%2Ftr%3Fed%3D2560#BPB共享节点")
            results.append(node)
        return results
    
    def generate_notls_nodes(self, domains):
        """生成noTLS VLESS节点"""
        results = []
        for domain in domains:
            if not domain.strip():
                continue
            domain = self.clean_domain(domain)
            node = (f"vless://{self.uuid}@{self.base_domain}:80?"
                   f"encryption=none&security=none&type=ws&"
                   f"host={domain}&path=%3Fed%3D2560#BPB共享节点notls")
            results.append(node)
        return results
    
    def generate_sub_links(self, domains):
        """生成订阅链接"""
        results = []
        for domain in domains:
            if not domain.strip():
                continue
            domain = self.clean_domain(domain)
            link = f"https://{domain}/sub/{self.uuid}"
            results.append(link)
        return results 