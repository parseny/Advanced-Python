from functools import wraps


# def generate_table(array):
#     number_columns = len(array[0])
#     columns = "\\begin{tabular}{" + "||" + " c " * number_columns + "||}"
#     res = [columns]
#     res.append("\hline")
#     for row in array:
#         row = " & ".join(map(str, row)) + " \\\\"
#         res.append(row)
#         res.append("\hline")
#     res.append("\\end{tabular}")
#     return '\n'.join(res)


def row_decorator(func):
    @wraps(func)
    def wrapper(row):
        formatted_row = func(row)
        return f"{formatted_row}\\\\\n\\hline\n"

    return wrapper


@row_decorator
def format_row(row):
    return " & ".join(map(str, row))


def generate_table(array):
    number_columns = len(array[0])
    columns = "\\begin{tabular}{" + "||" + " c " * number_columns + "||}\n\\hline\n"
    body = "".join(map(format_row, array))
    res = f"{columns}{body}" + "\\end{tabular}"
    return res


def generate_png(image_path):
    res = "\includegraphics[width=\\textwidth]{" + image_path + "}"
    return res
