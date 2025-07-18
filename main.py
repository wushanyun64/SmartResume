import pypandoc
from pathlib import Path

INPUT_PATH = Path('./markdown/resume.md')
OUTPUT_PATH = Path('./output/resume.pdf')

def main():
    input_path = INPUT_PATH
    assert input_path.exists(), f"Input file {input_path} does not exist."
    output_path = OUTPUT_PATH
    output = pypandoc.convert_file(input_path, 'pdf', outputfile=output_path, extra_args=['--template=default_template.tex','--pdf-engine=xelatex'])
    assert output == ""


if __name__ == "__main__":
    main()
