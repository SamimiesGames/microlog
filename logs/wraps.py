from .assets import item_clause_enter, item_clause_leave, error_clause_enter, \
    error_clause_leave, important_clause_enter, important_clause_leave


def error_item(message, quote=True):
    if quote:
        message = quote_wrapped(message)

    return f"{error_clause_enter}{message}{error_clause_leave}"


def data_item(message, quote=True):
    if quote:
        message = quote_wrapped(message)

    return f"{item_clause_enter}{message}{item_clause_leave}"


def important_data_item(message, quote=True):
    if quote:
        message = quote_wrapped(message)

    return f"{important_clause_enter}{message}{important_clause_leave}"


def quote_wrapped(message):
    return f"'{message}'"
