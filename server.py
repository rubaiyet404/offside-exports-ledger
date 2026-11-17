#!/usr/bin/env python3
"""
OFFSIDE EXPORTS - Customer Payment & Ledger Management Server
Built for persistent SQLite data storage and local web access.
"""

import os
import sys
import json
import sqlite3
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from datetime import datetime

DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'offside_accounts.db')
PORT = 5000

# Seed records matching user's Excel spreadsheet screenshot (Export_Business_Accounts.xlsx)
SEED_RECORDS = [
    {"date": "2026-10-01", "client_name": "Ifty", "invoice_no": "INV-001", "total_bill": 450, "amount_received": 0, "receivable_due": 450, "payment_method": "", "expected_date": "", "notes": "", "phone": ""},
    {"date": "2026-10-02", "client_name": "Mehedy Vai (Tanjir)", "invoice_no": "INV-002", "total_bill": 2250, "amount_received": 0, "receivable_due": 2250, "payment_method": "", "expected_date": "", "notes": "", "phone": ""},
    {"date": "2026-10-20", "client_name": "Jagadeesh (Tanjir)", "invoice_no": "INV-003", "total_bill": 1200, "amount_received": 1200, "receivable_due": 0, "payment_method": "bKash", "expected_date": "", "notes": "Fully paid via bKash", "phone": ""},
    {"date": "2026-10-20", "client_name": "Fahad", "invoice_no": "INV-004", "total_bill": 2700, "amount_received": 0, "receivable_due": 2700, "payment_method": "", "expected_date": "", "notes": "", "phone": ""},
    {"date": "2026-10-20", "client_name": "Nafis", "invoice_no": "INV-005", "total_bill": 4100, "amount_received": 0, "receivable_due": 4100, "payment_method": "", "expected_date": "", "notes": "", "phone": ""},
    {"date": "2026-10-20", "client_name": "Tonmoy", "invoice_no": "INV-006", "total_bill": 3500, "amount_received": 0, "receivable_due": 3500, "payment_method": "", "expected_date": "", "notes": "", "phone": ""},
    {"date": "2026-10-20", "client_name": "Hasib", "invoice_no": "INV-007", "total_bill": 250, "amount_received": 250, "receivable_due": 0, "payment_method": "bKash", "expected_date": "", "notes": "Fully paid via bKash", "phone": ""},
    {"date": "2026-10-20", "client_name": "Shawon", "invoice_no": "INV-008", "total_bill": 10670, "amount_received": 0, "receivable_due": 10670, "payment_method": "", "expected_date": "", "notes": "Order placed", "phone": ""},
    {"date": "2026-10-20", "client_name": "Sani", "invoice_no": "INV-009", "total_bill": 1100, "amount_received": 0, "receivable_due": 1100, "payment_method": "", "expected_date": "", "notes": "", "phone": ""},
    {"date": "2026-10-20", "client_name": "Tanjir", "invoice_no": "INV-010", "total_bill": 4200, "amount_received": 0, "receivable_due": 4200, "payment_method": "", "expected_date": "", "notes": "", "phone": ""},
    {"date": "2026-10-20", "client_name": "Mithil", "invoice_no": "INV-011", "total_bill": 2750, "amount_received": 0, "receivable_due": 2750, "payment_method": "", "expected_date": "", "notes": "", "phone": ""},
    {"date": "2026-10-20", "client_name": "Aziz", "invoice_no": "INV-012", "total_bill": 600, "amount_received": 500, "receivable_due": 100, "payment_method": "Cash", "expected_date": "2026-10-25", "notes": "Cash 500 given, 100 due", "phone": ""},
    {"date": "2026-10-20", "client_name": "Rasel", "invoice_no": "INV-013", "total_bill": 1900, "amount_received": 0, "receivable_due": 1900, "payment_method": "", "expected_date": "", "notes": "", "phone": ""},
    {"date": "2026-10-20", "client_name": "Ratul", "invoice_no": "INV-014", "total_bill": 1120, "amount_received": 0, "receivable_due": 1120, "payment_method": "", "expected_date": "", "notes": "", "phone": ""},
    {"date": "2026-10-20", "client_name": "Aziz", "invoice_no": "INV-015", "total_bill": 4000, "amount_received": 0, "receivable_due": 4000, "payment_method": "", "expected_date": "", "notes": "", "phone": ""},
    {"date": "2026-10-20", "client_name": "Shazzad", "invoice_no": "INV-016", "total_bill": 400, "amount_received": 400, "receivable_due": 0, "payment_method": "bKash", "expected_date": "", "notes": "Fully paid via bKash", "phone": ""},
    {"date": "2026-10-20", "client_name": "Mati", "invoice_no": "INV-017", "total_bill": 700, "amount_received": 0, "receivable_due": 700, "payment_method": "", "expected_date": "", "notes": "", "phone": ""},
    {"date": "2026-10-20", "client_name": "Hasib", "invoice_no": "INV-018", "total_bill": 500, "amount_received": 0, "receivable_due": 500, "payment_method": "", "expected_date": "", "notes": "", "phone": ""},
    {"date": "2026-10-20", "client_name": "Mithil", "invoice_no": "INV-019", "total_bill": 300, "amount_received": 0, "receivable_due": 300, "payment_method": "", "expected_date": "", "notes": "", "phone": ""},
    {"date": "2026-10-20", "client_name": "Shawon", "invoice_no": "INV-020", "total_bill": 600, "amount_received": 0, "receivable_due": 600, "payment_method": "", "expected_date": "", "notes": "", "phone": ""},
    {"date": "2026-10-20", "client_name": "Tanjir", "invoice_no": "INV-021", "total_bill": 500, "amount_received": 0, "receivable_due": 500, "payment_method": "", "expected_date": "", "notes": "", "phone": ""},
    {"date": "2026-10-20", "client_name": "Shakilur", "invoice_no": "INV-022", "total_bill": 3800, "amount_received": 1000, "receivable_due": 2800, "payment_method": "bKash", "expected_date": "2026-10-28", "notes": "1000 paid via bKash, 2800 due", "phone": ""},
    {"date": "2026-10-20", "client_name": "Tajbiul", "invoice_no": "INV-023", "total_bill": 700, "amount_received": 0, "receivable_due": 700, "payment_method": "", "expected_date": "", "notes": "", "phone": ""},
    {"date": "2026-10-20", "client_name": "Ratul", "invoice_no": "INV-024", "total_bill": 750, "amount_received": 0, "receivable_due": 750, "payment_method": "", "expected_date": "", "notes": "", "phone": ""},
    {"date": "2026-10-22", "client_name": "Onik (online)", "invoice_no": "INV-025", "total_bill": 2240, "amount_received": 140, "receivable_due": 2100, "payment_method": "bKash", "expected_date": "2026-10-30", "notes": "Online order, 140 delivery charge advance", "phone": ""},
    {"date": "2026-10-22", "client_name": "Rabbi (online)", "invoice_no": "INV-026", "total_bill": 2540, "amount_received": 140, "receivable_due": 2400, "payment_method": "bKash", "expected_date": "2026-10-30", "notes": "Online order, 140 delivery charge advance", "phone": ""}
]

