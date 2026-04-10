#!/usr/bin/env python3
"""
NEOMAAA Broker — Markdown to PDF Generator
Converts all markdown documents in docs/ to professional PDFs.
Uses: markdown (for parsing) + reportlab (for PDF generation)
"""

import os
import re
import sys
import glob
import markdown
from io import BytesIO
from xml.etree import ElementTree as ET

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, black, white, Color
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable, ListFlowable, ListItem,
    BaseDocTemplate, Frame, PageTemplate
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ─── Colors ───────────────────────────────────────────────────────────────────
GREEN_PRIMARY = HexColor("#00D4AA")
GREEN_DARK = HexColor("#006B55")
GREEN_LIGHT = HexColor("#E6FFF8")
GREEN_HEADER_BG = HexColor("#006B55")
TEXT_DARK = HexColor("#1a1a1a")
TEXT_BODY = HexColor("#333333")
TEXT_MUTED = HexColor("#666666")
BG_LIGHT = HexColor("#f9f9f9")
BG_CODE = HexColor("#f4f4f5")
BORDER_LIGHT = HexColor("#e5e7eb")
BORDER_TABLE = HexColor("#d1d5db")

# ─── Configuration ────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, "docs")
OUTPUT_DIR = os.path.join(DOCS_DIR, "pdf", "es")

EXCLUDE_FILES = {"_sidebar.md", "README.md", "404.md"}
EXCLUDE_DIRS = {"superpowers"}

PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 20 * mm


def get_styles():
    """Create custom paragraph styles for the PDF."""
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name='DocTitle',
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=28,
        textColor=TEXT_DARK,
        spaceAfter=4 * mm,
        spaceBefore=0,
    ))

    styles.add(ParagraphStyle(
        name='H1Custom',
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=26,
        textColor=TEXT_DARK,
        spaceBefore=10 * mm,
        spaceAfter=4 * mm,
    ))

    styles.add(ParagraphStyle(
        name='H2Custom',
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=21,
        textColor=GREEN_DARK,
        spaceBefore=8 * mm,
        spaceAfter=3 * mm,
    ))

    styles.add(ParagraphStyle(
        name='H3Custom',
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=TEXT_DARK,
        spaceBefore=6 * mm,
        spaceAfter=2 * mm,
    ))

    styles.add(ParagraphStyle(
        name='H4Custom',
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=TEXT_BODY,
        spaceBefore=4 * mm,
        spaceAfter=2 * mm,
    ))

    styles.add(ParagraphStyle(
        name='BodyCustom',
        fontName='Helvetica',
        fontSize=10,
        leading=16,
        textColor=TEXT_BODY,
        spaceAfter=3 * mm,
        alignment=TA_JUSTIFY,
    ))

    styles.add(ParagraphStyle(
        name='BulletCustom',
        fontName='Helvetica',
        fontSize=10,
        leading=16,
        textColor=TEXT_BODY,
        leftIndent=8 * mm,
        spaceAfter=1.5 * mm,
        bulletIndent=2 * mm,
    ))

    styles.add(ParagraphStyle(
        name='BulletNested',
        fontName='Helvetica',
        fontSize=10,
        leading=16,
        textColor=TEXT_BODY,
        leftIndent=16 * mm,
        spaceAfter=1.5 * mm,
        bulletIndent=10 * mm,
    ))

    styles.add(ParagraphStyle(
        name='NumberedCustom',
        fontName='Helvetica',
        fontSize=10,
        leading=16,
        textColor=TEXT_BODY,
        leftIndent=8 * mm,
        spaceAfter=1.5 * mm,
        bulletIndent=2 * mm,
    ))

    styles.add(ParagraphStyle(
        name='CodeBlock',
        fontName='Courier',
        fontSize=8.5,
        leading=13,
        textColor=TEXT_DARK,
        backColor=BG_CODE,
        leftIndent=4 * mm,
        rightIndent=4 * mm,
        spaceBefore=2 * mm,
        spaceAfter=3 * mm,
        borderPadding=(3 * mm, 3 * mm, 3 * mm, 3 * mm),
    ))

    styles.add(ParagraphStyle(
        name='CodeInline',
        fontName='Courier',
        fontSize=9,
        textColor=TEXT_DARK,
        backColor=BG_CODE,
    ))

    styles.add(ParagraphStyle(
        name='BlockQuote',
        fontName='Helvetica-Oblique',
        fontSize=10,
        leading=16,
        textColor=GREEN_DARK,
        leftIndent=8 * mm,
        spaceBefore=3 * mm,
        spaceAfter=3 * mm,
        borderPadding=(2 * mm, 2 * mm, 2 * mm, 4 * mm),
    ))

    styles.add(ParagraphStyle(
        name='FooterStyle',
        fontName='Helvetica',
        fontSize=8,
        textColor=TEXT_MUTED,
        alignment=TA_CENTER,
    ))

    styles.add(ParagraphStyle(
        name='HeaderStyle',
        fontName='Helvetica',
        fontSize=7,
        textColor=TEXT_MUTED,
        alignment=TA_RIGHT,
    ))

    return styles


