from colorama import Back, Fore
from logs.asset import *


OPERATOR_COLOR = Fore.MAGENTA
CONTEXT_COLOR = Fore.LIGHTGREEN_EX

UNSPECIFIED = Asset("Unspecified!", Fore.BLACK, Back.YELLOW)

info = Asset("info:", Fore.BLUE)
warn = Asset("warn:", Fore.BLACK, Back.YELLOW)
error = Asset("error:", Fore.RED)
fatal = Asset("fatal:", Fore.BLACK, Back.RED)

future_error = Asset("future_error:", Fore.BLACK, Back.YELLOW)

column = Asset(":", OPERATOR_COLOR)
question = Asset("?", OPERATOR_COLOR)
add = Asset("+", Fore.LIGHTGREEN_EX)
sub = Asset("-", Fore.RED)

tabulated = Asset("   ", CONTEXT_COLOR)
indented = Asset("...", CONTEXT_COLOR)
roman_dash = Asset("---", CONTEXT_COLOR)
arrow_right = Asset("-->", CONTEXT_COLOR)
at = Asset("at", CONTEXT_COLOR)
reason = Asset("reason", CONTEXT_COLOR)

ok = Asset("ok", Fore.GREEN)
fail = Asset("fail", Fore.RED)
yes = Asset("yes", Fore.LIGHTGREEN_EX)
no = Asset("no", Fore.LIGHTRED_EX)

done = Asset("done", Fore.LIGHTGREEN_EX)

waiting = Asset("waiting", CONTEXT_COLOR)
working = Asset("working", CONTEXT_COLOR)
ignore = Asset("ingore", CONTEXT_COLOR)
resolved = Asset("resolved", Fore.LIGHTGREEN_EX)
resolve = Asset("resolve", Fore.WHITE)
merge = Asset("merge", Fore.WHITE)
promise = Asset("promise", Fore.WHITE)
saved = Asset("saved", Fore.WHITE)

error_clause_enter = Asset("", Fore.RED, reset=False)
error_clause_leave = Asset("", Fore.RED, reset=True)

item_clause_enter = Asset("", Fore.LIGHTCYAN_EX, reset=False)
item_clause_leave = Asset("", Fore.LIGHTCYAN_EX)

important_clause_enter = Asset("", Fore.BLACK, Back.CYAN, reset=False)
important_clause_leave = Asset("", Fore.BLACK, Back.CYAN)


validator_stylesheet = {
    True: yes,
    False: no
}
