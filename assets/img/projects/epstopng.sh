#!/bin/bash

# Configuration
INPUT_FILE="cavitation_BEM.eps"
OUTPUT_FILE="tucunare_cavitation_BEM.png"
DPI=600

# Use 'gs' for Linux/WSL
if gs -dSAFER -dBATCH -dNOPAUSE -dNOPROMPT \
    -sDEVICE=png16m \
    -r$DPI \
    -sOutputFile="$OUTPUT_FILE" \
    "$INPUT_FILE"; then
    echo "Conversion complete: $OUTPUT_FILE at $DPI DPI."
else
    echo "Error: Conversion failed."
    exit 1
fi