def header_footer(canvas, doc):
    """Draw header and footer on each page."""
    canvas.saveState()

    # Header: right-aligned text
    canvas.setFont('Helvetica', 7)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawRightString(
        PAGE_WIDTH - MARGIN,
        PAGE_HEIGHT - 12 * mm,
        "NEOMAAA Markets — Documento Interno"
    )

    # Thin green line under header
    canvas.setStrokeColor(GREEN_PRIMARY)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, PAGE_HEIGHT - 14 * mm, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 14 * mm)

    # Footer: page number centered
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawCentredString(
        PAGE_WIDTH / 2,
        10 * mm,
        f"Página {doc.page}"
    )

    # Thin line above footer
    canvas.setStrokeColor(BORDER_LIGHT)
    canvas.setLineWidth(0.3)
    canvas.line(MARGIN, 14 * mm, PAGE_WIDTH - MARGIN, 14 * mm)

    canvas.restoreState()


def sanitize_text(text):
    """Clean text for reportlab Paragraph (escape XML-invalid chars)."""
    if not text:
        return ""
    # Replace & first (before other replacements that introduce &)
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text


def format_inline(text):
    """Convert inline markdown formatting to reportlab XML tags."""
    if not text:
        return ""

    # Escape XML entities first
    text = text.replace("&", "&amp;")

    # Bold + Italic (***text*** or ___text___)
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', text)
    text = re.sub(r'___(.+?)___', r'<b><i>\1</i></b>', text)

    # Bold (**text** or __text__)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'__(.+?)__', r'<b>\1</b>', text)

    # Italic (*text* or _text_) — be careful not to match inside words with underscores
    text = re.sub(r'(?<!\w)\*([^\*]+?)\*(?!\w)', r'<i>\1</i>', text)
    text = re.sub(r'(?<!\w)_([^_]+?)_(?!\w)', r'<i>\1</i>', text)

    # Inline code (`text`)
    text = re.sub(r'`([^`]+?)`', r'<font name="Courier" size="9" color="#1a1a1a">\1</font>', text)

    # Links [text](url)
    text = re.sub(r'\[([^\]]+?)\]\(([^\)]+?)\)', r'<font color="#006B55"><u>\1</u></font>', text)

    # Strikethrough ~~text~~
    text = re.sub(r'~~(.+?)~~', r'<strike>\1</strike>', text)

    return text


