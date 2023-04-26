import ast
import re
import typing

import bandit
from bandit.core import issue
from bandit.core import test_properties as test

RE_WORDS = "(pas+wo?r?d|pass(phrase)?|pwd|token|secrete?|Final|Literal)"
RE_CANDIDATES = re.compile(
    "(^{0}$|_{0}_|^{0}_|_{0}$)".format(RE_WORDS), re.IGNORECASE
)


def _report(value):
    return bandit.Issue(
        severity=bandit.LOW,
        confidence=bandit.MEDIUM,
        cwe=issue.Cwe.HARD_CODED_PASSWORD,
        text=f"Possible hardcoded password: '{value}'",
    )


@test.checks("Str", "Final", "Literal")
@test.test_id("B105")
class CustomVisitor(ast.NodeVisitor):

    def hardcoded_password_string(context):
        node = context.node
        if isinstance(node._bandit_parent, ast.Assign):
            # looks for "candidate='some_string'"
            for targ in node._bandit_parent.targets:
                if isinstance(targ, ast.Name) and RE_CANDIDATES.search(targ.id):
                    return _report(node.s)
                elif isinstance(targ, ast.Attribute) and RE_CANDIDATES.search(
                        targ.attr
                ):
                    return _report(node.s)

        elif isinstance(
                node._bandit_parent, ast.Subscript
        ) and RE_CANDIDATES.search(node.s):
            # Py39+: looks for "dict[candidate]='some_string'"
            # subscript -> index -> string
            assign = node._bandit_parent._bandit_parent
            if isinstance(assign, ast.Assign) and isinstance(
                    assign.value, ast.Str
            ):
                return _report(assign.value.s)

        elif isinstance(node._bandit_parent, ast.Index) and RE_CANDIDATES.search(
                node.s
        ):
            # looks for "dict[candidate]='some_string'"
            # assign -> subscript -> index -> string
            assign = node._bandit_parent._bandit_parent._bandit_parent
            if isinstance(assign, ast.Assign) and isinstance(
                    assign.value, ast.Str
            ):
                return _report(assign.value.s)

        elif isinstance(node._bandit_parent, ast.Compare):
            # looks for "candidate == 'some_string'"
            comp = node._bandit_parent
            if isinstance(comp.left, ast.Name):
                if RE_CANDIDATES.search(comp.left.id):
                    if isinstance(comp.comparators[0], ast.Str):
                        return _report(comp.comparators[0].s)
            elif isinstance(comp.left, ast.Attribute):
                if RE_CANDIDATES.search(comp.left.attr):
                    if isinstance(comp.comparators[0], ast.Str):
                        return _report(comp.comparators[0].s)
        elif isinstance(node._bandit_parent, (ast.Lambda, ast.FunctionDef)):
            # looks for "lambda x: 'some_string'"
            # functiondef -> args -> string
            for arg in node._bandit_parent.args.args:
                if isinstance(arg.annotation, ast.Subscript):
                    if RE_CANDIDATES.search(arg.annotation.slice.value.s):
                        return _report(node.s)



@test.checks("Call", "Final", "Literal")
@test.test_id("B106")
def hardcoded_password_funcarg(context):
    # looks for "function(candidate='some_string')"
    for kw in context.node.keywords:
        if isinstance(kw.value, ast.Str) and RE_CANDIDATES.search(kw.arg):
            return _report(kw.value.s)


@test.checks("FunctionDef", "Final", "Literal")
@test.test_id("B107")
def hardcoded_password_default(context):

    # looks for "def function(candidate='some_string')"

    # this pads the list of default values with "None" if nothing is given
    # looks for "def function(candidate='some_string')"

    # this pads the list of default values with "None" if nothing is given
    defaults = [None] * (
            len(context.node.args.args) - len(context.node.args.defaults)
    )
    defaults.extend(context.node.args.defaults)

    for default, arg in zip(defaults, context.node.args.args):
        if isinstance(default, ast.Str) and RE_CANDIDATES.search(arg.arg):
            return _report(default.s)