def calculate_status(bill, received):
    bill = float(bill or 0)
    received = float(received or 0)
    if bill <= 0:
        return 'paid' if received >= 0 else 'due'
    if received >= bill:
        return 'paid'
    elif received > 0:
        return 'partial'
    else:
        return 'due'

def get_db():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            client_name TEXT NOT NULL,
            invoice_no TEXT,
            total_bill REAL NOT NULL DEFAULT 0,
            amount_received REAL NOT NULL DEFAULT 0,
            receivable_due REAL NOT NULL DEFAULT 0,
            payment_method TEXT DEFAULT '',
            expected_date TEXT DEFAULT '',
            notes TEXT DEFAULT '',
            phone TEXT DEFAULT '',
            status TEXT DEFAULT 'due',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS payments_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            record_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            payment_method TEXT DEFAULT '',
            date TEXT NOT NULL,
            notes TEXT DEFAULT '',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (record_id) REFERENCES records (id) ON DELETE CASCADE
        )
    ''')

    # Seed if records is empty
    c.execute('SELECT COUNT(*) FROM records')
    count = c.fetchone()[0]
    if count == 0:
        print("[DATABASE] Initializing database with 26 records from Excel spreadsheet...")
        for r in SEED_RECORDS:
            bill = float(r["total_bill"])
            rcvd = float(r["amount_received"])
            due = bill - rcvd
            status = calculate_status(bill, rcvd)
            c.execute('''
                INSERT INTO records (date, client_name, invoice_no, total_bill, amount_received, receivable_due, payment_method, expected_date, notes, phone, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (r["date"], r["client_name"], r["invoice_no"], bill, rcvd, due, r["payment_method"], r["expected_date"], r["notes"], r["phone"], status))
        conn.commit()
        print("[DATABASE] Seed complete! Total bill: 53,820 BDT | Received: 3,630 BDT | Due: 50,190 BDT")
    conn.close()