def parse_markdown_to_elements(md_text, styles):
    """Parse markdown text and return a list of reportlab flowable elements."""
    elements = []
    lines = md_text.split('\n')
    i = 0
    first_h1 = True

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip empty lines
        if not stripped:
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^(-{3,}|\*{3,}|_{3,})$', stripped):
            elements.append(Spacer(1, 2 * mm))
            elements.append(HRFlowable(
                width="100%", thickness=0.5,
                color=BORDER_LIGHT, spaceBefore=2 * mm, spaceAfter=4 * mm
            ))
            i += 1
            continue

        # Headers
        header_match = re.match(r'^(#{1,6})\s+(.+)$', stripped)
        if header_match:
            level = len(header_match.group(1))
            text = format_inline(header_match.group(2))

            if level == 1:
                if first_h1:
                    elements.append(Paragraph(text, styles['DocTitle']))
                    # Green bottom border for H1
                    elements.append(HRFlowable(
                        width="100%", thickness=2,
                        color=GREEN_PRIMARY, spaceBefore=0, spaceAfter=6 * mm
                    ))
                    first_h1 = False
                else:
                    elements.append(Paragraph(text, styles['H1Custom']))
                    elements.append(HRFlowable(
                        width="100%", thickness=2,
                        color=GREEN_PRIMARY, spaceBefore=0, spaceAfter=4 * mm
                    ))
            elif level == 2:
                elements.append(Paragraph(text, styles['H2Custom']))
            elif level == 3:
                elements.append(Paragraph(text, styles['H3Custom']))
            else:
                elements.append(Paragraph(text, styles['H4Custom']))

            i += 1
            continue

        # Fenced code block
        if stripped.startswith('```'):
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing ```

            code_text = sanitize_text('\n'.join(code_lines))
            code_text = code_text.replace('\n', '<br/>')
            code_text = code_text.replace(' ', '&nbsp;')
            elements.append(Paragraph(code_text, styles['CodeBlock']))
            continue

        # Blockquote
        if stripped.startswith('>'):
            quote_lines = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                quote_text = re.sub(r'^>\s*', '', lines[i].strip())
                quote_lines.append(quote_text)
                i += 1

            quote_content = format_inline(' '.join(quote_lines))

            # Create blockquote with left green border using a table
            quote_para = Paragraph(quote_content, styles['BlockQuote'])
            quote_table = Table(
                [[quote_para]],
                colWidths=[PAGE_WIDTH - 2 * MARGIN - 10 * mm],
            )
            quote_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), GREEN_LIGHT),
                ('LEFTPADDING', (0, 0), (-1, -1), 4 * mm),
                ('RIGHTPADDING', (0, 0), (-1, -1), 3 * mm),
                ('TOPPADDING', (0, 0), (-1, -1), 2 * mm),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 2 * mm),
                ('LINEBEFOREDECOR', (0, 0), (0, -1), 3, GREEN_PRIMARY),
            ]))
            elements.append(Spacer(1, 2 * mm))
            elements.append(quote_table)
            elements.append(Spacer(1, 2 * mm))
            continue

        # Table
        if '|' in stripped and i + 1 < len(lines):
            table_lines = []
            # Collect all table lines
            start_i = i
            while i < len(lines) and '|' in lines[i].strip():
                table_lines.append(lines[i].strip())
                i += 1

            if len(table_lines) >= 2:
                # Parse table
                parsed_rows = []
                separator_idx = None
                for idx, tl in enumerate(table_lines):
                    cells = [c.strip() for c in tl.strip('|').split('|')]
                    # Check if this is a separator row (---|---|---)
                    if all(re.match(r'^[-:]+$', c.strip()) for c in cells if c.strip()):
                        separator_idx = idx
                        continue
                    parsed_rows.append(cells)

                if parsed_rows:
                    # Normalize column count
                    max_cols = max(len(r) for r in parsed_rows)
                    for row in parsed_rows:
                        while len(row) < max_cols:
                            row.append('')

                    # Calculate column widths
                    available_width = PAGE_WIDTH - 2 * MARGIN - 4 * mm
                    col_width = available_width / max_cols

                    # Create table data with Paragraphs
                    table_data = []
                    for row_idx, row in enumerate(parsed_rows):
                        table_row = []
                        for cell in row:
                            cell_text = format_inline(cell)
                            if row_idx == 0 and separator_idx is not None:
                                # Header row
                                style = ParagraphStyle(
                                    'TableHeader',
                                    parent=styles['BodyCustom'],
                                    fontName='Helvetica-Bold',
                                    fontSize=9,
                                    leading=13,
                                    textColor=white,
                                    spaceAfter=0,
                                    spaceBefore=0,
                                    alignment=TA_LEFT,
                                )
                            else:
                                style = ParagraphStyle(
                                    'TableCell',
                                    parent=styles['BodyCustom'],
                                    fontSize=9,
                                    leading=13,
                                    spaceAfter=0,
                                    spaceBefore=0,
                                    alignment=TA_LEFT,
                                )
                            table_row.append(Paragraph(cell_text, style))
                        table_data.append(table_row)

                    if not table_data:
                        continue

                    t = Table(table_data, colWidths=[col_width] * max_cols)

                    # Table styling
                    style_cmds = [
                        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_TABLE),
                        ('TOPPADDING', (0, 0), (-1, -1), 2 * mm),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 2 * mm),
                        ('LEFTPADDING', (0, 0), (-1, -1), 2 * mm),
                        ('RIGHTPADDING', (0, 0), (-1, -1), 2 * mm),
                        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    ]

                    # Header row styling
                    if separator_idx is not None and len(table_data) > 0:
                        style_cmds.append(('BACKGROUND', (0, 0), (-1, 0), GREEN_HEADER_BG))
                        style_cmds.append(('TEXTCOLOR', (0, 0), (-1, 0), white))

                        # Alternating row colors for data rows
                        for row_idx in range(1, len(table_data)):
                            if row_idx % 2 == 0:
                                style_cmds.append(('BACKGROUND', (0, row_idx), (-1, row_idx), BG_LIGHT))

                    t.setStyle(TableStyle(style_cmds))
                    elements.append(Spacer(1, 2 * mm))
                    elements.append(KeepTogether([t]))
                    elements.append(Spacer(1, 3 * mm))
                continue

        # Checkbox list items
        checkbox_match = re.match(r'^[-*]\s+\[( |x|X)\]\s+(.+)$', stripped)
        if checkbox_match:
            checked = checkbox_match.group(1).lower() == 'x'
            item_text = format_inline(checkbox_match.group(2))
            marker = "☑" if checked else "☐"
            elements.append(Paragraph(
                f"{marker}&nbsp;&nbsp;{item_text}",
                styles['BulletCustom']
            ))
            i += 1
            continue

        # Unordered list items
        ul_match = re.match(r'^(\s*)([-*+])\s+(.+)$', stripped)
        if ul_match:
            indent = len(line) - len(line.lstrip())
            item_text = format_inline(ul_match.group(3))
            if indent >= 2:
                elements.append(Paragraph(
                    f"◦&nbsp;&nbsp;{item_text}",
                    styles['BulletNested']
                ))
            else:
                elements.append(Paragraph(
                    f"•&nbsp;&nbsp;{item_text}",
                    styles['BulletCustom']
                ))
            i += 1
            continue

        # Ordered list items
        ol_match = re.match(r'^(\d+)[.)]\s+(.+)$', stripped)
        if ol_match:
            num = ol_match.group(1)
            item_text = format_inline(ol_match.group(2))
            elements.append(Paragraph(
                f"{num}.&nbsp;&nbsp;{item_text}",
                styles['NumberedCustom']
            ))
            i += 1
            continue

        # Regular paragraph — collect consecutive non-empty, non-special lines
        para_lines = []
        while i < len(lines):
            cl = lines[i].strip()
            if not cl:
                break
            if cl.startswith('#') or cl.startswith('```') or cl.startswith('>'):
                break
            if cl.startswith('|') and i + 1 < len(lines) and '|' in lines[i + 1]:
                break
            if re.match(r'^(-{3,}|\*{3,}|_{3,})$', cl):
                break
            if re.match(r'^[-*+]\s+', cl):
                break
            if re.match(r'^\d+[.)]\s+', cl):
                break
            para_lines.append(cl)
            i += 1

        if para_lines:
            para_text = format_inline(' '.join(para_lines))
            elements.append(Paragraph(para_text, styles['BodyCustom']))
            continue

        # Fallback: skip line
        i += 1

    return elements


