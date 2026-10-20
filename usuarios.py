
import re


def validar_email(email: str) -> bool:
    """Valida o formato básico de um endereço de e-mail."""

    if not isinstance(email, str):
        return False

    email = email.strip()

    # Verifica o tamanho total
    if not email or len(email) > 254:
        return False

    # Verifica se existe exatamente um @
    if email.count("@") != 1:
        return False

    usuario, dominio = email.split("@")

    # Verifica o usuário
    if not usuario or len(usuario) > 64:
        return False

    if usuario.startswith(".") or usuario.endswith("."):
        return False

    if ".." in usuario:
        return False

    # Verifica o domínio
    if not dominio or len(dominio) > 253:
        return False

    if "." not in dominio:
        return False

    if dominio.startswith(".") or dominio.endswith("."):
        return False

    # Verifica os caracteres permitidos no usuário
    if not re.fullmatch(
        r"[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+", usuario
    ):
        return False

    # Verifica cada parte do domínio
    partes = dominio.split(".")

    for parte in partes:
        if not parte or len(parte) > 63:
            return False

        if not re.fullmatch(r"[a-zA-Z0-9-]+", parte):
            return False

        if parte.startswith("-") or parte.endswith("-"):
            return False

    # Exige pelo menos dois caracteres na extensão
    if len(partes[-1]) < 2:
        return False

    return True
