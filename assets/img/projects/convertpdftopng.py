#!/usr/bin/env python3
"""
Convert PDF files to PNG images for web display.
Handles EPS-to-PDF converted files for Jekyll/web portfolios.

Requirements:
    pip install pdf2image Pillow

System dependency:
    - poppler-utils (Linux: apt install poppler-utils)
    - poppler (macOS: brew install poppler)
"""
import os
import sys
from pathlib import Path

try:
    from pdf2image import convert_from_path
except ImportError:
    print("Error: pdf2image not installed.")
    print("Install with: pip install pdf2image")
    sys.exit(1)


def convert_pdf_to_png(input_path, output_path=None, dpi=300):
    """
    Convert a PDF file to PNG.

    Args:
        input_path: Path to PDF file
        output_path: Path for output PNG (default: same name with .png)
        dpi: Resolution (default 300 for print quality, use 150 for web)

    Returns:
        Path to created PNG file
    """
    input_path = Path(input_path)

    if not input_path.exists():
        raise FileNotFoundError(f"PDF not found: {input_path}")

    if output_path is None:
        output_path = input_path.with_suffix('.png')
    else:
        output_path = Path(output_path)

    # Convert PDF to images
    images = convert_from_path(input_path, dpi=dpi)

    if len(images) == 1:
        # Single page - save directly
        images[0].save(output_path, 'PNG')
        print(f"✓ {input_path.name} → {output_path.name}")
    else:
        # Multiple pages - save with page numbers
        for i, image in enumerate(images):
            page_output = output_path.with_stem(f"{output_path.stem}_page{i+1}")
            image.save(page_output, 'PNG')
            print(f"✓ {input_path.name} (page {i+1}) → {page_output.name}")

    return output_path


def batch_convert(input_dir, output_dir=None, dpi=300, prefix=None):
    """
    Convert all PDF files in a directory to PNG.

    Args:
        input_dir: Directory containing PDF files
        output_dir: Output directory (default: same as input)
        dpi: Resolution for conversion
        prefix: Only convert files starting with this prefix (e.g., 'ici-')
    """
    input_dir = Path(input_dir)
    output_dir = Path(output_dir) if output_dir else input_dir

    if not input_dir.exists():
        raise FileNotFoundError(f"Directory not found: {input_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)

    # Find PDF files
    pdf_files = list(input_dir.glob('*.pdf'))

    if prefix:
        pdf_files = [f for f in pdf_files if f.name.startswith(prefix)]

    if not pdf_files:
        print(f"No PDF files found in {input_dir}")
        if prefix:
            print(f"  (with prefix '{prefix}')")
        return

    print(f"Converting {len(pdf_files)} PDF files (DPI: {dpi})...\n")

    converted = 0
    failed = []

    for pdf_file in sorted(pdf_files):
        output_path = output_dir / pdf_file.with_suffix('.png').name
        try:
            convert_pdf_to_png(pdf_file, output_path, dpi)
            converted += 1
        except Exception as e:
            print(f"✗ {pdf_file.name}: {e}")
            failed.append(pdf_file.name)

    print(f"\nDone: {converted} converted, {len(failed)} failed")
    if failed:
        print(f"Failed files: {', '.join(failed)}")


def main():
    """Command-line interface."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Convert PDF files to PNG for web display'
    )
    parser.add_argument(
        'input',
        help='Input PDF file or directory'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output file or directory (default: same location with .png)'
    )
    parser.add_argument(
        '-d', '--dpi',
        type=int,
        default=300,
        help='Resolution in DPI (default: 300, use 150 for smaller web files)'
    )
    parser.add_argument(
        '-p', '--prefix',
        help='Only convert files with this prefix (e.g., "ici-")'
    )

    args = parser.parse_args()

    input_path = Path(args.input)

    if input_path.is_file():
        # Single file conversion
        convert_pdf_to_png(input_path, args.output, args.dpi)
    elif input_path.is_dir():
        # Batch conversion
        batch_convert(input_path, args.output, args.dpi, args.prefix)
    else:
        print(f"Error: {input_path} not found")
        sys.exit(1)


# ICI Project specific files
ICI_FILES = [
    'ici-terreo-plano-1500mm.pdf',
    'ici-terreo-retorno.pdf',
    'ici-terreo-corte-processamento.pdf',
    'ici-1pav-plano-z.pdf',
    'ici-ventiladores-alocados.pdf',
    'ici-ventiladores-150cm.pdf',
    'ici-ventiladores-corte-xz.pdf',
    'ici-ventiladores-retorno.pdf',
]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
    else:
        # Default: show usage
        print("PDF to PNG Converter for Web Display")
        print("=" * 40)
        print("\nUsage:")
        print("  Single file:  python pdf_to_png.py image.pdf")
        print("  Directory:    python pdf_to_png.py ./images/")
        print("  With prefix:  python pdf_to_png.py ./images/ -p ici-")
        print("  Lower DPI:    python pdf_to_png.py ./images/ -d 150")
        print("\nICI project files to convert:")
        for f in ICI_FILES:
            print(f"  - {f}")
        print("\nExample for ICI project:")
        print("  python pdf_to_png.py assets/img/projects/ -p ici- -d 200")
