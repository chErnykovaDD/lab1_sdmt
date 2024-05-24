import sys
import argparse
import re

def parse_markdown(input_text):
    html_output = []
    in_preformatted = False

    for line in input_text.split('\n'):
        if line.strip() == "":
            if not in_preformatted:
                html_output.append("</p><p>")
            else:
                html_output.append("\n")
            continue

        if line.startswith("```"):
            if in_preformatted:
                html_output.append("</pre>")
            else:
                html_output.append("<pre>")
            in_preformatted = not in_preformatted
            continue

        if in_preformatted:
            html_output.append(line + "\n")  # Ensure new lines are preserved
            continue

        line = handle_markdown_elements(line)

        html_output.append(line)

    if in_preformatted:
        raise ValueError("Invalid markdown: unclosed preformatted block")

    return '<p>' + ''.join(html_output) + '</p>'

def handle_markdown_elements(line):
    markdown_elements = [
        (r'\*\*(\S.*?\S)\*\*', r'<b>\1</b>'),
        (r'__(.*?)__', r'<b>\1</b>'),
        (r'`(\S.*?\S)`', r'<tt>\1</tt>'),
        (r'(^|\s)_(\S.*?\S)_(?=\s|$)', r'\1<i>\2</i>'),
        (r'^# (.*)', r'<h1>\1</h1>'),
        (r'^## (.*)', r'<h2>\1</h2>')
    ]

    for pattern, replacement in markdown_elements:
        line = re.sub(pattern, replacement, line)

    return line
def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def generate_html(markdown_text):
    try:
        html_output = parse_markdown(markdown_text)
        return html_output
    except ValueError as e:
        sys.stderr.write(str(e) + '\n')
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Markdown to HTML converter")
    parser.add_argument('input', help="Path to the input markdown file")
    parser.add_argument('--out', help="Path to the output HTML file")
    args = parser.parse_args()

    markdown_text = read_file(args.input)
    html_output = generate_html(markdown_text)

    if args.out:
        with open(args.out, 'w', encoding='utf-8') as file:
            file.write(html_output)
    else:
        print(html_output)

if __name__ == "__main__":
    main()