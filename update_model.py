
import os

file_path = r"c:\Users\admin\Desktop\Проект РП\Release\Ancestral_Estate_Model.py"

new_content = r'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌲 NEURO-ESTATE OS v2.5 (Stable)
================================
The Operating System for Sustainable Life.

> "We are not building villages. We are engineering the future of human habitat."

This software simulates the economic and ecological lifecycle of a high-tech
ancestral estate ("Agro-Polis"). It calculates the ROI of returning to the land
equipped with AI, Robotics, and Decentralized Finance.

Target Audience: Engineers, Visionaries, and Future Settlers.
License: MIT
"""

import time
import random
import sys
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from enum import Enum

# --- CONFIGURATION & CONSTANTS ---

class TerminalColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def cprint(text: str, color: str = TerminalColors.ENDC, end: str = "\n"):
    """Print colored text to terminal."""
    sys.stdout.write(f"{color}{text}{TerminalColors.ENDC}{end}")
    sys.stdout.flush()

# --- DATA STRUCTURES ---

class TechLevel(Enum):
    BASIC = 1       # Manual labor, 4G internet
    ADVANCED = 2    # Automation, Starlink, Solar Panels
    FUTURISTIC = 3  # AI-Agro Drones, 3D-Printed Expansion, DAO Governance

@dataclass
class EstateConfig:
    family_name: str
    region: str
    initial_capital: float
    tech_level: TechLevel = TechLevel.BASIC

@dataclass
class FinancialReport:
    year: int
    revenue: float
    expenses: float
    net_income: float
    capital_valuation: float
    events: List[str]

# --- CORE LOGIC ---

class NeuroEstateKernel:
    """
    The core simulation engine. 
    Treats the estate as a programmable asset class.
    """
    
    def __init__(self, config: EstateConfig):
        self.config = config
        self.year = 0
        
        # Capital Assets (The "Balance Sheet")
        self.assets = {
            "land_infrastructure": 0.0,  # Tangible
            "ecosystem_services": 100_000.0, # Natural Capital (Soil, Air)
            "human_capital": 500_000.0,      # Health, Skills
            "social_capital": 50_000.0,      # Reputation, DAO tokens
            "crypto_reserves": 0.0           # Liquid assets
        }
        
        self.history: List[FinancialReport] = []
        self._initialize_system()

    def _initialize_system(self):
        """Bootstrapping the estate infrastructure."""
        cprint(f"\n[SYSTEM] Initializing NEURO-ESTATE for {self.config.family_name}...", TerminalColors.BLUE)
        time.sleep(0.5)
        
        # CAPEX (Capital Expenditure)
        capex = {
            "land_lease_99yr": 300_000,
            "prefab_module_45m": 2_500_000,
            "smart_grid_share": 400_000,
            "agri_bot_starter": 200_000,
            "runway_contribution": 100_000 # For light aviation
        }
        
        total_capex = sum(capex.values())
        self.assets["land_infrastructure"] = total_capex
        self.config.initial_capital -= total_capex
        
        cprint(f"├── 🏗️  Deploying Modular House (Prefab)... OK", TerminalColors.GREEN)
        time.sleep(0.2)
        cprint(f"├── 🛰️  Connecting Starlink/5G Node... OK", TerminalColors.GREEN)
        time.sleep(0.2)
        cprint(f"├── ✈️  Mapping Airstrip & Drone Routes... OK", TerminalColors.GREEN)
        time.sleep(0.2)
        cprint(f"└── 💳  Minting DAO Governance Tokens... OK", TerminalColors.GREEN)
        
        cprint(f"\n[FINANCE] Total CAPEX: {total_capex:,.0f} RUB", TerminalColors.WARNING)
        cprint(f"[STATUS] System Online. Simulation Started.", TerminalColors.BOLD)

    def _generate_random_event(self, year: int) -> tuple[float, str]:
        """Simulates black swans and golden geese."""
        events = [
            (0.1, "🌪️  Mild Drought (Agro yield -10%)", -50_000),
            (0.1, "📈  Crypto Bull Run (Savings +20%)", 150_000),
            (0.05, "🦄  Startup Exit (Unicorn Status!)", 5_000_000),
            (0.2, "🦠  New Virus (City Lockdown, Estate Value +++)", 0), # Value grows, cash flow same
            (0.3, "🎥  Viral TikTok about your Estate (Tourism +++)", 200_000),
            (0.25, "🧘  Nothing special, just happiness", 0)
        ]
        
        # Weighted random choice could be implemented, simple choice for now
        if random.random() > 0.7:
            evt = random.choice(events)
            return evt[2], evt[1]
        return 0, ""

    def run_year(self):
        self.year += 1
        tech_multiplier = 1.0
        
        # Tech Upgrades Logic
        if self.year == 3:
            self.config.tech_level = TechLevel.ADVANCED
            cprint(f"\n[UPGRADE] ⚡ System upgraded to ADVANCED (Solar + Automation)", TerminalColors.CYAN)
            tech_multiplier = 1.2
        elif self.year == 7:
            self.config.tech_level = TechLevel.FUTURISTIC
            cprint(f"\n[UPGRADE] 🤖 System upgraded to FUTURISTIC (AI Swarm + 3D Printing)", TerminalColors.CYAN)
            tech_multiplier = 1.5

        # Revenue Streams (The "P&L")
        # Base income grows with inflation and experience
        remote_work = 1_800_000 * (1.05 ** self.year) 
        
        # Agro income depends on tech level
        organic_sales = 600_000 * (1.1 ** self.year) * tech_multiplier if self.year > 1 else 0
        
        # Ecosystem services (Carbon Credits)
        carbon_credits = 180_000 * (1.15 ** self.year) if self.year > 3 else 0
        
        # Tourism & Education
        tourism = 720_000 * (1.1 ** self.year) * tech_multiplier if self.year > 2 else 0
        
        revenue = remote_work + organic_sales + carbon_credits + tourism
        
        # Expenses (Deflationary due to autonomy!)
        # Living costs drop as you grow your own food and generate energy
        base_expense = 1_200_000
        autonomy_discount = min(0.5, 0.02 * self.year * tech_multiplier) # Max 50% discount
        expenses = base_expense * (1 - autonomy_discount) * (1.03 ** self.year) # Inflation still exists
        
        # Random Events
        event_impact, event_desc = self._generate_random_event(self.year)
        revenue += event_impact
        
        net_income = revenue - expenses
        self.assets["crypto_reserves"] += net_income
        
        # Asset Appreciation (The "HODL" effect)
        self.assets["land_infrastructure"] *= 1.08 # Real estate growth
        self.assets["ecosystem_services"] *= 1.12  # Nature heals and grows
        self.assets["human_capital"] *= 1.05       # Health improves
        self.assets["social_capital"] *= 1.10      # Community grows
        
        total_valuation = sum(self.assets.values())
        
        report = FinancialReport(
            year=self.year,
            revenue=revenue,
            expenses=expenses,
            net_income=net_income,
            capital_valuation=total_valuation,
            events=[event_desc] if event_desc else []
        )
        self.history.append(report)
        return report

# --- INTERFACE & VISUALIZATION ---

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
    """Call in a loop to create terminal progress bar"""
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
    if iteration == total: 
        sys.stdout.write('\n')

def main():
    # Header
    print("\n" * 2)
    cprint("   🌲 NEURO-ESTATE SIMULATION v2.5   ", TerminalColors.HEADER)
    cprint("   =================================   ", TerminalColors.HEADER)
    print("   Initializing Kernel... [OK]")
    print("   Loading Economic Models... [OK]")
    print("   Connecting to Global DAO... [OK]")
    print("\n")

    # User Input
    try:
        family = input(f"{TerminalColors.BOLD}Enter Family Name (default: Sokolov): {TerminalColors.ENDC}") or "Sokolov"
        years = int(input(f"{TerminalColors.BOLD}Simulation Horizon (years, default: 15): {TerminalColors.ENDC}") or 15)
    except ValueError:
        years = 15

    # Config
    config = EstateConfig(
        family_name=family,
        region="Central Russia",
        initial_capital=10_000_000 # Virtual credit line
    )
    
    kernel = NeuroEstateKernel(config)
    
    # Simulation Loop
    print("\n")
    cprint(f"{'YEAR':<5} | {'REVENUE':<12} | {'NET INCOME':<12} | {'ASSET VALUE':<15} | {'EVENT'}", TerminalColors.BLUE)
    print("-" * 80)
    
    for y in range(years):
        # Visual delay for effect
        time.sleep(0.1) 
        report = kernel.run_year()
        
        event_str = report.events[0] if report.events else ""
        
        # Color coding for net income
        income_color = TerminalColors.GREEN if report.net_income > 0 else TerminalColors.FAIL
        
        print(f"{report.year:<5} | "
              f"{report.revenue/1e6:6.1f}M RUB  | "
              f"{income_color}{report.net_income/1e6:6.1f}M RUB{TerminalColors.ENDC}  | "
              f"{report.capital_valuation/1e6:6.1f}M RUB      | "
              f"{event_str}")

    # Final Report
    print("\n")
    cprint("✨ SIMULATION COMPLETE. GENERATING FINAL REPORT...", TerminalColors.HEADER)
    time.sleep(1)
    
    final_assets = kernel.assets
    total_value = sum(final_assets.values())
    roi = (total_value - 4_000_000) / 4_000_000 * 100 # Assuming ~4M initial real investment
    
    print("-" * 50)
    cprint(f"🏆 FAMILY: {family.upper()}", TerminalColors.BOLD)
    cprint(f"📅 TIMEFRAME: {years} Years", TerminalColors.BOLD)
    print("-" * 50)
    
    cprint(f"💰 TOTAL ASSET VALUE: {total_value:,.0f} RUB", TerminalColors.GREEN)
    cprint(f"📈 ROI (Return on Investment): {roi:.1f}%", TerminalColors.CYAN)
    print("-" * 50)
    
    print("ASSET BREAKDOWN:")
    print(f"  🏡 Real Estate & Infra:  {final_assets['land_infrastructure']:,.0f}")
    print(f"  🌳 Natural Capital:      {final_assets['ecosystem_services']:,.0f}")
    print(f"  🧠 Human Capital:        {final_assets['human_capital']:,.0f}")
    print(f"  💳 Crypto/Cash Reserves: {final_assets['crypto_reserves']:,.0f}")
    
    print("\n")
    cprint("🔮 AI VERDICT:", TerminalColors.HEADER)
    print("The model demonstrates that 'Ancestral Estate 2.0' is not just a lifestyle choice,")
    print("but a high-yield venture capital asset. By combining low-cost living with")
    print("high-tech income streams, you achieve financial singularity by Year 7.")
    print("\n> Welcome to the future. Welcome home.")
    print("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Simulation Aborted.")
'''

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Successfully updated {file_path}")
