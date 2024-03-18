from latexgen.latexgen.generate import generate_table, generate_png
from functools import partial


def create_latex_file(begin, end, separator, path, text, mode='w'):
    with open(path, mode) as f:
        f.write(begin + separator + text + separator + end)


def append_to_latex_file(path, text, separator='\n'):
    create_latex_file("", "", separator, path, text, mode='a')


array = [[1, 2, 3], [4, 5, 6]]
file_path = 'artefacts/artefact.tex'
create_latex_file_func = partial(create_latex_file,
                                 begin='\\documentclass[12pt]{article}\n\n\\usepackage{graphicx}\n\n\\begin{document}\n',
                                 end='',
                                 separator='\n')
create_latex_file_func(path=file_path, text=generate_table(array))

image_path = "artefacts/Lenna"
image_latex = generate_png(image_path)
# image_latex = "\includegraphics[width=\\textwidth]{" + image_path + "}"
append_to_latex_file(path=file_path, text=image_latex)

append_to_latex_file(path=file_path, text='\n\\end{document}', separator='')
