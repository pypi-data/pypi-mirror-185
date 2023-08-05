use rustpython_ast::Expr;

use crate::ast::helpers::match_module_member;
use crate::ast::types::Range;
use crate::autofix::Fix;
use crate::checkers::ast::Checker;
use crate::registry::Diagnostic;
use crate::violations;

/// UP019
pub fn typing_text_str_alias(checker: &mut Checker, expr: &Expr) {
    if match_module_member(
        expr,
        "typing",
        "Text",
        &checker.from_imports,
        &checker.import_aliases,
    ) {
        let mut diagnostic =
            Diagnostic::new(violations::TypingTextStrAlias, Range::from_located(expr));
        if checker.patch(diagnostic.kind.code()) {
            diagnostic.amend(Fix::replacement(
                "str".to_string(),
                expr.location,
                expr.end_location.unwrap(),
            ));
        }
        checker.diagnostics.push(diagnostic);
    }
}
