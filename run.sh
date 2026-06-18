#!/bin/bash

# Default URL if not provided
URL="${1:-https://redhat.com/workshop/2eex7p}"

# Logo is the 2nd argument (can be blank)
LOGO_PATH="$2"

# Default output name if not provided
OUTPUT_FILE="${3:-gen_qr_code.png}"

# Create the virtual environment named .qr
python3 -m venv .qr

# Activate the virtual environment
source .qr/bin/activate

# Upgrade pip and install the requirements
pip3 install --upgrade pip
pip3 install -r requirements.txt

# Run the QR generator script dynamically based on whether a logo was provided
if [ -z "$LOGO_PATH" ]; then
    # No logo provided, drop the -l flag entirely
    python3 qr-generator.py -u "$URL" -o "$OUTPUT_FILE"
else
    # Logo provided, pass it along
    python3 qr-generator.py -u "$URL" -l "$LOGO_PATH" -o "$OUTPUT_FILE"
fi