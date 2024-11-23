import tkinter as tk
from tkinter import ttk, scrolledtext
from node_generator import NodeGenerator

class NodeGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("节点生成器")
        self.root.geometry("800x600")
        
        self.node_generator = NodeGenerator()
        
        # 创建选项卡
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both', padx=5, pady=5)
        
        # VLESS节点选项卡
        self.vless_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.vless_frame, text='VLESS节点')
        self.setup_vless_frame()
        
        # Trojan节点选项卡
        self.trojan_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.trojan_frame, text='Trojan节点')
        self.setup_trojan_frame()
        
        # noTLS VLESS节点选项卡
        self.notls_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.notls_frame, text='noTLS VLESS节点')
        self.setup_notls_frame()
        
        # 订阅链接选项卡
        self.sub_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.sub_frame, text='节点订阅链接')
        self.setup_sub_frame()

    def setup_vless_frame(self):
        # 域名1输入
        ttk.Label(self.vless_frame, text="域名1（每行一个）:").pack(pady=5)
        self.vless_domain1 = scrolledtext.ScrolledText(self.vless_frame, height=5)
        self.vless_domain1.pack(padx=5, pady=5, fill='x')
        
        # 域名2输入
        ttk.Label(self.vless_frame, text="域名2（每行一个）:").pack(pady=5)
        self.vless_domain2 = scrolledtext.ScrolledText(self.vless_frame, height=5)
        self.vless_domain2.pack(padx=5, pady=5, fill='x')
        
        # 生成按钮
        ttk.Button(self.vless_frame, text="生成VLESS节点", 
                   command=self.generate_vless).pack(pady=5)
        
        # 结果显示
        ttk.Label(self.vless_frame, text="生成结果:").pack(pady=5)
        self.vless_result = scrolledtext.ScrolledText(self.vless_frame, height=8)
        self.vless_result.pack(padx=5, pady=5, fill='both', expand=True)

    def setup_trojan_frame(self):
        # 域名1输入
        ttk.Label(self.trojan_frame, text="域名1（每行一个）:").pack(pady=5)
        self.trojan_domain1 = scrolledtext.ScrolledText(self.trojan_frame, height=5)
        self.trojan_domain1.pack(padx=5, pady=5, fill='x')
        
        # 域名2输入
        ttk.Label(self.trojan_frame, text="域名2（每行一个）:").pack(pady=5)
        self.trojan_domain2 = scrolledtext.ScrolledText(self.trojan_frame, height=5)
        self.trojan_domain2.pack(padx=5, pady=5, fill='x')
        
        # 生成按钮
        ttk.Button(self.trojan_frame, text="生成Trojan节点", 
                   command=self.generate_trojan).pack(pady=5)
        
        # 结果显示
        ttk.Label(self.trojan_frame, text="生成结果:").pack(pady=5)
        self.trojan_result = scrolledtext.ScrolledText(self.trojan_frame, height=8)
        self.trojan_result.pack(padx=5, pady=5, fill='both', expand=True)

    def setup_notls_frame(self):
        # 域名输入
        ttk.Label(self.notls_frame, text="域名（每行一个）:").pack(pady=5)
        self.notls_domain = scrolledtext.ScrolledText(self.notls_frame, height=5)
        self.notls_domain.pack(padx=5, pady=5, fill='x')
        
        # 生成按钮
        ttk.Button(self.notls_frame, text="生成noTLS VLESS节点", 
                   command=self.generate_notls).pack(pady=5)
        
        # 结果显示
        ttk.Label(self.notls_frame, text="生成结果:").pack(pady=5)
        self.notls_result = scrolledtext.ScrolledText(self.notls_frame, height=8)
        self.notls_result.pack(padx=5, pady=5, fill='both', expand=True)

    def setup_sub_frame(self):
        # 域名输入
        ttk.Label(self.sub_frame, text="域名（每行一个）:").pack(pady=5)
        self.sub_domain = scrolledtext.ScrolledText(self.sub_frame, height=5)
        self.sub_domain.pack(padx=5, pady=5, fill='x')
        
        # 生成按钮
        ttk.Button(self.sub_frame, text="生成订阅链接", 
                   command=self.generate_sub).pack(pady=5)
        
        # 结果显示
        ttk.Label(self.sub_frame, text="生成结果:").pack(pady=5)
        self.sub_result = scrolledtext.ScrolledText(self.sub_frame, height=8)
        self.sub_result.pack(padx=5, pady=5, fill='both', expand=True)

    def generate_vless(self):
        domains1 = self.vless_domain1.get('1.0', tk.END).strip().split('\n')
        domains2 = self.vless_domain2.get('1.0', tk.END).strip().split('\n')
        results = self.node_generator.generate_vless_nodes(domains1, domains2)
        self.vless_result.delete('1.0', tk.END)
        self.vless_result.insert('1.0', '\n'.join(results))

    def generate_trojan(self):
        domains1 = self.trojan_domain1.get('1.0', tk.END).strip().split('\n')
        domains2 = self.trojan_domain2.get('1.0', tk.END).strip().split('\n')
        results = self.node_generator.generate_trojan_nodes(domains1, domains2)
        self.trojan_result.delete('1.0', tk.END)
        self.trojan_result.insert('1.0', '\n'.join(results))

    def generate_notls(self):
        domains = self.notls_domain.get('1.0', tk.END).strip().split('\n')
        results = self.node_generator.generate_notls_nodes(domains)
        self.notls_result.delete('1.0', tk.END)
        self.notls_result.insert('1.0', '\n'.join(results))

    def generate_sub(self):
        domains = self.sub_domain.get('1.0', tk.END).strip().split('\n')
        results = self.node_generator.generate_sub_links(domains)
        self.sub_result.delete('1.0', tk.END)
        self.sub_result.insert('1.0', '\n'.join(results))

if __name__ == '__main__':
    root = tk.Tk()
    app = NodeGeneratorGUI(root)
    root.mainloop() 