class RequestHandler(BaseHTTPRequestHandler):
    def _send_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    def _send_json(self, data, status=200):
        self.send_response(status)
        self._send_cors_headers()
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))

    def _read_body_json(self):
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            body = self.rfile.read(content_length).decode('utf-8')
            return json.loads(body)
        return {}

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == '/api/records':
            conn = get_db()
            c = conn.cursor()
            c.execute('SELECT * FROM records ORDER BY date DESC, id DESC')
            rows = [dict(r) for r in c.fetchall()]
            conn.close()
            self._send_json({"success": True, "records": rows})
            return

        elif path.startswith('/api/records/'):
            try:
                rec_id = int(path.split('/')[-1])
                conn = get_db()
                c = conn.cursor()
                c.execute('SELECT * FROM records WHERE id = ?', (rec_id,))
                row = c.fetchone()
                if row:
                    rec = dict(row)
                    c.execute('SELECT * FROM payments_log WHERE record_id = ? ORDER BY id DESC', (rec_id,))
                    rec['payments'] = [dict(p) for p in c.fetchall()]
                    conn.close()
                    self._send_json({"success": True, "record": rec})
                else:
                    conn.close()
                    self._send_json({"success": False, "error": "Record not found"}, 404)
            except Exception as e:
                self._send_json({"success": False, "error": str(e)}, 400)
            return

        elif path == '/api/stats':
            conn = get_db()
            c = conn.cursor()
            c.execute('SELECT SUM(total_bill), SUM(amount_received), SUM(receivable_due), COUNT(*) FROM records')
            row = c.fetchone()
            total_bill = row[0] or 0
            amount_received = row[1] or 0
            receivable_due = row[2] or 0
            total_count = row[3] or 0

            c.execute("SELECT COUNT(*) FROM records WHERE status = 'paid'")
            paid_count = c.fetchone()[0]

            c.execute("SELECT COUNT(*) FROM records WHERE status = 'partial'")
            partial_count = c.fetchone()[0]

            c.execute("SELECT COUNT(*) FROM records WHERE status = 'due'")
            due_count = c.fetchone()[0]

            conn.close()
            self._send_json({
                "success": True,
                "stats": {
                    "total_bill": round(total_bill, 2),
                    "amount_received": round(amount_received, 2),
                    "receivable_due": round(receivable_due, 2),
                    "total_count": total_count,
                    "paid_count": paid_count,
                    "partial_count": partial_count,
                    "due_count": due_count
                }
            })
            return

        elif path == '/api/export-csv':
            conn = get_db()
            c = conn.cursor()
            c.execute('SELECT * FROM records ORDER BY date ASC, id ASC')
            rows = c.fetchall()
            conn.close()

            # CSV format matching user's spreadsheet
            csv_lines = ['"Date","Client Name","Invoice / Order No","Total Bill (BDT)","Amount Received (BDT)","Receivable / Due (BDT)","Payment Method","Expected Payment Date","Status","Notes","Phone"']
            for r in rows:
                csv_lines.append(f'"{r["date"]}","{r["client_name"]}","{r["invoice_no"]}","{r["total_bill"]}","{r["amount_received"]}","{r["receivable_due"]}","{r["payment_method"]}","{r["expected_date"]}","{r["status"]}","{r["notes"]}","{r["phone"]}"')

            csv_content = "\r\n".join(csv_lines)
            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'text/csv; charset=utf-8')
            self.send_header('Content-Disposition', 'attachment; filename="Export_Business_Accounts.csv"')
            self.end_headers()
            self.wfile.write(csv_content.encode('utf-8'))
            return

        elif path == '/api/backup':
            conn = get_db()
            c = conn.cursor()
            c.execute('SELECT * FROM records')
            records = [dict(r) for r in c.fetchall()]
            c.execute('SELECT * FROM payments_log')
            payments = [dict(p) for p in c.fetchall()]
            conn.close()
            self._send_json({"version": "1.0", "timestamp": datetime.now().isoformat(), "records": records, "payments": payments})
            return

        # Serve static files
        self._serve_static(path)

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == '/api/records':
            data = self._read_body_json()
            client_name = data.get('client_name', '').strip()
            if not client_name:
                self._send_json({"success": False, "error": "Client Name is required"}, 400)
                return

            date = data.get('date') or datetime.now().strftime('%Y-%m-%d')
            invoice_no = data.get('invoice_no', '').strip()
            total_bill = float(data.get('total_bill', 0) or 0)
            amount_received = float(data.get('amount_received', 0) or 0)
            receivable_due = total_bill - amount_received
            payment_method = data.get('payment_method', '').strip()
            expected_date = data.get('expected_date', '').strip()
            notes = data.get('notes', '').strip()
            phone = data.get('phone', '').strip()
            status = calculate_status(total_bill, amount_received)

            conn = get_db()
            c = conn.cursor()
            c.execute('''
                INSERT INTO records (date, client_name, invoice_no, total_bill, amount_received, receivable_due, payment_method, expected_date, notes, phone, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (date, client_name, invoice_no, total_bill, amount_received, receivable_due, payment_method, expected_date, notes, phone, status))
            new_id = c.lastrowid

            if amount_received > 0:
                c.execute('''
                    INSERT INTO payments_log (record_id, amount, payment_method, date, notes)
                    VALUES (?, ?, ?, ?, ?)
                ''', (new_id, amount_received, payment_method, date, 'Initial payment'))

            conn.commit()
            c.execute('SELECT * FROM records WHERE id = ?', (new_id,))
            new_record = dict(c.fetchone())
            conn.close()

            self._send_json({"success": True, "message": "Record saved successfully to SQLite database", "record": new_record})
            return

        elif path.startswith('/api/records/') and path.endswith('/pay'):
            # Incremental payment
            try:
                rec_id = int(path.split('/')[-2])
                data = self._read_body_json()
                amount = float(data.get('amount', 0) or 0)
                method = data.get('payment_method', '').strip() or 'bKash'
                pay_date = data.get('date') or datetime.now().strftime('%Y-%m-%d')
                pay_notes = data.get('notes', '').strip()

                if amount <= 0:
                    self._send_json({"success": False, "error": "Payment amount must be greater than 0"}, 400)
                    return

                conn = get_db()
                c = conn.cursor()
                c.execute('SELECT * FROM records WHERE id = ?', (rec_id,))
                rec = c.fetchone()
                if not rec:
                    conn.close()
                    self._send_json({"success": False, "error": "Record not found"}, 404)
                    return

                new_received = float(rec['amount_received']) + amount
                new_due = float(rec['total_bill']) - new_received
                new_status = calculate_status(rec['total_bill'], new_received)
                updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Update record
                c.execute('''
                    UPDATE records
                    SET amount_received = ?, receivable_due = ?, payment_method = ?, status = ?, updated_at = ?
                    WHERE id = ?
                ''', (new_received, new_due, method, new_status, updated_at, rec_id))

                # Log payment
                c.execute('''
                    INSERT INTO payments_log (record_id, amount, payment_method, date, notes)
                    VALUES (?, ?, ?, ?, ?)
                ''', (rec_id, amount, method, pay_date, pay_notes))

                conn.commit()
                c.execute('SELECT * FROM records WHERE id = ?', (rec_id,))
                updated_record = dict(c.fetchone())
                conn.close()

                self._send_json({"success": True, "message": f"Payment of ৳{amount} recorded successfully!", "record": updated_record})
            except Exception as e:
                self._send_json({"success": False, "error": str(e)}, 400)
            return

        elif path == '/api/restore':
            try:
                data = self._read_body_json()
                records = data.get('records', [])
                if not records:
                    self._send_json({"success": False, "error": "No records in backup payload"}, 400)
                    return

                conn = get_db()
                c = conn.cursor()
                c.execute('DELETE FROM records')
                c.execute('DELETE FROM payments_log')

                for r in records:
                    bill = float(r.get('total_bill', 0) or 0)
                    rcvd = float(r.get('amount_received', 0) or 0)
                    due = float(r.get('receivable_due', bill - rcvd) or (bill - rcvd))
                    status = r.get('status') or calculate_status(bill, rcvd)
                    c.execute('''
                        INSERT INTO records (id, date, client_name, invoice_no, total_bill, amount_received, receivable_due, payment_method, expected_date, notes, phone, status)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (r.get('id'), r.get('date'), r.get('client_name'), r.get('invoice_no'), bill, rcvd, due, r.get('payment_method'), r.get('expected_date'), r.get('notes'), r.get('phone', ''), status))

                conn.commit()
                conn.close()
                self._send_json({"success": True, "message": f"Restored {len(records)} records successfully"})
            except Exception as e:
                self._send_json({"success": False, "error": str(e)}, 500)
            return

        self._send_json({"error": "Endpoint not found"}, 404)

    def do_PUT(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path.startswith('/api/records/'):
            try:
                rec_id = int(path.split('/')[-1])
                data = self._read_body_json()
                client_name = data.get('client_name', '').strip()
                if not client_name:
                    self._send_json({"success": False, "error": "Client Name is required"}, 400)
                    return

                date = data.get('date') or datetime.now().strftime('%Y-%m-%d')
                invoice_no = data.get('invoice_no', '').strip()
                total_bill = float(data.get('total_bill', 0) or 0)
                amount_received = float(data.get('amount_received', 0) or 0)
                receivable_due = total_bill - amount_received
                payment_method = data.get('payment_method', '').strip()
                expected_date = data.get('expected_date', '').strip()
                notes = data.get('notes', '').strip()
                phone = data.get('phone', '').strip()
                status = calculate_status(total_bill, amount_received)
                updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                conn = get_db()
                c = conn.cursor()
                c.execute('''
                    UPDATE records
                    SET date = ?, client_name = ?, invoice_no = ?, total_bill = ?, amount_received = ?, receivable_due = ?, payment_method = ?, expected_date = ?, notes = ?, phone = ?, status = ?, updated_at = ?
                    WHERE id = ?
                ''', (date, client_name, invoice_no, total_bill, amount_received, receivable_due, payment_method, expected_date, notes, phone, status, updated_at, rec_id))
                conn.commit()

                c.execute('SELECT * FROM records WHERE id = ?', (rec_id,))
                row = c.fetchone()
                conn.close()

                if row:
                    self._send_json({"success": True, "message": "Record updated in SQLite database", "record": dict(row)})
                else:
                    self._send_json({"success": False, "error": "Record not found"}, 404)
            except Exception as e:
                self._send_json({"success": False, "error": str(e)}, 400)
            return

        self._send_json({"error": "Endpoint not found"}, 404)

    def do_DELETE(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path.startswith('/api/records/'):
            try:
                rec_id = int(path.split('/')[-1])
                conn = get_db()
                c = conn.cursor()
                c.execute('DELETE FROM records WHERE id = ?', (rec_id,))
                c.execute('DELETE FROM payments_log WHERE record_id = ?', (rec_id,))
                conn.commit()
                conn.close()
                self._send_json({"success": True, "message": f"Record {rec_id} deleted from SQLite database"})
            except Exception as e:
                self._send_json({"success": False, "error": str(e)}, 400)
            return

        self._send_json({"error": "Endpoint not found"}, 404)

    def _serve_static(self, path):
        if path == '/' or path == '':
            path = '/index.html'

        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, path.lstrip('/'))

        if os.path.exists(file_path) and os.path.isfile(file_path):
            mime_type, _ = mimetypes.guess_type(file_path)
            mime_type = mime_type or 'application/octet-stream'

            try:
                with open(file_path, 'rb') as f:
                    content = f.read()

                self.send_response(200)
                self._send_cors_headers()
                self.send_header('Content-Type', mime_type)
                self.send_header('Content-Length', len(content))
                self.end_headers()
                self.wfile.write(content)
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(str(e).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

def run(port=PORT):
    init_db()
    server_address = ('', port)
    try:
        httpd = HTTPServer(server_address, RequestHandler)
    except OSError:
        # Try port 5001 if 5000 is occupied
        port = port + 1
        server_address = ('', port)
        httpd = HTTPServer(server_address, RequestHandler)

    print(f"\n========================================================")
    print(f"  OFFSIDE EXPORTS - Customer Ledger & Payment System   ")
    print(f"  Database File: {DB_FILE} (SQLite Persistent)        ")
    print(f"  Server URL: http://localhost:{port}                  ")
    print(f"  bKash: 01834093932 | Rocket: 018927170930            ")
    print(f"========================================================\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.server_close()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    run(port)