def generate_pdf(md_filepath, output_filepath, styles):
    """Convert a single markdown file to PDF."""
    with open(md_filepath, 'r', encoding='utf-8') as f:
        md_text = f.read()

    elements = parse_markdown_to_elements(md_text, styles)

    if not elements:
        print(f"  WARNING: No content parsed from {md_filepath}")
        return False

    # Build the PDF
    doc = SimpleDocTemplate(
        output_filepath,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN + 4 * mm,  # Extra space for header
        bottomMargin=MARGIN,
        title=os.path.basename(md_filepath).replace('.md', ''),
        author="NEOMAAA Markets",
    )

    try:
        doc.build(elements, onFirstPage=header_footer, onLaterPages=header_footer)
        return True
    except Exception as e:
        print(f"  ERROR building PDF: {e}")
        return False


def collect_md_files(docs_dir):
    """Find all .md files to process, respecting exclusions."""
    md_files = []
    for root, dirs, files in os.walk(docs_dir):
        # Skip excluded directories
        rel_root = os.path.relpath(root, docs_dir)
        root_parts = rel_root.split(os.sep)
        if any(part in EXCLUDE_DIRS for part in root_parts):
            continue

        # Skip pdf directory itself
        if 'pdf' in root_parts:
            continue

        for f in sorted(files):
            if f.endswith('.md') and f not in EXCLUDE_FILES:
                md_files.append(os.path.join(root, f))

    return sorted(md_files)


