import argparse
import pypandoc
from pathlib import Path

DEFAULT_INPUT_PATH = Path('./markdown/resume.md')
DEFAULT_OUTPUT_PATH = Path('./output/resume.pdf')

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown resume to PDF using Pandoc and LaTeX')
    parser.add_argument('-i', '--input', type=str, default=str(DEFAULT_INPUT_PATH),
                        help='Input Markdown file path (default: ./markdown/resume.md)')
    parser.add_argument('-o', '--output', type=str, default=str(DEFAULT_OUTPUT_PATH),
                        help='Output PDF file path (default: ./output/resume.pdf)')
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    output_path = Path(args.output)
    
    assert input_path.exists(), f"Input file {input_path} does not exist."
    
    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    output = pypandoc.convert_file(input_path, 'pdf', outputfile=output_path, extra_args=['--template=default_template.tex','--pdf-engine=xelatex'])
    assert output == ""
    print(f"Successfully converted {input_path} to {output_path}")


if __name__ == "__main__":
    main()
