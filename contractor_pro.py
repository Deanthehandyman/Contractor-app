import tkinter as tk
from tkinter import ttk, messagebox
from fpdf import FPDF
import json

class ContractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contractor Business-in-a-Box")
        self.root.geometry("500x600")

        self.tabs = ttk.Notebook(root)
        self.tab_web = ttk.Frame(self.tabs)
        self.tab_inv = ttk.Frame(self.tabs)
        
        self.tabs.add(self.tab_web, text="Website (SEO/GEO)")
        self.tabs.add(self.tab_inv, text="Invoices/Estimates")
        self.tabs.pack(expand=1, fill="both")

        self.setup_web_tab()
        self.setup_inv_tab()

    def setup_web_tab(self):
        # UI for Website Generation
        tk.Label(self.tab_web, text="Business Name:").pack(pady=5)
        self.ent_name = tk.Entry(self.tab_web, width=40); self.ent_name.pack()
        
        tk.Label(self.tab_web, text="City & State (e.g. Pittsburg, TX):").pack(pady=5)
        self.ent_loc = tk.Entry(self.tab_web, width=40); self.ent_loc.pack()

        tk.Label(self.tab_web, text="Main Service (for SEO):").pack(pady=5)
        self.ent_service = tk.Entry(self.tab_web, width=40); self.ent_service.pack()

        tk.Button(self.tab_web, text="🚀 Generate AI-Ready Website", command=self.build_site, bg="#28a745", fg="white").pack(pady=20)

    def setup_inv_tab(self):
        # UI for Invoicing
        tk.Label(self.tab_inv, text="Customer Name:").pack(pady=5)
        self.ent_cust = tk.Entry(self.tab_inv, width=40); self.ent_cust.pack()

        tk.Label(self.tab_inv, text="Job Description:").pack(pady=5)
        self.ent_job = tk.Entry(self.tab_inv, width=40); self.ent_job.pack()

        tk.Label(self.tab_inv, text="Total Amount ($):").pack(pady=5)
        self.ent_total = tk.Entry(self.tab_inv, width=40); self.ent_total.pack()

        tk.Button(self.tab_inv, text="📄 Generate PDF Invoice", command=self.build_invoice, bg="#007bff", fg="white").pack(pady=20)

    def build_site(self):
        name = self.ent_name.get()
        loc = self.ent_loc.get()
        svc = self.ent_service.get()

        # GEO/AEO Schema - This makes AI & Google trust the business
        schema = {
            "@context": "https://schema.org",
            "@type": "HomeAndConstructionBusiness",
            "name": name,
            "address": {"@type": "PostalAddress", "addressLocality": loc},
            "description": f"Professional {svc} provider in {loc}."
        }

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{name} | {svc} in {loc}</title>
            <script type="application/ld+json">{json.dumps(schema)}</script>
            <style>
                body {{ font-family: sans-serif; max-width: 800px; margin: auto; padding: 40px; line-height: 1.6; }}
                .cta {{ background: #ffcc00; padding: 20px; text-align: center; border-radius: 8px; font-weight: bold; }}
                h1 {{ color: #222; }}
            </style>
        </head>
        <body>
            <h1>{name} - {loc}</h1>
            <div class="cta">Need {svc}? Call for a Free Estimate!</div>
            <h2>Services Offered</h2>
            <ul><li>Professional {svc}</li><li>Locally Owned and Operated</li></ul>
            <h3>FAQ (For Voice Search)</h3>
            <p><strong>Who is the best {svc} in {loc}?</strong><br>{name} provides top-rated {svc} services to the {loc} community.</p>
        </body>
        </html>
        """
        with open("index.html", "w") as f: f.write(html)
        messagebox.showinfo("Success", "Website generated! Open index.html to see it.")

    def build_invoice(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt=f"INVOICE: {self.ent_name.get()}", ln=True, align='C')
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Customer: {self.ent_cust.get()}", ln=True)
        pdf.cell(200, 10, txt=f"Job: {self.ent_job.get()}", ln=True)
        pdf.cell(200, 10, txt=f"Total Due: ${self.ent_total.get()}", ln=True)
        pdf.cell(200, 20, txt="Payment accepted via Venmo/CashApp.", ln=True)
        pdf.output(f"Invoice_{self.ent_cust.get()}.pdf")
        messagebox.showinfo("Success", "PDF Invoice saved to your folder!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContractorApp(root)
    root.mainloop()
