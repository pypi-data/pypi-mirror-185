use rustpython_ast::{Expr, ExprKind, Keyword};

use crate::ast::types::Range;
use crate::checkers::ast::Checker;
use crate::registry::Diagnostic;
use crate::violations;

/// B026
pub fn star_arg_unpacking_after_keyword_arg(
    checker: &mut Checker,
    args: &[Expr],
    keywords: &[Keyword],
) {
    let Some(keyword) = keywords.first() else {
        return;
    };
    for arg in args {
        let ExprKind::Starred { .. } = arg.node else {
            continue;
        };
        if arg.location <= keyword.location {
            continue;
        }
        checker.diagnostics.push(Diagnostic::new(
            violations::StarArgUnpackingAfterKeywordArg,
            Range::from_located(arg),
        ));
    }
}
