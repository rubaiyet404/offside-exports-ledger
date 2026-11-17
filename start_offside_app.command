#!/bin/bash
cd "$(dirname "$0")"
echo "Starting OFFSIDE EXPORTS Accounting & Ledger Management..."
python3 server.py &
SERVER_PID=$!
sleep 1
open "http://localhost:5000"
echo "Server is running (PID: $SERVER_PID). Press Ctrl+C to stop."
wait $SERVER_PID
