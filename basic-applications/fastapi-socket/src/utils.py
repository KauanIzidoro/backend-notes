import re
import os 


def validate_input(data: str):
    """_summary_
    Args:
        data (str): texto que seja usado como prompt para interagir com o modelo.

    Raises:
        Exception: Prompts que forem caminhos de arquivos ou imagens não são permitidos.

    Returns:
        str: prompt se for válido.
    """
    if re.search(os.sep, data) or re.search(r"\.(png|svg|jpg)$", data):
        raise Exception("O prompt deve ser texto!")
    return data
    