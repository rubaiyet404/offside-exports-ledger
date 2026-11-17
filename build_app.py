#!/usr/bin/env python3
"""
OFFSIDE EXPORTS - Customer Ledger & Payment Management Web Application Generator
Produces the complete, production-ready, beautiful index.html with embedded branding.
"""

import os

# Read the base64 logo if available
logo_base64 = ""
if os.path.exists('logo_base64.txt'):
    with open('logo_base64.txt', 'r', encoding='utf-8') as f:
        logo_base64 = f.read().strip()

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="bn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>OFFSIDE EXPORTS | কাস্টমার পেমেন্ট ও বাকি হিসাব (Customer Ledger & Accounts)</title>
  <link rel="icon" type="image/jpeg" href="__LOGO_DATA__">

  <!-- Google Fonts: Outfit & Plus Jakarta Sans & Hind Siliguri for Bengali -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <!-- Font Awesome 6 Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <style>
    /* ==========================================================================
       1. THEME & DESIGN TOKENS
       Brand: OFFSIDE EXPORTS (Midnight Navy, Royal Cyber Blue, Gold & Crisp White)
       ========================================================================== */
    :root {
      --bg-dark: #040914;
      --bg-surface: #081224;
      --bg-card: #0d1a33;
      --bg-card-hover: #122447;
      --border-subtle: #192d52;
      --border-light: rgba(59, 130, 246, 0.25);

      --blue-primary: #1d4ed8;
      --blue-accent: #2563eb;
      --blue-glow: #38bdf8;
      --blue-glow-shadow: rgba(56, 189, 248, 0.25);

      --gold-primary: #d4af37;
      --gold-glow: #f59e0b;
      --gold-bg: rgba(245, 158, 11, 0.12);

      --bkash-pink: #e2136e;
      --bkash-glow: rgba(226, 19, 110, 0.3);
      --rocket-purple: #8b1fa8;
      --rocket-glow: rgba(139, 31, 168, 0.3);
      --whatsapp-green: #25d366;

      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --text-dim: #64748b;

      --status-paid-bg: rgba(16, 185, 129, 0.16);
      --status-paid-border: #10b981;
      --status-paid-text: #34d399;

      --status-partial-bg: rgba(245, 158, 11, 0.16);
      --status-partial-border: #f59e0b;
      --status-partial-text: #fbbf24;

      --status-due-bg: rgba(239, 68, 68, 0.16);
      --status-due-border: #ef4444;
      --status-due-text: #f87171;

      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --radius-xl: 20px;
      --radius-pill: 9999px;

      --shadow-card: 0 10px 25px -5px rgba(0, 0, 0, 0.5), 0 8px 10px -6px rgba(0, 0, 0, 0.5);
      --shadow-glow: 0 0 20px rgba(37, 99, 235, 0.25);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', 'Hind Siliguri', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--bg-dark);
      background-image: 
        radial-gradient(circle at 15% 10%, rgba(37, 99, 235, 0.12) 0%, transparent 40%),
        radial-gradient(circle at 85% 80%, rgba(226, 19, 110, 0.08) 0%, transparent 45%),
        radial-gradient(circle at 50% 50%, rgba(13, 26, 51, 0.6) 0%, transparent 80%);
      background-attachment: fixed;
      color: var(--text-main);
      min-height: 100vh;
      line-height: 1.5;
      overflow-x: hidden;
    }

    /* Scrollbar */
    ::-webkit-scrollbar {
      width: 8px;
      height: 8px;
    }
    ::-webkit-scrollbar-track {
      background: var(--bg-surface);
    }
    ::-webkit-scrollbar-thumb {
      background: var(--border-subtle);
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: var(--blue-accent);
    }

    /* Container */
    .container {
      max-width: 1440px;
      margin: 0 auto;
      padding: 0 20px;
    }

    /* ==========================================================================
       2. TOP PROMINENT PAYMENT & BRAND HEADER
       ========================================================================== */
    .header-bar {
      background: rgba(8, 18, 36, 0.88);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--border-subtle);
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    }

    .header-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 12px 0;
      gap: 16px;
      flex-wrap: wrap;
    }

    .brand-section {
      display: flex;
      align-items: center;
      gap: 14px;
      text-decoration: none;
    }

    .brand-logo-wrap {
      position: relative;
      width: 52px;
      height: 52px;
      border-radius: 14px;
      overflow: hidden;
      border: 2px solid rgba(56, 189, 248, 0.6);
      box-shadow: 0 0 15px rgba(37, 99, 235, 0.4);
      background: #000;
      flex-shrink: 0;
    }

    .brand-logo-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    .brand-titles h1 {
      font-family: 'Outfit', sans-serif;
      font-size: 1.35rem;
      font-weight: 800;
      letter-spacing: 0.5px;
      background: linear-gradient(135deg, #ffffff 30%, #38bdf8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      line-height: 1.15;
    }

    .brand-subtitle {
      font-size: 0.78rem;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 6px;
      margin-top: 2px;
    }

    .estd-badge {
      background: var(--gold-bg);
      color: var(--gold-primary);
      padding: 1px 7px;
      border-radius: 6px;
      font-size: 0.7rem;
      font-weight: 700;
      border: 1px solid rgba(212, 175, 55, 0.3);
    }

    /* Payment Channels in Top Banner (Requested by User) */
    .payment-pills-bar {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .pay-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 7px 14px;
      border-radius: var(--radius-pill);
      font-size: 0.85rem;
      font-weight: 600;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      transition: all 0.2s ease;
      cursor: pointer;
      user-select: none;
    }

    .pay-pill:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }

    .pay-pill.bkash {
      border-color: rgba(226, 19, 110, 0.4);
      background: rgba(226, 19, 110, 0.1);
      color: #ff529c;
    }
    .pay-pill.bkash:hover {
      box-shadow: 0 0 16px var(--bkash-glow);
      border-color: #e2136e;
    }

    .pay-pill.rocket {
      border-color: rgba(139, 31, 168, 0.4);
      background: rgba(139, 31, 168, 0.1);
      color: #d16ce9;
    }
    .pay-pill.rocket:hover {
      box-shadow: 0 0 16px var(--rocket-glow);
      border-color: #8b1fa8;
    }

    .pay-pill.whatsapp {
      border-color: rgba(37, 211, 102, 0.4);
      background: rgba(37, 211, 102, 0.1);
      color: #4ade80;
      text-decoration: none;
    }
    .pay-pill.whatsapp:hover {
      box-shadow: 0 0 16px rgba(37, 211, 102, 0.3);
      border-color: var(--whatsapp-green);
    }

    .copy-chip {
      font-size: 0.72rem;
      background: rgba(255, 255, 255, 0.12);
      padding: 2px 7px;
      border-radius: 6px;
      margin-left: 2px;
      color: #fff;
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .db-status-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      border-radius: var(--radius-pill);
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: #34d399;
      font-size: 0.78rem;
      font-weight: 600;
    }

    .status-dot-pulse {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 8px #10b981;
      animation: pulse 1.8s infinite;
    }

    @keyframes pulse {
      0% { opacity: 0.4; transform: scale(0.9); }
      50% { opacity: 1; transform: scale(1.15); }
      100% { opacity: 0.4; transform: scale(0.9); }
    }

    /* Buttons */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 9px 18px;
      border-radius: var(--radius-md);
      font-size: 0.88rem;
      font-weight: 600;
      cursor: pointer;
      border: none;
      transition: all 0.2s ease;
      font-family: inherit;
      text-decoration: none;
    }

    .btn-primary {
      background: linear-gradient(135deg, #2563eb, #1d4ed8);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(37, 99, 235, 0.4);
    }
    .btn-primary:hover {
      background: linear-gradient(135deg, #3b82f6, #2563eb);
      box-shadow: 0 6px 20px rgba(37, 99, 235, 0.6);
      transform: translateY(-1px);
    }

    .btn-success {
      background: linear-gradient(135deg, #10b981, #059669);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4);
    }
    .btn-success:hover {
      background: linear-gradient(135deg, #34d399, #10b981);
      box-shadow: 0 6px 20px rgba(16, 185, 129, 0.6);
      transform: translateY(-1px);
    }

    .btn-outline {
      background: transparent;
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
    }
    .btn-outline:hover {
      background: var(--bg-card-hover);
      border-color: var(--blue-accent);
      color: #ffffff;
    }

    .btn-sm {
      padding: 6px 12px;
      font-size: 0.78rem;
      border-radius: var(--radius-sm);
    }

    /* ==========================================================================
       3. TOP SUMMARY KPI CARDS (Matching User's Google Sheet Headers)
       ========================================================================== */
    .summary-section {
      padding: 24px 0 16px 0;
    }

    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
    }

    .kpi-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 20px 22px;
      position: relative;
      overflow: hidden;
      box-shadow: var(--shadow-card);
      transition: transform 0.2s ease, border-color 0.2s ease;
    }

    .kpi-card:hover {
      transform: translateY(-3px);
      border-color: var(--border-light);
    }

    .kpi-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 4px;
    }

    .kpi-card.bill::before { background: linear-gradient(90deg, #3b82f6, #60a5fa); }
    .kpi-card.received::before { background: linear-gradient(90deg, #10b981, #34d399); }
    .kpi-card.due::before { background: linear-gradient(90deg, #ef4444, #f87171); }
    .kpi-card.clients::before { background: linear-gradient(90deg, #d4af37, #f59e0b); }

    .kpi-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 10px;
    }

    .kpi-title {
      font-size: 0.84rem;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .kpi-icon-wrap {
      width: 42px;
      height: 42px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.15rem;
    }

    .kpi-card.bill .kpi-icon-wrap { background: rgba(59, 130, 246, 0.15); color: #60a5fa; }
    .kpi-card.received .kpi-icon-wrap { background: rgba(16, 185, 129, 0.15); color: #34d399; }
    .kpi-card.due .kpi-icon-wrap { background: rgba(239, 68, 68, 0.15); color: #f87171; }
    .kpi-card.clients .kpi-icon-wrap { background: rgba(212, 175, 55, 0.15); color: var(--gold-primary); }

    .kpi-value {
      font-family: 'Outfit', sans-serif;
      font-size: 1.9rem;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.1;
      margin-bottom: 6px;
    }

    .kpi-meta {
      font-size: 0.78rem;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .progress-bar-bg {
      width: 100%;
      height: 6px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 3px;
      margin-top: 10px;
      overflow: hidden;
    }

    .progress-bar-fill {
      height: 100%;
      background: linear-gradient(90deg, #10b981, #34d399);
      border-radius: 3px;
      transition: width 0.4s ease;
    }

    /* ==========================================================================
       4. CONTROLS, SEARCH & FILTER TOOLBAR
       ========================================================================== */
    .toolbar-section {
      padding: 10px 0 20px 0;
    }

    .toolbar-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 16px 20px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .toolbar-top-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }

    .search-input-wrap {
      position: relative;
      flex: 1;
      min-width: 280px;
    }

    .search-input-wrap i {
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
      font-size: 0.9rem;
    }

    .search-input {
      width: 100%;
      background: var(--bg-dark);
      border: 1px solid var(--border-subtle);
      padding: 10px 14px 10px 38px;
      border-radius: var(--radius-md);
      color: var(--text-main);
      font-size: 0.88rem;
      font-family: inherit;
      outline: none;
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }

    .search-input:focus {
      border-color: var(--blue-accent);
      box-shadow: 0 0 10px rgba(37, 99, 235, 0.3);
    }

    .search-input::placeholder {
      color: var(--text-dim);
    }

    .toolbar-actions {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .filter-tabs-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
      padding-top: 12px;
      border-top: 1px solid rgba(255, 255, 255, 0.05);
    }

    .status-filter-pills {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .filter-pill {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      padding: 6px 14px;
      border-radius: var(--radius-pill);
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
      font-family: inherit;
    }

    .filter-pill:hover {
      background: var(--bg-card-hover);
      color: var(--text-main);
    }

    .filter-pill.active {
      background: var(--blue-accent);
      border-color: var(--blue-accent);
      color: #ffffff;
      box-shadow: 0 2px 10px rgba(37, 99, 235, 0.4);
    }

    .filter-pill.active.due-pill {
      background: #ef4444;
      border-color: #ef4444;
      box-shadow: 0 2px 10px rgba(239, 68, 68, 0.4);
    }

    .filter-pill.active.partial-pill {
      background: #f59e0b;
      border-color: #f59e0b;
      box-shadow: 0 2px 10px rgba(245, 158, 11, 0.4);
    }

    .filter-pill.active.paid-pill {
      background: #10b981;
      border-color: #10b981;
      box-shadow: 0 2px 10px rgba(16, 185, 129, 0.4);
    }

    .count-tag {
      background: rgba(0, 0, 0, 0.35);
      padding: 1px 6px;
      border-radius: 8px;
      font-size: 0.72rem;
    }

    .filter-dropdowns {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .select-input {
      background: var(--bg-dark);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      padding: 6px 12px;
      border-radius: var(--radius-sm);
      font-size: 0.8rem;
      font-family: inherit;
      outline: none;
      cursor: pointer;
    }
    .select-input:focus {
      border-color: var(--blue-accent);
    }

    /* ==========================================================================
       5. LEDGER TABLE SECTION (EXCEL LOOK & FEEL)
       ========================================================================== */
    .table-section {
      padding-bottom: 60px;
    }

    .table-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-card);
    }

    .table-header-meta {
      padding: 14px 20px;
      background: var(--bg-card);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
    }

    .table-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .table-sub-hint {
      font-size: 0.76rem;
      color: var(--text-muted);
    }

    .table-responsive {
      width: 100%;
      overflow-x: auto;
    }

    .ledger-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.86rem;
      text-align: left;
    }

    .ledger-table thead th {
      background: #09152b;
      color: #cbd5e1;
      font-weight: 700;
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.4px;
      padding: 14px 14px;
      border-bottom: 1px solid var(--border-subtle);
      white-space: nowrap;
    }

    .ledger-table thead th.text-right {
      text-align: right;
    }
    .ledger-table thead th.text-center {
      text-align: center;
    }

    .ledger-table tbody tr {
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
      transition: background 0.15s ease;
    }

    .ledger-table tbody tr:hover {
      background: rgba(37, 99, 235, 0.07);
    }

    .ledger-table tbody td {
      padding: 12px 14px;
      vertical-align: middle;
      color: #e2e8f0;
    }

    .ledger-table tbody td.text-right {
      text-align: right;
    }
    .ledger-table tbody td.text-center {
      text-align: center;
    }

    .client-cell {
      font-weight: 600;
      color: #ffffff;
      display: flex;
      flex-direction: column;
    }

    .client-sub {
      font-size: 0.72rem;
      color: var(--text-muted);
      font-weight: normal;
    }

    .badge-status {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 3px 10px;
      border-radius: var(--radius-pill);
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }

    .badge-status.paid {
      background: var(--status-paid-bg);
      color: var(--status-paid-text);
      border: 1px solid var(--status-paid-border);
    }

    .badge-status.partial {
      background: var(--status-partial-bg);
      color: var(--status-partial-text);
      border: 1px solid var(--status-partial-border);
    }

    .badge-status.due {
      background: var(--status-due-bg);
      color: var(--status-due-text);
      border: 1px solid var(--status-due-border);
    }

    .pay-badge {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 2px 8px;
      border-radius: 6px;
      font-size: 0.72rem;
      font-weight: 600;
    }
    .pay-badge.bkash {
      background: rgba(226, 19, 110, 0.15);
      color: #ff64a5;
      border: 1px solid rgba(226, 19, 110, 0.3);
    }
    .pay-badge.rocket {
      background: rgba(139, 31, 168, 0.15);
      color: #dc7df1;
      border: 1px solid rgba(139, 31, 168, 0.3);
    }
    .pay-badge.cash {
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.3);
    }
    .pay-badge.nagad {
      background: rgba(249, 115, 22, 0.15);
      color: #fb923c;
      border: 1px solid rgba(249, 115, 22, 0.3);
    }

    .amount-due-highlight {
      font-weight: 700;
      font-family: 'Outfit', sans-serif;
      font-size: 0.92rem;
      color: #f87171;
    }
    .amount-due-highlight.cleared {
      color: #34d399;
      font-weight: 500;
    }

    .amount-val {
      font-family: 'Outfit', sans-serif;
      font-weight: 600;
    }

    /* Actions in table */
    .row-actions {
      display: flex;
      align-items: center;
      justify-content: flex-end;
      gap: 6px;
    }

    .action-btn {
      width: 32px;
      height: 32px;
      border-radius: var(--radius-sm);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.18s ease;
      font-size: 0.82rem;
    }

    .action-btn:hover {
      background: var(--bg-card-hover);
      color: #fff;
      border-color: var(--blue-accent);
      transform: translateY(-1px);
    }

    .action-btn.pay:hover {
      background: #10b981;
      border-color: #10b981;
      color: #fff;
    }

    .action-btn.wa:hover {
      background: #25d366;
      border-color: #25d366;
      color: #fff;
    }

    .action-btn.del:hover {
      background: #ef4444;
      border-color: #ef4444;
      color: #fff;
    }

    .empty-state {
      padding: 60px 20px;
      text-align: center;
      color: var(--text-muted);
    }

    .empty-state i {
      font-size: 3rem;
      color: var(--text-dim);
      margin-bottom: 12px;
    }

    /* ==========================================================================
       6. MODAL DIALOGS
       ========================================================================== */
    .modal-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(3, 7, 18, 0.8);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 1000;
      padding: 16px;
    }

    .modal-overlay.active {
      display: flex;
      animation: fadeIn 0.2s ease;
    }

    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }

    .modal-box {
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      width: 100%;
      max-width: 600px;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
      animation: modalSlideUp 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes modalSlideUp {
      from { transform: translateY(20px) scale(0.97); }
      to { transform: translateY(0) scale(1); }
    }

    .modal-header {
      padding: 18px 24px;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      background: var(--bg-surface);
      z-index: 10;
    }

    .modal-title {
      font-family: 'Outfit', sans-serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .modal-close-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 1.2rem;
      cursor: pointer;
      width: 32px;
      height: 32px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .modal-close-btn:hover {
      background: rgba(255, 255, 255, 0.1);
      color: #fff;
    }

    .modal-body {
      padding: 24px;
    }

    .form-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }

    .form-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .form-group.full-width {
      grid-column: span 2;
    }

    .form-label {
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--text-muted);
    }

    .form-label span.req {
      color: #ef4444;
    }

    .form-control {
      background: var(--bg-dark);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 10px 14px;
      color: var(--text-main);
      font-size: 0.88rem;
      font-family: inherit;
      outline: none;
      transition: all 0.2s ease;
    }

    .form-control:focus {
      border-color: var(--blue-accent);
      box-shadow: 0 0 10px rgba(37, 99, 235, 0.3);
    }

    .calculation-callout {
      background: rgba(37, 99, 235, 0.1);
      border: 1px solid rgba(37, 99, 235, 0.3);
      border-radius: var(--radius-md);
      padding: 14px 18px;
      margin-top: 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      grid-column: span 2;
    }

    .calc-item {
      display: flex;
      flex-direction: column;
    }

    .calc-label {
      font-size: 0.74rem;
      color: var(--text-muted);
      text-transform: uppercase;
      font-weight: 600;
    }

    .calc-value {
      font-family: 'Outfit', sans-serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
    }

    .calc-value.due-highlight {
      color: #f87171;
    }

    .modal-footer {
      padding: 18px 24px;
      border-top: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: flex-end;
      gap: 12px;
      background: var(--bg-surface);
      position: sticky;
      bottom: 0;
    }

    /* Quick Pay Modal specific */
    .quick-pay-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 16px;
      margin-bottom: 18px;
    }

    .qp-row {
      display: flex;
      justify-content: space-between;
      font-size: 0.85rem;
      padding: 4px 0;
      color: var(--text-muted);
    }
    .qp-row strong {
      color: #fff;
      font-family: 'Outfit', sans-serif;
    }

    /* Money Receipt Print View */
    .receipt-container {
      background: #ffffff;
      color: #0f172a;
      border-radius: 12px;
      padding: 24px;
      font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .receipt-header {
      text-align: center;
      border-bottom: 2px dashed #cbd5e1;
      padding-bottom: 16px;
      margin-bottom: 16px;
    }

    .receipt-header h2 {
      font-size: 1.35rem;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: 1px;
    }

    .receipt-contacts {
      font-size: 0.78rem;
      color: #475569;
      margin-top: 4px;
    }

    .receipt-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.85rem;
      margin: 16px 0;
    }

    .receipt-table td {
      padding: 8px 0;
      border-bottom: 1px solid #f1f5f9;
    }

    .receipt-total-row {
      font-weight: 700;
      font-size: 0.95rem;
      border-top: 2px solid #0f172a;
    }

    /* Toast Notification */
    .toast-container {
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 9999;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .toast {
      background: #0d1a33;
      border: 1px solid var(--blue-accent);
      border-left: 4px solid var(--blue-glow);
      color: #fff;
      padding: 12px 20px;
      border-radius: var(--radius-md);
      font-size: 0.86rem;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
      display: flex;
      align-items: center;
      gap: 12px;
      animation: slideInRight 0.25s ease;
    }

    .toast.success {
      border-left-color: #10b981;
    }

    @keyframes slideInRight {
      from { transform: translateX(100%); opacity: 0; }
      to { transform: translateX(0); opacity: 1; }
    }

    /* Responsive */
    @media (max-width: 768px) {
      .header-inner {
        flex-direction: column;
        align-items: flex-start;
      }
      .payment-pills-bar {
        width: 100%;
        justify-content: flex-start;
      }
      .form-grid {
        grid-template-columns: 1fr;
      }
      .form-group.full-width {
        grid-column: span 1;
      }
      .calculation-callout {
        grid-column: span 1;
        flex-direction: column;
        gap: 8px;
        align-items: flex-start;
      }
    }
  </style>
</head>
<body>

  <!-- ==========================================================================
       1. TOP BRANDING & PAYMENT CHANNELS HEADER
       ========================================================================== -->
  <header class="header-bar">
    <div class="container header-inner">

      <!-- Brand Logo & Title -->
      <a href="#" class="brand-section">
        <div class="brand-logo-wrap">
          <img src="__LOGO_DATA__" alt="Offside Exports Logo" class="brand-logo-img">
        </div>
        <div class="brand-titles">
          <h1>OFFSIDE EXPORTS</h1>
          <div class="brand-subtitle">
            <span class="estd-badge">ESTD 2026</span>
            <span>কাস্টমার পেমেন্ট ও বাকি খাতা</span>
          </div>
        </div>
      </a>

      <!-- User's Requested Payment Numbers Bar (Click to Copy) -->
      <div class="payment-pills-bar">
        <div class="pay-pill bkash" onclick="copyPaymentNumber('01834093932', 'bKash')" title="ক্লিক করে bKash নাম্বার কপি করুন">
          <i class="fa-solid fa-mobile-screen"></i>
          <span>bKash: <strong>01834093932</strong></span>
          <span class="copy-chip"><i class="fa-regular fa-copy"></i> কপি</span>
        </div>

        <div class="pay-pill rocket" onclick="copyPaymentNumber('018927170930', 'Rocket')" title="ক্লিক করে Rocket নাম্বার কপি করুন">
          <i class="fa-solid fa-bolt"></i>
          <span>Rocket: <strong>018927170930</strong></span>
          <span class="copy-chip"><i class="fa-regular fa-copy"></i> কপি</span>
        </div>

        <a href="https://wa.me/8801892717093" target="_blank" class="pay-pill whatsapp" title="WhatsApp এ মেসেজ পাঠান">
          <i class="fa-brands fa-whatsapp"></i>
          <span>WhatsApp: <strong>01892717093</strong></span>
        </a>
      </div>

      <!-- Database Status & New Customer Button -->
      <div class="header-actions">
        <div class="db-status-pill" id="db-status-indicator" title="ডাটাবেজ কানেকশন স্ট্যাটাস">
          <span class="status-dot-pulse"></span>
          <span id="db-status-text">SQLite Database Connected</span>
        </div>

        <button class="btn btn-primary" onclick="openAddModal()">
          <i class="fa-solid fa-user-plus"></i>
          <span>হিসাব যোগ করুন</span>
        </button>
      </div>

    </div>
  </header>

  <main class="container">

    <!-- ==========================================================================
         2. KPI SUMMARY METRIC CARDS (Matching Google Sheet Top Row)
         ========================================================================== -->
    <section class="summary-section">
      <div class="kpi-grid">

        <!-- Total Bill -->
        <div class="kpi-card bill">
          <div class="kpi-header">
            <span class="kpi-title">মোট বিক্রি (Total Bill)</span>
            <div class="kpi-icon-wrap"><i class="fa-solid fa-file-invoice-dollar"></i></div>
          </div>
          <div class="kpi-value">৳ <span id="kpi-total-bill">0</span></div>
          <div class="kpi-meta">
            <i class="fa-solid fa-arrow-trend-up"></i>
            <span>সকল অর্ডারের সমন্বিত মূল্য</span>
          </div>
        </div>

        <!-- Total Received -->
        <div class="kpi-card received">
          <div class="kpi-header">
            <span class="kpi-title">মোট আদায় (Received)</span>
            <div class="kpi-icon-wrap"><i class="fa-solid fa-money-bill-trend-up"></i></div>
          </div>
          <div class="kpi-value">৳ <span id="kpi-total-received">0</span></div>
          <div class="kpi-meta">
            <span>আদায় হার: <strong id="kpi-collection-rate">0%</strong></span>
          </div>
          <div class="progress-bar-bg">
            <div class="progress-bar-fill" id="kpi-progress-bar" style="width: 0%;"></div>
          </div>
        </div>

        <!-- Total Receivable / Due -->
        <div class="kpi-card due">
          <div class="kpi-header">
            <span class="kpi-title">মোট বাকি (Receivable / Due)</span>
            <div class="kpi-icon-wrap"><i class="fa-solid fa-hand-holding-dollar"></i></div>
          </div>
          <div class="kpi-value">৳ <span id="kpi-total-due">0</span></div>
          <div class="kpi-meta">
            <i class="fa-solid fa-triangle-exclamation" style="color: #f87171;"></i>
            <span>গ্রাহকদের কাছে পাওনা বাকি টাকা</span>
          </div>
        </div>

        <!-- Customer Summary Breakdown -->
        <div class="kpi-card clients">
          <div class="kpi-header">
            <span class="kpi-title">কাস্টমার সামারি</span>
            <div class="kpi-icon-wrap"><i class="fa-solid fa-users"></i></div>
          </div>
          <div class="kpi-value"><span id="kpi-total-clients">0</span> <span style="font-size: 1rem; font-weight: normal; color: var(--text-muted);">জন</span></div>
          <div class="kpi-meta" style="flex-wrap: wrap; gap: 8px;">
            <span style="color: #34d399;"><i class="fa-solid fa-circle-check"></i> পরিশোধ: <strong id="kpi-paid-count">0</strong></span>
            <span style="color: #fbbf24;"><i class="fa-solid fa-circle-half-stroke"></i> আংশিক: <strong id="kpi-partial-count">0</strong></span>
            <span style="color: #f87171;"><i class="fa-solid fa-circle-xmark"></i> বাকি: <strong id="kpi-due-count">0</strong></span>
          </div>
        </div>

      </div>
    </section>

    <!-- ==========================================================================
         3. SEARCH, FILTERS & ACTION TOOLBAR
         ========================================================================== -->
    <section class="toolbar-section">
      <div class="toolbar-card">

        <!-- Top Row: Search & Export/Backup Buttons -->
        <div class="toolbar-top-row">
          <div class="search-input-wrap">
            <i class="fa-solid fa-magnifying-glass"></i>
            <input type="text" id="table-search-input" class="search-input" placeholder="কাস্টমারের নাম, ইনভয়েস নং বা ফোন দিয়ে খুঁজুন..." oninput="filterRecords()">
          </div>

          <div class="toolbar-actions">
            <button class="btn btn-outline btn-sm" onclick="exportToExcelCSV()" title="এক্সেল ফাইল ডাউনলোড করুন">
              <i class="fa-solid fa-file-excel" style="color: #10b981;"></i>
              <span>Excel (CSV)</span>
            </button>

            <button class="btn btn-outline btn-sm" onclick="printTableReport()" title="লেজার প্রিন্ট বা পিডিএফ করুন">
              <i class="fa-solid fa-print"></i>
              <span>প্রিন্ট / PDF</span>
            </button>

            <button class="btn btn-outline btn-sm" onclick="openBackupModal()" title="ডাটাবেজ ব্যাকআপ ও রিস্টোর">
              <i class="fa-solid fa-database" style="color: #38bdf8;"></i>
              <span>ডাটাবেজ ব্যাকআপ</span>
            </button>

            <button class="btn btn-success btn-sm" onclick="openAddModal()">
              <i class="fa-solid fa-plus"></i>
              <span>নতুন কাস্টমার</span>
            </button>
          </div>
        </div>

        <!-- Bottom Row: Filter Pills (All, Due, Partial, Paid, Payment Methods) -->
        <div class="filter-tabs-row">
          <div class="status-filter-pills">
            <button class="filter-pill active" onclick="setStatusFilter('all', this)">
              <i class="fa-solid fa-list-ul"></i> সব কাস্টমার <span class="count-tag" id="filter-count-all">0</span>
            </button>
            <button class="filter-pill due-pill" onclick="setStatusFilter('due', this)">
              <i class="fa-solid fa-circle-xmark" style="color: #f87171;"></i> বাকি আছে <span class="count-tag" id="filter-count-due">0</span>
            </button>
            <button class="filter-pill partial-pill" onclick="setStatusFilter('partial', this)">
              <i class="fa-solid fa-circle-half-stroke" style="color: #fbbf24;"></i> আংশিক পরিশোধ <span class="count-tag" id="filter-count-partial">0</span>
            </button>
            <button class="filter-pill paid-pill" onclick="setStatusFilter('paid', this)">
              <i class="fa-solid fa-circle-check" style="color: #34d399;"></i> সম্পূর্ণ পরিশোধ <span class="count-tag" id="filter-count-paid">0</span>
            </button>
          </div>

          <div class="filter-dropdowns">
            <select id="method-filter-select" class="select-input" onchange="filterRecords()">
              <option value="all">💳 সকল পেমেন্ট মাধ্যম</option>
              <option value="bKash">bKash</option>
              <option value="Rocket">Rocket</option>
              <option value="Cash">Cash (নগদ)</option>
              <option value="Nagad">Nagad</option>
              <option value="none">পেমেন্ট মেথড ছাড়া</option>
            </select>

            <select id="sort-select" class="select-input" onchange="filterRecords()">
              <option value="date-desc">তারিখ: নতুন আগে</option>
              <option value="date-asc">তারিখ: পুরাতন আগে</option>
              <option value="due-desc">বাকি টাকা: বেশি আগে</option>
              <option value="bill-desc">মোট বিল: বেশি আগে</option>
              <option value="name-asc">নাম: A - Z</option>
            </select>
          </div>
        </div>

      </div>
    </section>

    <!-- ==========================================================================
         4. THE MASTER LEDGER TABLE (Identical to User's Excel Sheet)
         ========================================================================== -->
    <section class="table-section">
      <div class="table-card">
        <div class="table-header-meta">
          <div class="table-title">
            <i class="fa-solid fa-table-list" style="color: var(--blue-glow);"></i>
            <span>কাস্টমার রসিদ ও বাকি খাতা (Client Receipts & Receivables)</span>
          </div>
          <div class="table-sub-hint">
            <i class="fa-solid fa-shield-halved" style="color: #10b981;"></i>
            <span>অটো-সেভ সক্রিয়: ওয়েবসাইট বন্ধ করলেও ডাটা সংরক্ষিত থাকবে</span>
          </div>
        </div>

        <div class="table-responsive">
          <table class="ledger-table" id="main-ledger-table">
            <thead>
              <tr>
                <th style="width: 40px;" class="text-center">#</th>
                <th style="min-width: 105px;">তারিখ (Date)</th>
                <th style="min-width: 160px;">কাস্টমারের নাম (Client Name)</th>
                <th style="min-width: 100px;">অর্ডার / ইনভয়েস নং</th>
                <th class="text-right" style="min-width: 110px;">মোট বিল (BDT)</th>
                <th class="text-right" style="min-width: 110px;">জমা দিয়েছে (Received)</th>
                <th class="text-right" style="min-width: 120px;">বাকি আছে (Due)</th>
                <th style="min-width: 110px;">পেমেন্ট মেথড</th>
                <th style="min-width: 110px;">পরিশোধের তারিখ</th>
                <th class="text-center" style="min-width: 90px;">স্ট্যাটাস</th>
                <th style="min-width: 140px;">নোটস</th>
                <th class="text-right" style="min-width: 140px;">অ্যাকশন</th>
              </tr>
            </thead>
            <tbody id="ledger-table-body">
              <!-- Rendered via JavaScript -->
            </tbody>
          </table>
        </div>

        <div id="table-empty-placeholder" class="empty-state" style="display: none;">
          <i class="fa-solid fa-folder-open"></i>
          <h3>কোনো রেকর্ড পাওয়া যায় নি</h3>
          <p>আপনার সার্চ বা ফিল্টারের সাথে মিলে এমন কোনো কাস্টমার তথ্য নেই।</p>
        </div>

      </div>
    </section>

  </main>

  <!-- ==========================================================================
       MODAL 1: ADD / EDIT CUSTOMER RECORD
       ========================================================================== -->
  <div class="modal-overlay" id="record-modal">
    <div class="modal-box">
      <div class="modal-header">
        <h3 class="modal-title" id="record-modal-title">
          <i class="fa-solid fa-user-pen" style="color: var(--blue-glow);"></i>
          <span>কাস্টমার হিসাব যোগ / পরিবর্তন</span>
        </h3>
        <button class="modal-close-btn" onclick="closeRecordModal()">&times;</button>
      </div>

      <div class="modal-body">
        <form id="record-form" onsubmit="handleRecordFormSubmit(event)">
          <input type="hidden" id="form-record-id">

          <div class="form-grid">

            <!-- Client Name -->
            <div class="form-group full-width">
              <label class="form-label">কাস্টমারের নাম (Client Name) <span class="req">*</span></label>
              <input type="text" id="form-client-name" class="form-control" placeholder="যেমন: Mehedy Vai, Jagadeesh, Aziz..." required>
            </div>

            <!-- Phone Number -->
            <div class="form-group">
              <label class="form-label">মোবাইল / WhatsApp নং</label>
              <input type="tel" id="form-phone" class="form-control" placeholder="যেমন: 018XXXXXXXX">
            </div>

            <!-- Order / Invoice No -->
            <div class="form-group">
              <label class="form-label">ইনভয়েস / অর্ডার নং</label>
              <input type="text" id="form-invoice-no" class="form-control" placeholder="যেমন: INV-027">
            </div>

            <!-- Date -->
            <div class="form-group">
              <label class="form-label">তারিখ (Date) <span class="req">*</span></label>
              <input type="date" id="form-date" class="form-control" required>
            </div>

            <!-- Payment Method -->
            <div class="form-group">
              <label class="form-label">পেমেন্ট মেথড</label>
              <select id="form-payment-method" class="form-control">
                <option value="">-- নির্বাচন করুন --</option>
                <option value="bKash">bKash (01834093932)</option>
                <option value="Rocket">Rocket (018927170930)</option>
                <option value="Cash">Cash (নগদ)</option>
                <option value="Nagad">Nagad</option>
                <option value="Bank">Bank Transfer</option>
              </select>
            </div>

            <!-- Total Bill -->
            <div class="form-group">
              <label class="form-label">মোট বিল (Total Bill BDT) <span class="req">*</span></label>
              <input type="number" step="any" min="0" id="form-total-bill" class="form-control" placeholder="0" oninput="calculateModalDue()" required>
            </div>

            <!-- Amount Received -->
            <div class="form-group">
              <label class="form-label">জমা দেওয়া টাকা (Received BDT)</label>
              <input type="number" step="any" min="0" id="form-amount-received" class="form-control" placeholder="0" oninput="calculateModalDue()">
            </div>

            <!-- Auto Calculation Callout -->
            <div class="calculation-callout">
              <div class="calc-item">
                <span class="calc-label">মোট বিল</span>
                <span class="calc-value" id="calc-preview-bill">৳ 0</span>
              </div>
              <div class="calc-item">
                <span class="calc-label">জমা হয়েছে</span>
                <span class="calc-value" id="calc-preview-received" style="color: #34d399;">৳ 0</span>
              </div>
              <div class="calc-item">
                <span class="calc-label">বাকি থাকবে (Due)</span>
                <span class="calc-value due-highlight" id="calc-preview-due">৳ 0</span>
              </div>
            </div>

            <!-- Expected Payment Date -->
            <div class="form-group">
              <label class="form-label">বাকি পরিশোধের সম্ভাব্য তারিখ</label>
              <input type="date" id="form-expected-date" class="form-control">
            </div>

            <!-- Notes -->
            <div class="form-group full-width">
              <label class="form-label">নোটস / বিস্তারিত বিবরণ</label>
              <textarea id="form-notes" class="form-control" rows="2" placeholder="অর্ডারের বিবরণ, ট্রানজেকশন আইডি বা অন্য যেকোনো মন্তব্য..."></textarea>
            </div>

          </div>

          <div class="modal-footer">
            <button type="button" class="btn btn-outline" onclick="closeRecordModal()">বাতিল</button>
            <button type="submit" class="btn btn-success" id="record-save-btn">
              <i class="fa-solid fa-floppy-disk"></i>
              <span>ডাটাবেজে সেভ করুন</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       MODAL 2: QUICK PAY (টাকা জমা নেওয়ার পপআপ)
       ========================================================================== -->
  <div class="modal-overlay" id="quick-pay-modal">
    <div class="modal-box" style="max-width: 440px;">
      <div class="modal-header">
        <h3 class="modal-title">
          <i class="fa-solid fa-hand-holding-dollar" style="color: #34d399;"></i>
          <span>টাকা জমা নিন (Add Payment)</span>
        </h3>
        <button class="modal-close-btn" onclick="closeQuickPayModal()">&times;</button>
      </div>

      <div class="modal-body">
        <input type="hidden" id="qp-record-id">

        <div class="quick-pay-card">
          <div class="qp-row">
            <span>কাস্টমার:</span>
            <strong id="qp-client-name">-</strong>
          </div>
          <div class="qp-row">
            <span>মোট বিল:</span>
            <strong id="qp-total-bill">৳ 0</strong>
          </div>
          <div class="qp-row">
            <span>আগে জমা ছিল:</span>
            <strong id="qp-amount-received" style="color: #34d399;">৳ 0</strong>
          </div>
          <div class="qp-row" style="border-top: 1px dashed rgba(255,255,255,0.1); padding-top: 6px; margin-top: 4px;">
            <span>বর্তমান বাকি:</span>
            <strong id="qp-current-due" style="color: #f87171; font-size: 1.05rem;">৳ 0</strong>
          </div>
        </div>

        <form id="quick-pay-form" onsubmit="handleQuickPaySubmit(event)">
          <div class="form-group" style="margin-bottom: 14px;">
            <label class="form-label">এখন কত টাকা জমা দিলেন? (BDT) <span class="req">*</span></label>
            <input type="number" step="any" min="1" id="qp-payment-amount" class="form-control" placeholder="যেমন: 500" required style="font-size: 1.1rem; font-weight: 700; color: #34d399;">
          </div>

          <div class="form-group" style="margin-bottom: 14px;">
            <label class="form-label">পেমেন্ট মেথড</label>
            <select id="qp-payment-method" class="form-control">
              <option value="bKash">bKash (01834093932)</option>
              <option value="Rocket">Rocket (018927170930)</option>
              <option value="Cash">Cash (নগদ)</option>
              <option value="Nagad">Nagad</option>
              <option value="Bank">Bank Transfer</option>
            </select>
          </div>

          <div class="form-group" style="margin-bottom: 14px;">
            <label class="form-label">নোট (TrxID / তারিখ)</label>
            <input type="text" id="qp-notes" class="form-control" placeholder="যেমন: TrxID: 9X82...">
          </div>

          <div class="modal-footer" style="padding: 12px 0 0 0; background: transparent;">
            <button type="button" class="btn btn-outline" onclick="closeQuickPayModal()">বাতিল</button>
            <button type="submit" class="btn btn-success">
              <i class="fa-solid fa-check"></i>
              <span>জমা সম্পন্ন করুন</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       MODAL 3: MONEY RECEIPT & INVOICE PRINT VIEW
       ========================================================================== -->
  <div class="modal-overlay" id="receipt-modal">
    <div class="modal-box" style="max-width: 480px; background: #ffffff;">
      <div class="modal-header" style="background: #ffffff; border-bottom: 1px solid #e2e8f0;">
        <h3 class="modal-title" style="color: #0f172a;">
          <i class="fa-solid fa-receipt" style="color: #2563eb;"></i>
          <span>কাস্টমার মানি রসিদ (Receipt)</span>
        </h3>
        <button class="modal-close-btn" style="color: #64748b;" onclick="closeReceiptModal()">&times;</button>
      </div>

      <div class="modal-body" id="printable-receipt-content" style="padding: 20px;">
        <div class="receipt-container">
          <div class="receipt-header">
            <h2>OFFSIDE EXPORTS</h2>
            <div style="font-size: 0.72rem; color: #64748b; font-weight: 600;">ESTD 2026 • WEAR CONFIDENCE</div>
            <div class="receipt-contacts">
              <div><strong>bKash:</strong> 01834093932 | <strong>Rocket:</strong> 018927170930</div>
              <div><strong>WhatsApp:</strong> 01892717093 | Facebook: Offside Exports</div>
            </div>
          </div>

          <table class="receipt-table">
            <tr>
              <td><strong>রসিদ / অর্ডার নং:</strong></td>
              <td class="text-right" id="rcpt-inv-no">-</td>
            </tr>
            <tr>
              <td><strong>তারিখ:</strong></td>
              <td class="text-right" id="rcpt-date">-</td>
            </tr>
            <tr>
              <td><strong>কাস্টমার নাম:</strong></td>
              <td class="text-right" id="rcpt-client-name">-</td>
            </tr>
            <tr>
              <td><strong>মোট বিল:</strong></td>
              <td class="text-right" style="font-weight: 700;" id="rcpt-bill">৳ 0</td>
            </tr>
            <tr>
              <td><strong>পরিশোধ / জমা:</strong></td>
              <td class="text-right" style="font-weight: 700; color: #16a34a;" id="rcpt-received">৳ 0</td>
            </tr>
            <tr class="receipt-total-row">
              <td style="padding-top: 10px;"><strong>অবশিষ্ট বাকি (Due):</strong></td>
              <td class="text-right" style="padding-top: 10px; color: #dc2626; font-size: 1.1rem;" id="rcpt-due">৳ 0</td>
            </tr>
            <tr>
              <td><strong>পেমেন্ট মাধ্যম:</strong></td>
              <td class="text-right" id="rcpt-method">-</td>
            </tr>
            <tr>
              <td><strong>মন্তব্য / নোট:</strong></td>
              <td class="text-right" id="rcpt-notes">-</td>
            </tr>
          </table>

          <div style="text-align: center; font-size: 0.75rem; color: #64748b; margin-top: 18px; border-top: 1px solid #f1f5f9; padding-top: 12px;">
            আমাদের সাথে থাকার জন্য ধন্যবাদ! ❤️ Offside Exports
          </div>
        </div>
      </div>

      <div class="modal-footer" style="background: #ffffff; border-top: 1px solid #e2e8f0;">
        <button class="btn btn-outline btn-sm" style="color: #0f172a; border-color: #cbd5e1;" onclick="closeReceiptModal()">বন্ধ করুন</button>
        <button class="btn btn-primary btn-sm" onclick="printReceiptDirectly()">
          <i class="fa-solid fa-print"></i>
          <span>প্রিন্ট রসিদ</span>
        </button>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       MODAL 4: DATABASE BACKUP & RESTORE
       ========================================================================== -->
  <div class="modal-overlay" id="backup-modal">
    <div class="modal-box" style="max-width: 520px;">
      <div class="modal-header">
        <h3 class="modal-title">
          <i class="fa-solid fa-database" style="color: var(--blue-glow);"></i>
          <span>ডাটাবেজ ব্যাকআপ ও সুরক্ষা</span>
        </h3>
        <button class="modal-close-btn" onclick="closeBackupModal()">&times;</button>
      </div>

      <div class="modal-body">
        <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 16px;">
          আপনার ডাটাবেজের সকল কাস্টমার, অর্ডার এবং পেমেন্টের হিসাব ১০০% সুরক্ষিত রাখতে যেকোনো সময় ব্যাকআপ ডাউনলোড করে রাখতে পারেন।
        </p>

        <div style="display: flex; flex-direction: column; gap: 12px;">
          <div style="background: var(--bg-card); padding: 14px; border-radius: var(--radius-md); border: 1px solid var(--border-subtle); display: flex; align-items: center; justify-content: space-between;">
            <div>
              <strong style="font-size: 0.9rem; color: #fff;">JSON ব্যাকআপ ফাইল</strong>
              <div style="font-size: 0.76rem; color: var(--text-muted);">সম্পূর্ণ ডাটাবেজ এক ক্লিকে ডাউনলোড করুন</div>
            </div>
            <button class="btn btn-primary btn-sm" onclick="downloadJSONBackup()">
              <i class="fa-solid fa-download"></i> ব্যাকআপ নিন
            </button>
          </div>

          <div style="background: var(--bg-card); padding: 14px; border-radius: var(--radius-md); border: 1px solid var(--border-subtle); display: flex; align-items: center; justify-content: space-between;">
            <div>
              <strong style="font-size: 0.9rem; color: #fff;">Excel / CSV স্প্রেডশীট</strong>
              <div style="font-size: 0.76rem; color: var(--text-muted);">Google Sheets বা Excel এ খোলার উপযোগী ফাইল</div>
            </div>
            <button class="btn btn-success btn-sm" onclick="exportToExcelCSV()">
              <i class="fa-solid fa-file-excel"></i> এক্সেল ফাইল
            </button>
          </div>

          <div style="background: var(--bg-card); padding: 14px; border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
            <strong style="font-size: 0.9rem; color: #fff; display: block; margin-bottom: 6px;">ব্যাকআপ থেকে ডাটা ফিরিয়ে আনুন (Restore)</strong>
            <div style="font-size: 0.76rem; color: var(--text-muted); margin-bottom: 10px;">পূর্বে সেভ করা JSON ব্যাকআপ ফাইল নির্বাচন করুন:</div>
            <input type="file" id="restore-file-input" accept=".json" class="form-control" style="padding: 6px;" onchange="handleRestoreFile(event)">
          </div>

          <div style="background: rgba(239, 68, 68, 0.08); padding: 14px; border-radius: var(--radius-md); border: 1px solid rgba(239, 68, 68, 0.25); display: flex; align-items: center; justify-content: space-between;">
            <div>
              <strong style="font-size: 0.9rem; color: #f87171;">রিসেট অপশন (মূল ২৬টি হিসাব)</strong>
              <div style="font-size: 0.76rem; color: var(--text-muted);">প্রয়োজনে আগের আদি ২৬টি কাস্টমারের হিসাব ফিরিয়ে আনুন</div>
            </div>
            <button class="btn btn-outline btn-sm" style="border-color: rgba(239, 68, 68, 0.4); color: #f87171;" onclick="resetToDefaultSeedData()">
              <i class="fa-solid fa-rotate-left"></i> মূল ডেটায় রিসেট
            </button>
          </div>
        </div>

      </div>

      <div class="modal-footer">
        <button class="btn btn-outline" onclick="closeBackupModal()">বন্ধ করুন</button>
      </div>
    </div>
  </div>

  <!-- Toast Container -->
  <div class="toast-container" id="toast-box"></div>

  <!-- ==========================================================================
       JAVASCRIPT APPLICATION ENGINE
       Supports SQLite Server API + IndexedDB / LocalStorage Automatic Fallback
       ========================================================================== -->
  <script>
    // Initial 26 records seeded directly from the user's Google Sheet screenshot
    const DEFAULT_SEED_DATA = [
      { id: 1, date: "2026-10-01", client_name: "Ifty", invoice_no: "INV-001", total_bill: 450, amount_received: 0, receivable_due: 450, payment_method: "", expected_date: "", notes: "", phone: "", status: "due" },
      { id: 2, date: "2026-10-02", client_name: "Mehedy Vai (Tanjir)", invoice_no: "INV-002", total_bill: 2250, amount_received: 0, receivable_due: 2250, payment_method: "", expected_date: "", notes: "", phone: "", status: "due" },
      { id: 3, date: "2026-10-20", client_name: "Jagadeesh (Tanjir)", invoice_no: "INV-003", total_bill: 1200, amount_received: 1200, receivable_due: 0, payment_method: "bKash", expected_date: "", notes: "Fully paid via bKash", phone: "", status: "paid" },
      { id: 4, date: "2026-10-20", client_name: "Fahad", invoice_no: "INV-004", total_bill: 2700, amount_received: 0, receivable_due: 2700, payment_method: "", expected_date: "", notes: "", phone: "", status: "due" },
      { id: 5, date: "2026-10-20", client_name: "Nafis", invoice_no: "INV-005", total_bill: 4100, amount_received: 0, receivable_due: 4100, payment_method: "", expected_date: "", notes: "", phone: "", status: "due" },
      { id: 6, date: "2026-10-20", client_name: "Tonmoy", invoice_no: "INV-006", total_bill: 3500, amount_received: 0, receivable_due: 3500, payment_method: "", expected_date: "", notes: "", phone: "", status: "due" },
      { id: 7, date: "2026-10-20", client_name: "Hasib", invoice_no: "INV-007", total_bill: 250, amount_received: 250, receivable_due: 0, payment_method: "bKash", expected_date: "", notes: "Fully paid via bKash", phone: "", status: "paid" },
      { id: 8, date: "2026-10-20", client_name: "Shawon", invoice_no: "INV-008", total_bill: 10670, amount_received: 0, receivable_due: 10670, payment_method: "", expected_date: "", notes: "Big order", phone: "", status: "due" },
      { id: 9, date: "2026-10-20", client_name: "Sani", invoice_no: "INV-009", total_bill: 1100, amount_received: 0, receivable_due: 1100, payment_method: "", expected_date: "", notes: "", phone: "", status: "due" },
      { id: 10, date: "2026-10-20", client_name: "Tanjir", invoice_no: "INV-010", total_bill: 4200, amount_received: 0, receivable_due: 4200, payment_method: "", expected_date: "", notes: "", phone: "", status: "due" },
      { id: 11, date: "2026-10-20", client_name: "Mithil", invoice_no: "INV-011", total_bill: 2750, amount_received: 0, receivable_due: 2750, payment_method: "", expected_date: "", notes: "", phone: "", status: "due" },
      { id: 12, date: "2026-10-20", client_name: "Aziz", invoice_no: "INV-012", total_bill: 600, amount_received: 500, receivable_due: 100, payment_method: "Cash", expected_date: "2026-10-25", notes: "500 Cash given, 100 due", phone: "", status: "partial" },
      { id: 13, date: "2026-10-20", client_name: "Rasel", invoice_no: "INV-013", total_bill: 1900, amount_received: 0, receivable_due: 1900, payment_method: "", expected_date: "", notes: "", phone: "", status: "due" },
      { id: 14, date: "2026-10-20", client_name: "Ratul", invoice_no: "INV-014", total_bill: 1120, amount_received: 0, receivable_due: 1120, payment_method: "", expected_date: "", notes: "", phone: "", status: "due" },
      { id: 15, date: "2026-10-20", client_name: "Aziz", invoice_no: "INV-015", total_bill: 4000, amount_received: 0, receivable_due: 4000, payment_method: "", expected_date: "", notes: "", phone: "", status: "due" },
      { id: 16, date: "2026-10-20", client_name: "Shazzad", invoice_no: "INV-016", total_bill: 400, amount_received: 400, receivable_due: 0, payment_method: "bKash", expected_date: "", notes: "Fully paid via bKash", phone: "", status: "paid" },
      { id: 17, date: "2026-10-20", client_name: "Mati", invoice_no: "INV-017", total_bill: 700, amount_received: 0, receivable_due: 700, payment_method: "", expected_date: "", notes: "", phone: "", status: "due" },
      { id: 18, date: "2026-10-20", client_name: "Hasib", invoice_no: "INV-018", total_bill: 500, amount_received: 0, receivable_due: 500, payment_method: "", expected_date: "", notes: "", phone: "", status: "due" },
      { id: 19, date: "2026-10-20", client_name: "Mithil", invoice_no: "INV-019", total_bill: 300, amount_received: 0, receivable_due: 300, payment_method: "", expected_date: "", notes: "", phone: "", status: "due" },
      { id: 20, date: "2026-10-20", client_name: "Shawon", invoice_no: "INV-020", total_bill: 600, amount_received: 0, receivable_due: 600, payment_method: "", expected_date: "", notes: "", phone: "", status: "due" },
      { id: 21, date: "2026-10-20", client_name: "Tanjir", invoice_no: "INV-021", total_bill: 500, amount_received: 0, receivable_due: 500, payment_method: "", expected_date: "", notes: "", phone: "", status: "due" },
      { id: 22, date: "2026-10-20", client_name: "Shakilur", invoice_no: "INV-022", total_bill: 3800, amount_received: 1000, receivable_due: 2800, payment_method: "bKash", expected_date: "2026-10-28", notes: "1000 paid via bKash, 2800 due", phone: "", status: "partial" },
      { id: 23, date: "2026-10-20", client_name: "Tajbiul", invoice_no: "INV-023", total_bill: 700, amount_received: 0, receivable_due: 700, payment_method: "", expected_date: "", notes: "", phone: "", status: "due" },
      { id: 24, date: "2026-10-20", client_name: "Ratul", invoice_no: "INV-024", total_bill: 750, amount_received: 0, receivable_due: 750, payment_method: "", expected_date: "", notes: "", phone: "", status: "due" },
      { id: 25, date: "2026-10-22", client_name: "Onik (online)", invoice_no: "INV-025", total_bill: 2240, amount_received: 140, receivable_due: 2100, payment_method: "bKash", expected_date: "2026-10-30", notes: "Online order, 140 delivery fee advance", phone: "", status: "partial" },
      { id: 26, date: "2026-10-22", client_name: "Rabbi (online)", invoice_no: "INV-026", total_bill: 2540, amount_received: 140, receivable_due: 2400, payment_method: "bKash", expected_date: "2026-10-30", notes: "Online order, 140 delivery fee advance", phone: "", status: "partial" }
    ];

    // State Variables
    let allRecords = [];
    let currentFilterStatus = 'all';
    let isServerApiAvailable = false;
    let dbInstance = null;

    // Toast helper
    function showToast(message, type = 'success') {
      const box = document.getElementById('toast-box');
      const toast = document.createElement('div');
      toast.className = `toast ${type}`;
      toast.innerHTML = `
        <i class="fa-solid fa-circle-check" style="color: #10b981;"></i>
        <span>${message}</span>
      `;
      box.appendChild(toast);
      setTimeout(() => {
        toast.style.transition = 'all 0.3s ease';
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(10px)';
        setTimeout(() => toast.remove(), 300);
      }, 3500);
    }

    // Number formatting helper
    function formatBDT(num) {
      if (isNaN(num)) return '0';
      return Number(num).toLocaleString('en-IN', { maximumFractionDigits: 2 });
    }

    // Status calculator
    function computeStatus(bill, received) {
      bill = parseFloat(bill || 0);
      received = parseFloat(received || 0);
      if (bill <= 0) return 'paid';
      if (received >= bill) return 'paid';
      if (received > 0) return 'partial';
      return 'due';
    }

    // ==========================================================================
    // PERSISTENCE ENGINE: DUAL-STORAGE (LOCALSTORAGE FIRST + INDEXEDDB BACKUP)
    // 100% Guaranteed Permanent Storage - Survives tab exit, reload & restart
    // ==========================================================================
    const STORAGE_KEY = 'offside_exports_records_v3';
    const INIT_FLAG_KEY = 'offside_exports_init_v3';
    let dbInstance = null;

    // Bulletproof synchronous storage to LocalStorage
    function saveToLocalStorage(records) {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(records));
        localStorage.setItem(INIT_FLAG_KEY, 'true');
      } catch (err) {
        console.error('LocalStorage write failed:', err);
      }
    }

    function loadFromLocalStorage() {
      try {
        const isInit = localStorage.getItem(INIT_FLAG_KEY);
        if (isInit === 'true') {
          const raw = localStorage.getItem(STORAGE_KEY);
          if (raw !== null) {
            return JSON.parse(raw);
          }
        }
      } catch (err) {
        console.error('LocalStorage read failed:', err);
      }
      return null;
    }

    // Master persist function: updates allRecords, saves synchronously, syncs to IndexedDB & Server
    function persistRecords(updatedRecords) {
      allRecords = updatedRecords;
      saveToLocalStorage(allRecords);
      syncToIndexedDB(allRecords);
      refreshUI();
    }

    // IndexedDB backup sync
    function initIndexedDB() {
      return new Promise((resolve) => {
        try {
          const req = indexedDB.open('OffsideExportsDB_v3', 1);
          req.onupgradeneeded = (e) => {
            const db = e.target.result;
            if (!db.objectStoreNames.contains('records')) {
              db.createObjectStore('records', { keyPath: 'id' });
            }
          };
          req.onsuccess = (e) => {
            dbInstance = e.target.result;
            resolve(dbInstance);
          };
          req.onerror = () => {
            resolve(null);
          };
        } catch (e) {
          resolve(null);
        }
      });
    }

    function syncToIndexedDB(records) {
      if (!dbInstance) return;
      try {
        const tx = dbInstance.transaction('records', 'readwrite');
        const store = tx.objectStore('records');
        store.clear();
        records.forEach(r => store.put(r));
      } catch (err) {
        console.warn('IndexedDB sync warning:', err);
      }
    }

    function loadFromIndexedDB() {
      return new Promise((resolve) => {
        if (!dbInstance) return resolve(null);
        try {
          const tx = dbInstance.transaction('records', 'readonly');
          const store = tx.objectStore('records');
          const req = store.getAll();
          req.onsuccess = () => {
            resolve(req.result || null);
          };
          req.onerror = () => {
            resolve(null);
          };
        } catch (e) {
          resolve(null);
        }
      });
    }

    async function initStorageEngine() {
      // 1. Check if LocalStorage already has user data
      const localData = loadFromLocalStorage();
      if (localData !== null && Array.isArray(localData)) {
        allRecords = localData;
        console.log('[Storage] Loaded', allRecords.length, 'records from permanent storage');
        updateDBStatusPill(false);
        refreshUI();
        await initIndexedDB();
        syncToIndexedDB(allRecords);
        checkServerConnection();
        return;
      }

      // 2. Initialize IndexedDB to check backup
      await initIndexedDB();
      const idbData = await loadFromIndexedDB();
      if (idbData !== null && Array.isArray(idbData) && idbData.length > 0) {
        allRecords = idbData;
        saveToLocalStorage(allRecords);
        updateDBStatusPill(false);
        refreshUI();
        checkServerConnection();
        return;
      }

      // 3. Check if SQLite Python server is reachable
      try {
        const res = await fetch('/api/records', { method: 'GET', headers: { 'Accept': 'application/json' } });
        if (res.ok) {
          const data = await res.json();
          if (data && data.records && data.records.length > 0) {
            isServerApiAvailable = true;
            allRecords = data.records;
            updateDBStatusPill(true);
            saveToLocalStorage(allRecords);
            syncToIndexedDB(allRecords);
            refreshUI();
            return;
          }
        }
      } catch (e) {
        // static GitHub Pages or server off
      }

      // 4. Brand new first-time setup: Seed original 26 records and mark as initialized!
      allRecords = JSON.parse(JSON.stringify(DEFAULT_SEED_DATA));
      saveToLocalStorage(allRecords);
      syncToIndexedDB(allRecords);
      updateDBStatusPill(false);
      refreshUI();
    }

    async function checkServerConnection() {
      try {
        const res = await fetch('/api/records', { method: 'GET', headers: { 'Accept': 'application/json' } });
        if (res.ok) {
          isServerApiAvailable = true;
          updateDBStatusPill(true);
        }
      } catch (e) {}
    }

    function updateDBStatusPill(isServer) {
      const pill = document.getElementById('db-status-indicator');
      const text = document.getElementById('db-status-text');
      if (!pill || !text) return;
      if (isServer) {
        pill.style.borderColor = 'rgba(16, 185, 129, 0.4)';
        pill.style.background = 'rgba(16, 185, 129, 0.12)';
        text.innerHTML = '<strong style="color: #34d399;">SQLite Server Connected</strong> (ডাটা পার্মানেন্ট সংরক্ষিত)';
      } else {
        pill.style.borderColor = 'rgba(16, 185, 129, 0.4)';
        pill.style.background = 'rgba(16, 185, 129, 0.12)';
        text.innerHTML = '<strong style="color: #34d399;">Permanent Storage Active</strong> (ডাটা আজীবনের জন্য সুরক্ষিত)';
      }
    }

    // ==========================================================================
    // CRUD OPERATIONS (SAVE, EDIT, DELETE, PAY)
    // ==========================================================================
    async function saveRecord(recordData) {
      const isEdit = Boolean(recordData.id);
      let updated = [...allRecords];

      if (isEdit) {
        const targetId = Number(recordData.id);
        const idx = updated.findIndex(r => Number(r.id) === targetId);
        if (idx !== -1) {
          updated[idx] = { ...updated[idx], ...recordData, id: targetId };
        }
      } else {
        const maxId = updated.reduce((max, r) => Math.max(max, Number(r.id || 0)), 0);
        recordData.id = maxId + 1;
        updated.unshift(recordData);
      }

      // Save permanently immediately!
      persistRecords(updated);

      // Background sync to server if running
      if (isServerApiAvailable) {
        const url = isEdit ? `/api/records/${recordData.id}` : '/api/records';
        const method = isEdit ? 'PUT' : 'POST';
        fetch(url, {
          method: method,
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(recordData)
        }).catch(err => console.warn('Server sync error:', err));
      }

      showToast(isEdit ? '✅ হিসাব সফলভাবে আপডেট হয়েছে!' : '✅ নতুন কাস্টমার স্থায়ীভাবে সেভ হয়েছে!');
      return true;
    }

    async function deleteRecord(id) {
      const targetId = Number(id);
      const rec = allRecords.find(r => Number(r.id) === targetId);
      const name = rec ? rec.client_name : 'এই কাস্টমারের';
      if (!confirm(`আপনি কি নিশ্চিত যে "${name}"-এর হিসাবটি মুছে ফেলতে চান?`)) {
        return;
      }

      // Filter out using strict Number comparison
      const updated = allRecords.filter(r => Number(r.id) !== targetId);

      // Permanently save to localStorage & IndexedDB right now!
      persistRecords(updated);

      // Background delete from server if running
      if (isServerApiAvailable) {
        fetch(`/api/records/${targetId}`, { method: 'DELETE' }).catch(err => console.warn('Server delete error:', err));
      }

      showToast('🗑️ হিসাবটি স্থায়ীভাবে মুছে ফেলা হয়েছে');
    }

    async function addIncrementalPayment(id, amount, method, notes) {
      const targetId = Number(id);
      let updated = [...allRecords];
      const rec = updated.find(r => Number(r.id) === targetId);
      if (!rec) return false;

      const newReceived = parseFloat(rec.amount_received || 0) + parseFloat(amount || 0);
      const newDue = parseFloat(rec.total_bill || 0) - newReceived;
      rec.amount_received = newReceived;
      rec.receivable_due = newDue;
      rec.payment_method = method || rec.payment_method;
      rec.status = computeStatus(rec.total_bill, newReceived);
      if (notes) {
        rec.notes = rec.notes ? `${rec.notes} | [৳${amount} via ${method}: ${notes}]` : `[৳${amount} via ${method}: ${notes}]`;
      }

      // Save permanently immediately!
      persistRecords(updated);

      if (isServerApiAvailable) {
        fetch(`/api/records/${targetId}/pay`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            amount: amount,
            payment_method: method,
            notes: notes,
            date: new Date().toISOString().split('T')[0]
          })
        }).catch(err => console.warn('Server pay error:', err));
      }

      showToast(`✅ ৳${amount} টাকা জমা যোগ হয়েছে ও স্থায়ীভাবে সেভ হয়েছে!`);
      return true;
    }

    function resetToDefaultSeedData() {
      if (confirm('আপনি কি নিশ্চিত যে আপনার বর্তমান সব পরিবর্তন মুছে ফেলে মূল ২৬টি হিসাব ফিরিয়ে আনতে চান?')) {
        persistRecords(JSON.parse(JSON.stringify(DEFAULT_SEED_DATA)));
        closeBackupModal();
        showToast('🔄 মূল ২৬টি হিসাব সফলভাবে ফিরিয়ে আনা হয়েছে');
      }
    }

    // ==========================================================================
    // UI RENDERING & CALCULATIONS
    // ==========================================================================
    function refreshUI() {
      updateKPICards();
      renderTable();
    }

    function updateKPICards() {
      let totalBill = 0;
      let totalReceived = 0;
      let totalDue = 0;
      let paidCount = 0;
      let partialCount = 0;
      let dueCount = 0;

      allRecords.forEach(r => {
        const bill = parseFloat(r.total_bill || 0);
        const rcvd = parseFloat(r.amount_received || 0);
        const due = parseFloat(r.receivable_due || (bill - rcvd));

        totalBill += bill;
        totalReceived += rcvd;
        totalDue += due;

        const status = r.status || computeStatus(bill, rcvd);
        if (status === 'paid') paidCount++;
        else if (status === 'partial') partialCount++;
        else dueCount++;
      });

      document.getElementById('kpi-total-bill').textContent = formatBDT(totalBill);
      document.getElementById('kpi-total-received').textContent = formatBDT(totalReceived);
      document.getElementById('kpi-total-due').textContent = formatBDT(totalDue);
      document.getElementById('kpi-total-clients').textContent = allRecords.length;

      document.getElementById('kpi-paid-count').textContent = paidCount;
      document.getElementById('kpi-partial-count').textContent = partialCount;
      document.getElementById('kpi-due-count').textContent = dueCount;

      const rate = totalBill > 0 ? ((totalReceived / totalBill) * 100).toFixed(1) : 0;
      document.getElementById('kpi-collection-rate').textContent = `${rate}%`;
      document.getElementById('kpi-progress-bar').style.width = `${Math.min(rate, 100)}%`;

      // Filter tabs counts
      document.getElementById('filter-count-all').textContent = allRecords.length;
      document.getElementById('filter-count-due').textContent = dueCount;
      document.getElementById('filter-count-partial').textContent = partialCount;
      document.getElementById('filter-count-paid').textContent = paidCount;
    }

    function renderTable() {
      const tbody = document.getElementById('ledger-table-body');
      const emptyState = document.getElementById('table-empty-placeholder');
      tbody.innerHTML = '';

      const query = (document.getElementById('table-search-input').value || '').trim().toLowerCase();
      const methodFilter = document.getElementById('method-filter-select').value;
      const sortVal = document.getElementById('sort-select').value;

      // Filter
      let filtered = allRecords.filter(r => {
        const bill = parseFloat(r.total_bill || 0);
        const rcvd = parseFloat(r.amount_received || 0);
        const status = r.status || computeStatus(bill, rcvd);

        // Status filter
        if (currentFilterStatus !== 'all' && status !== currentFilterStatus) {
          return false;
        }

        // Method filter
        if (methodFilter !== 'all') {
          if (methodFilter === 'none') {
            if (r.payment_method) return false;
          } else {
            if (!r.payment_method || !r.payment_method.toLowerCase().includes(methodFilter.toLowerCase())) {
              return false;
            }
          }
        }

        // Query search
        if (query) {
          const matchName = (r.client_name || '').toLowerCase().includes(query);
          const matchInv = (r.invoice_no || '').toLowerCase().includes(query);
          const matchPhone = (r.phone || '').toLowerCase().includes(query);
          const matchNotes = (r.notes || '').toLowerCase().includes(query);
          if (!matchName && !matchInv && !matchPhone && !matchNotes) return false;
        }

        return true;
      });

      // Sort
      filtered.sort((a, b) => {
        if (sortVal === 'date-desc') return new Date(b.date || 0) - new Date(a.date || 0);
        if (sortVal === 'date-asc') return new Date(a.date || 0) - new Date(b.date || 0);
        if (sortVal === 'due-desc') return parseFloat(b.receivable_due || 0) - parseFloat(a.receivable_due || 0);
        if (sortVal === 'bill-desc') return parseFloat(b.total_bill || 0) - parseFloat(a.total_bill || 0);
        if (sortVal === 'name-asc') return (a.client_name || '').localeCompare(b.client_name || '');
        return 0;
      });

      if (filtered.length === 0) {
        emptyState.style.display = 'block';
        return;
      }
      emptyState.style.display = 'none';

      filtered.forEach((r, idx) => {
        const bill = parseFloat(r.total_bill || 0);
        const rcvd = parseFloat(r.amount_received || 0);
        const due = parseFloat(r.receivable_due != null ? r.receivable_due : (bill - rcvd));
        const status = r.status || computeStatus(bill, rcvd);

        let statusBadge = '';
        if (status === 'paid') {
          statusBadge = '<span class="badge-status paid"><i class="fa-solid fa-circle-check"></i> পরিশোধ</span>';
        } else if (status === 'partial') {
          statusBadge = '<span class="badge-status partial"><i class="fa-solid fa-circle-half-stroke"></i> আংশিক</span>';
        } else {
          statusBadge = '<span class="badge-status due"><i class="fa-solid fa-circle-xmark"></i> বাকি</span>';
        }

        // Payment method badge
        let methodBadge = '<span style="color: var(--text-dim);">-</span>';
        if (r.payment_method) {
          const mLower = r.payment_method.toLowerCase();
          if (mLower.includes('bkash')) {
            methodBadge = `<span class="pay-badge bkash"><i class="fa-solid fa-mobile-screen"></i> ${r.payment_method}</span>`;
          } else if (mLower.includes('rocket')) {
            methodBadge = `<span class="pay-badge rocket"><i class="fa-solid fa-bolt"></i> ${r.payment_method}</span>`;
          } else if (mLower.includes('cash')) {
            methodBadge = `<span class="pay-badge cash"><i class="fa-solid fa-money-bill-wave"></i> ${r.payment_method}</span>`;
          } else {
            methodBadge = `<span class="pay-badge nagad">${r.payment_method}</span>`;
          }
        }

        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td class="text-center" style="color: var(--text-dim); font-size: 0.78rem;">${idx + 1}</td>
          <td style="white-space: nowrap; font-size: 0.82rem; color: #cbd5e1;">
            <i class="fa-regular fa-calendar" style="color: var(--text-dim); margin-right: 4px;"></i>
            ${formatDateDisplay(r.date)}
          </td>
          <td>
            <div class="client-cell">
              <span>${escapeHtml(r.client_name)}</span>
              ${r.phone ? `<span class="client-sub"><i class="fa-solid fa-phone" style="font-size: 0.65rem;"></i> ${r.phone}</span>` : ''}
            </div>
          </td>
          <td style="font-family: 'Outfit', sans-serif; font-size: 0.82rem; color: #94a3b8;">
            ${r.invoice_no ? escapeHtml(r.invoice_no) : '-'}
          </td>
          <td class="text-right amount-val">৳ ${formatBDT(bill)}</td>
          <td class="text-right amount-val" style="color: #34d399;">${rcvd > 0 ? `৳ ${formatBDT(rcvd)}` : '-'}</td>
          <td class="text-right">
            <span class="amount-due-highlight ${due <= 0 ? 'cleared' : ''}">
              ${due <= 0 ? '৳ 0 (পরিশোধ)' : `৳ ${formatBDT(due)}`}
            </span>
          </td>
          <td>${methodBadge}</td>
          <td style="font-size: 0.8rem; color: #94a3b8;">${r.expected_date ? formatDateDisplay(r.expected_date) : '-'}</td>
          <td class="text-center">${statusBadge}</td>
          <td style="max-width: 160px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; font-size: 0.8rem; color: #94a3b8;" title="${escapeHtml(r.notes || '')}">
            ${r.notes ? escapeHtml(r.notes) : '-'}
          </td>
          <td>
            <div class="row-actions">
              <button class="action-btn pay" onclick="openQuickPayModal(${r.id})" title="টাকা জমা নিন">
                <i class="fa-solid fa-plus"></i>
              </button>
              <button class="action-btn" onclick="openReceiptModal(${r.id})" title="মানি রসিদ দেখুন ও প্রিন্ট করুন">
                <i class="fa-solid fa-receipt"></i>
              </button>
              <button class="action-btn wa" onclick="sendWhatsAppReminder(${r.id})" title="কাস্টমারকে WhatsApp এ হিসাব পাঠান">
                <i class="fa-brands fa-whatsapp"></i>
              </button>
              <button class="action-btn" onclick="openEditModal(${r.id})" title="সম্পাদনা / এডিট করুন">
                <i class="fa-solid fa-pen-to-square"></i>
              </button>
              <button class="action-btn del" onclick="deleteRecord(${r.id})" title="ডিলিট করুন">
                <i class="fa-solid fa-trash-can"></i>
              </button>
            </div>
          </td>
        `;
        tbody.appendChild(tr);
      });
    }

    function formatDateDisplay(dStr) {
      if (!dStr) return '-';
      try {
        const parts = dStr.split('-');
        if (parts.length === 3) {
          const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
          const monthIdx = parseInt(parts[1], 10) - 1;
          return `${parts[2]}-${months[monthIdx] || parts[1]}-${parts[0]}`;
        }
      } catch (e) {}
      return dStr;
    }

    function escapeHtml(text) {
      if (!text) return '';
      return String(text).replace(/[&<>"']/g, function(m) {
        return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' }[m];
      });
    }

    function setStatusFilter(status, btnElement) {
      currentFilterStatus = status;
      document.querySelectorAll('.filter-pill').forEach(b => b.classList.remove('active'));
      if (btnElement) btnElement.classList.add('active');
      renderTable();
    }

    function filterRecords() {
      renderTable();
    }

    // ==========================================================================
    // MODAL HANDLERS
    // ==========================================================================
    function openAddModal() {
      document.getElementById('record-form').reset();
      document.getElementById('form-record-id').value = '';
      document.getElementById('record-modal-title').innerHTML = `
        <i class="fa-solid fa-user-plus" style="color: var(--blue-glow);"></i>
        <span>নতুন কাস্টমারের হিসাব যোগ করুন</span>
      `;
      // Auto-set today date
      const today = new Date().toISOString().split('T')[0];
      document.getElementById('form-date').value = today;

      // Auto generate next invoice no
      const count = allRecords.length + 1;
      const invNum = `INV-${String(count).padStart(3, '0')}`;
      document.getElementById('form-invoice-no').value = invNum;

      calculateModalDue();
      document.getElementById('record-modal').classList.add('active');
    }

    function openEditModal(id) {
      const rec = allRecords.find(r => r.id === id);
      if (!rec) return;

      document.getElementById('form-record-id').value = rec.id;
      document.getElementById('form-client-name').value = rec.client_name || '';
      document.getElementById('form-phone').value = rec.phone || '';
      document.getElementById('form-invoice-no').value = rec.invoice_no || '';
      document.getElementById('form-date').value = rec.date || '';
      document.getElementById('form-total-bill').value = rec.total_bill || 0;
      document.getElementById('form-amount-received').value = rec.amount_received || 0;
      document.getElementById('form-payment-method').value = rec.payment_method || '';
      document.getElementById('form-expected-date').value = rec.expected_date || '';
      document.getElementById('form-notes').value = rec.notes || '';

      document.getElementById('record-modal-title').innerHTML = `
        <i class="fa-solid fa-user-pen" style="color: var(--blue-glow);"></i>
        <span>কাস্টমার হিসাব সম্পাদনা (Edit Record)</span>
      `;

      calculateModalDue();
      document.getElementById('record-modal').classList.add('active');
    }

    function closeRecordModal() {
      document.getElementById('record-modal').classList.remove('active');
    }

    function calculateModalDue() {
      const bill = parseFloat(document.getElementById('form-total-bill').value || 0);
      const rcvd = parseFloat(document.getElementById('form-amount-received').value || 0);
      const due = bill - rcvd;

      document.getElementById('calc-preview-bill').textContent = `৳ ${formatBDT(bill)}`;
      document.getElementById('calc-preview-received').textContent = `৳ ${formatBDT(rcvd)}`;
      document.getElementById('calc-preview-due').textContent = `৳ ${formatBDT(due)}`;

      const dueElem = document.getElementById('calc-preview-due');
      if (due <= 0) {
        dueElem.style.color = '#34d399';
      } else {
        dueElem.style.color = '#f87171';
      }
    }

    async function handleRecordFormSubmit(e) {
      e.preventDefault();
      const idVal = document.getElementById('form-record-id').value;
      const clientName = document.getElementById('form-client-name').value.trim();
      const phone = document.getElementById('form-phone').value.trim();
      const invoiceNo = document.getElementById('form-invoice-no').value.trim();
      const date = document.getElementById('form-date').value;
      const totalBill = parseFloat(document.getElementById('form-total-bill').value || 0);
      const amountReceived = parseFloat(document.getElementById('form-amount-received').value || 0);
      const paymentMethod = document.getElementById('form-payment-method').value;
      const expectedDate = document.getElementById('form-expected-date').value;
      const notes = document.getElementById('form-notes').value.trim();
      const receivableDue = totalBill - amountReceived;
      const status = computeStatus(totalBill, amountReceived);

      const recordObj = {
        date,
        client_name: clientName,
        invoice_no: invoiceNo,
        total_bill: totalBill,
        amount_received: amountReceived,
        receivable_due: receivableDue,
        payment_method: paymentMethod,
        expected_date: expectedDate,
        notes,
        phone,
        status
      };

      if (idVal) {
        recordObj.id = parseInt(idVal, 10);
      }

      await saveRecord(recordObj);
      closeRecordModal();
    }

    // Quick Pay Modal
    function openQuickPayModal(id) {
      const rec = allRecords.find(r => r.id === id);
      if (!rec) return;

      const bill = parseFloat(rec.total_bill || 0);
      const rcvd = parseFloat(rec.amount_received || 0);
      const due = parseFloat(rec.receivable_due != null ? rec.receivable_due : (bill - rcvd));

      document.getElementById('qp-record-id').value = rec.id;
      document.getElementById('qp-client-name').textContent = rec.client_name;
      document.getElementById('qp-total-bill').textContent = `৳ ${formatBDT(bill)}`;
      document.getElementById('qp-amount-received').textContent = `৳ ${formatBDT(rcvd)}`;
      document.getElementById('qp-current-due').textContent = `৳ ${formatBDT(due)}`;

      document.getElementById('qp-payment-amount').value = due > 0 ? due : '';
      document.getElementById('qp-payment-method').value = rec.payment_method || 'bKash';
      document.getElementById('qp-notes').value = '';

      document.getElementById('quick-pay-modal').classList.add('active');
    }

    function closeQuickPayModal() {
      document.getElementById('quick-pay-modal').classList.remove('active');
    }

    async function handleQuickPaySubmit(e) {
      e.preventDefault();
      const id = parseInt(document.getElementById('qp-record-id').value, 10);
      const amount = parseFloat(document.getElementById('qp-payment-amount').value || 0);
      const method = document.getElementById('qp-payment-method').value;
      const notes = document.getElementById('qp-notes').value.trim();

      if (amount <= 0) {
        alert('টাকার পরিমাণ অবশ্যই ০-এর বেশি হতে হবে');
        return;
      }

      await addIncrementalPayment(id, amount, method, notes);
      closeQuickPayModal();
    }

    // Receipt Modal
    function openReceiptModal(id) {
      const rec = allRecords.find(r => r.id === id);
      if (!rec) return;

      const bill = parseFloat(rec.total_bill || 0);
      const rcvd = parseFloat(rec.amount_received || 0);
      const due = parseFloat(rec.receivable_due != null ? rec.receivable_due : (bill - rcvd));

      document.getElementById('rcpt-inv-no').textContent = rec.invoice_no || `INV-${rec.id}`;
      document.getElementById('rcpt-date').textContent = formatDateDisplay(rec.date);
      document.getElementById('rcpt-client-name').textContent = rec.client_name;
      document.getElementById('rcpt-bill').textContent = `৳ ${formatBDT(bill)}`;
      document.getElementById('rcpt-received').textContent = `৳ ${formatBDT(rcvd)}`;
      document.getElementById('rcpt-due').textContent = due <= 0 ? '৳ 0 (পরিশোধ)' : `৳ ${formatBDT(due)}`;
      document.getElementById('rcpt-method').textContent = rec.payment_method || 'Cash / bKash';
      document.getElementById('rcpt-notes').textContent = rec.notes || 'কোনো নোট নেই';

      document.getElementById('receipt-modal').classList.add('active');
    }

    function closeReceiptModal() {
      document.getElementById('receipt-modal').classList.remove('active');
    }

    function printReceiptDirectly() {
      const content = document.getElementById('printable-receipt-content').innerHTML;
      const win = window.open('', '_blank', 'width=600,height=700');
      win.document.write(`
        <!DOCTYPE html>
        <html>
        <head>
          <title>Money Receipt - Offside Exports</title>
          <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; padding: 30px; }
            .receipt-container { max-width: 450px; margin: 0 auto; border: 1px solid #ddd; padding: 24px; border-radius: 8px; }
            .receipt-header { text-align: center; border-bottom: 2px dashed #999; padding-bottom: 14px; margin-bottom: 14px; }
            .receipt-header h2 { margin: 0; font-size: 24px; }
            .receipt-table { width: 100%; border-collapse: collapse; margin: 15px 0; }
            .receipt-table td { padding: 8px 0; border-bottom: 1px solid #eee; }
            .receipt-total-row { font-weight: bold; border-top: 2px solid #000; }
            .text-right { text-align: right; }
          </style>
        </head>
        <body>
          ${content}
          <script>
            window.onload = function() { window.print(); window.close(); }
          <\/script>
        </body>
        </html>
      `);
      win.document.close();
    }

    // WhatsApp Message Generator
    function sendWhatsAppReminder(id) {
      const rec = allRecords.find(r => r.id === id);
      if (!rec) return;

      const bill = parseFloat(rec.total_bill || 0);
      const rcvd = parseFloat(rec.amount_received || 0);
      const due = parseFloat(rec.receivable_due != null ? rec.receivable_due : (bill - rcvd));

      const message = `আসসালামু আলাইকুম ${rec.client_name} ভাই/ম্যাম,
Offside Exports থেকে বলছি। আপনার অর্ডারের হিসাব বিবরণী:

• মোট বিল: ৳ ${formatBDT(bill)}
• জমা দেওয়া হয়েছে: ৳ ${formatBDT(rcvd)}
• অবশিষ্ট বাকি (Due): ৳ ${formatBDT(due)}

বাকি টাকা পরিশোধের জন্য আমাদের নিম্নোক্ত একাউন্টে পাঠাতে পারেন:
📱 bKash: 01834093932
🚀 Rocket: 018927170930

পেমেন্ট করার পর অনুগ্রহ করে Last 4 Digits অথবা TrxID জানাবেন।
ধন্যবাদ!
— Offside Exports (ESTD 2026)`;

      const encodedMsg = encodeURIComponent(message);
      const phoneDigits = (rec.phone || '').replace(/[^0-9]/g, '');
      const waUrl = phoneDigits ? `https://wa.me/88${phoneDigits}?text=${encodedMsg}` : `https://wa.me/?text=${encodedMsg}`;
      window.open(waUrl, '_blank');
    }

    // Number copy helper
    function copyPaymentNumber(number, name) {
      navigator.clipboard.writeText(number).then(() => {
        showToast(`📋 ${name} নাম্বার: ${number} কপি করা হয়েছে!`);
      }).catch(() => {
        prompt(`কপি করতে চাপুন:`, number);
      });
    }

    // Export to Excel / CSV
    function exportToExcelCSV() {
      if (allRecords.length === 0) {
        alert('ডাউনলোড করার মতো কোনো রেকর্ড নেই');
        return;
      }

      let csv = '\uFEFFDate,Client Name,Invoice / Order No,Total Bill (BDT),Amount Received (BDT),Receivable / Due (BDT),Payment Method,Expected Payment Date,Status,Notes,Phone\r\n';

      allRecords.forEach(r => {
        const bill = parseFloat(r.total_bill || 0);
        const rcvd = parseFloat(r.amount_received || 0);
        const due = parseFloat(r.receivable_due != null ? r.receivable_due : (bill - rcvd));
        const status = r.status || computeStatus(bill, rcvd);

        csv += `"${r.date || ''}","${r.client_name || ''}","${r.invoice_no || ''}",${bill},${rcvd},${due},"${r.payment_method || ''}","${r.expected_date || ''}","${status}","${(r.notes || '').replace(/"/g, '""')}","${r.phone || ''}"\r\n`;
      });

      const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `Offside_Exports_Accounts_${new Date().toISOString().split('T')[0]}.csv`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      showToast('📥 Excel (CSV) ফাইল ডাউনলোড সম্পন্ন হয়েছে');
    }

    // Print Table Report
    function printTableReport() {
      window.print();
    }

    // Backup & Restore
    function openBackupModal() {
      document.getElementById('backup-modal').classList.add('active');
    }

    function closeBackupModal() {
      document.getElementById('backup-modal').classList.remove('active');
    }

    function downloadJSONBackup() {
      const data = {
        app: "Offside Exports Ledger",
        version: "1.0",
        timestamp: new Date().toISOString(),
        total_records: allRecords.length,
        records: allRecords
      };
      const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `Offside_Database_Backup_${new Date().toISOString().split('T')[0]}.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      showToast('💾 ডাটাবেজ ব্যাকআপ (JSON) ডাউনলোড হয়েছে');
    }

    function handleRestoreFile(e) {
      const file = e.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = async function(evt) {
        try {
          const parsed = JSON.parse(evt.target.result);
          const recordsToRestore = parsed.records || parsed;
          if (Array.isArray(recordsToRestore) && recordsToRestore.length > 0) {
            if (confirm(`আপনি কি ব্যাকআপ ফাইল থেকে ${recordsToRestore.length} টি রেকর্ড ডাটাবেজে ফিরিয়ে আনতে চান?`)) {
              if (isServerApiAvailable) {
                try {
                  const res = await fetch('/api/restore', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ records: recordsToRestore })
                  });
                  const result = await res.json();
                  if (result.success) {
                    allRecords = recordsToRestore;
                    saveLocalCache(allRecords);
                    refreshUI();
                    closeBackupModal();
                    showToast('✅ ডাটাবেজে ব্যাকআপ সফলভাবে রিস্টোর হয়েছে!');
                    return;
                  }
                } catch (err) {
                  console.warn('API restore failed, applying locally', err);
                }
              }

              persistRecords(recordsToRestore);
              closeBackupModal();
              showToast('✅ ব্যাকআপ ডাটা সফলভাবে ফিরিয়ে আনা হয়েছে!');
            }
          } else {
            alert('সঠিক ব্যাকআপ ফাইল নয় বা কোনো রেকর্ড পাওয়া যায়নি।');
          }
        } catch (err) {
          alert('ফাইল রিড করতে ব্যর্থ হয়েছে: ' + err.message);
        }
      };
      reader.readAsText(file);
    }

    // Initialize application on window load
    window.addEventListener('DOMContentLoaded', () => {
      initStorageEngine();
    });
  </script>
</body>
</html>
'''

# Replace placeholders
final_html = HTML_CONTENT.replace('__LOGO_DATA__', logo_base64)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Successfully generated index.html. Total size: {os.path.getsize('index.html')} bytes.")
