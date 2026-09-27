import hashlib
import datetime
import json
from flask import Flask, jsonify

app = Flask(__name__)

class HamadTamimGlobalDignityDashboard:
    def __init__(self, participant_name, passport_no, qid_no, base_income, role_type="Universal Contributor"):
        self.state_identity = "State of Qatar - Official Model"
        self.flag_colors = "Maroon & White (Al Adaam)"
        self.vision_target_year = 2030
        self.architect_vision = "Fulfilling Sir Hamid's eternal dream under Leader Tamim's master leadership by 2030."
        
        self.participant_name = participant_name
        self.qid_no = qid_no
        self.base_income = base_income
        self.role_type = role_type
        
        self.d_token = hashlib.sha256(f"{passport_no}{'dignity'}".encode()).hexdigest()
        self.legal_status = "Valued National Partner"  
        self.profile_access = "Participant_Controlled"

        self.system_status = "Active & Harmonized"
        self.latency_days = 0
        self.compliance_score = 100.0

        self.safety_contributions = 0.0
        self.partner_bonus_pool = 0.0
        self.deductions_log = []

        self.happiness_score = 10  
        self.emergency_support_active = False
        self.rescue_logs = []

        self.donation_wallet_balance = 1000.0  
        self.donation_history = []

        self.principal_paid = 0.0
        self.profit_rate = 0.06  
        self.exit_claims = []

        self.monthly_savings_locked = 0.0
        self.annual_profit_rate = 0.08  
        self.remittance_records = []

    def get_participant_identity(self):
        return {
            "Participant Name": self.participant_name,
            "Role Classification": self.role_type,
            "QID Number": self.qid_no,
            "D-Token ID": self.d_token[:16] + "...", 
            "Legal Status": self.legal_status,
            "Access Control": self.profile_access
        }

    def deposit_monthly_savings(self, monthly_amount):
        self.monthly_savings_locked += monthly_amount

    def process_annual_savings_profit_and_remittance(self, years_elapsed):
        if years_elapsed < 1:
            return
        total_accumulated_savings = self.monthly_savings_locked * 12 * years_elapsed
        annual_profit = total_accumulated_savings * self.annual_profit_rate * years_elapsed
        total_payout_amount = total_accumulated_savings + annual_profit
        
        record = {
            "QID": self.qid_no,
            "Years Elapsed": years_elapsed,
            "Total Principal Saved": total_accumulated_savings,
            "Annual Profit": round(annual_profit, 2),
            "Total Payout / Remittance": round(total_payout_amount, 2),
            "Status": "Ready for Secure Liquidation or Family Support",
            "Timestamp": str(datetime.datetime.now())
        }
        self.remittance_records.append(record)

    def generate_ht_gdd_summary(self):
        return {
            "State Branding": {
                "Entity": self.state_identity,
                "Colors": self.flag_colors,
                "Official Logo/Seal": "State of Qatar Emblem Active"
            },
            "Dashboard Title": "Hamad-Tamim Global Dignity & Telemetry Dashboard (HT-GDD)",
            "Strategic Vision Milestone (2030)": {
                "Target Year": self.vision_target_year,
                "Core Mission": self.architect_vision,
                "Leadership": "Leader Tamim fulfilling Sir Hamid's legacy by transforming Qatar into a universal dignity model."
            },
            "Scope": "Universal Model for All Contributors (Workers, Professionals & Business Owners)",
            "Identity": self.get_participant_identity(),
            "Telemetry": {
                "System Status": self.system_status,
                "Latency Days": self.latency_days,
                "Compliance Score": self.compliance_score
            },
            "Partner Finance (3-5 Years Fund)": {
                "Safety Contributions": self.safety_contributions,
                "Secured Bonus Pool": self.partner_bonus_pool
            },
            "Monthly Savings & Annual Growth": {
                "Active Vault Savings": self.monthly_savings_locked,
                "Records": self.remittance_records
            },
            "Early Transition / Exit Refunds": self.exit_claims,
            "Happiness Score": self.happiness_score,
            "Voluntary Donations": {
                "Wallet Balance": self.donation_wallet_balance,
                "History": self.donation_history
            },
            "Emergency Rescue Status": {
                "Active": self.emergency_support_active,
                "Logs": self.rescue_logs
            }
        }

# Initializing global node instance for server
node = HamadTamimGlobalDignityDashboard(
    participant_name="Universal Contributor Model Node", 
    passport_no="QA987654321", 
    qid_no="28475891234",
    base_income=5000,
    role_type="Universal Partner & Contributor"
)
for _ in range(12):
    node.deposit_monthly_savings(500)
node.process_annual_savings_profit_and_remittance(years_elapsed=1)

@app.route("/")
def home():
    return jsonify({
        "Announcement": "State of Qatar Official Model Branding (Maroon & White) - HT-GDD Active",
        "Vision": "Fulfilling Sir Hamid's Vision under Leader Tamim by 2030.",
        "Dashboard Data": node.generate_ht_gdd_summary()
    })

if __name__ == "__main__":
    print("Starting HT-GDD Server on http://127.0.0.1:5000 ...")
    app.run(host="0.0.0.0", port=5000, debug=True)