def main():
    """Main entry point."""
    print("=" * 60)
    print("NEOMAAA Broker — PDF Generator")
    print("=" * 60)

    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Collect files
    md_files = collect_md_files(DOCS_DIR)
    print(f"\nFound {len(md_files)} markdown files to process:\n")

    for f in md_files:
        rel = os.path.relpath(f, DOCS_DIR)
        print(f"  - {rel}")

    print()

    # Get styles
    styles = get_styles()

    # Process each file
    success_count = 0
    error_count = 0
    errors = []
    generated_files = []

    for md_file in md_files:
        rel_path = os.path.relpath(md_file, DOCS_DIR)
        # Create output filename: replace / with - and change extension
        output_name = rel_path.replace(os.sep, '-').replace('.md', '.pdf')
        output_path = os.path.join(OUTPUT_DIR, output_name)

        print(f"  Processing: {rel_path} -> {output_name} ...", end=" ")

        try:
            result = generate_pdf(md_file, output_path, styles)
            if result:
                size = os.path.getsize(output_path)
                print(f"OK ({size:,} bytes)")
                success_count += 1
                generated_files.append((rel_path, output_name, size))
            else:
                print("FAILED (no content)")
                error_count += 1
                errors.append((rel_path, "No content parsed"))
        except Exception as e:
            print(f"ERROR: {e}")
            error_count += 1
            errors.append((rel_path, str(e)))

    # Summary
    print("\n" + "=" * 60)
    print(f"SUMMARY: {success_count} PDFs generated, {error_count} errors")
    print("=" * 60)

    if errors:
        print("\nErrors:")
        for path, err in errors:
            print(f"  - {path}: {err}")

    if generated_files:
        print(f"\nOutput directory: {OUTPUT_DIR}")
        total_size = sum(s for _, _, s in generated_files)
        print(f"Total size: {total_size:,} bytes ({total_size / 1024 / 1024:.1f} MB)")

    return generated_files, errors


if __name__ == "__main__":
    generated, errors = main()
    sys.exit(1 if errors else 0)
