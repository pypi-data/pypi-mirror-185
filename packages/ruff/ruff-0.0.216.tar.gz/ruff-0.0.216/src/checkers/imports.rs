//! Lint rules based on import analysis.

use std::path::Path;

use rustpython_parser::ast::Suite;

use crate::ast::visitor::Visitor;
use crate::directives::IsortDirectives;
use crate::isort;
use crate::isort::track::ImportTracker;
use crate::registry::Diagnostic;
use crate::settings::{flags, Settings};
use crate::source_code_locator::SourceCodeLocator;
use crate::source_code_style::SourceCodeStyleDetector;

fn check_import_blocks(
    tracker: ImportTracker,
    locator: &SourceCodeLocator,
    settings: &Settings,
    stylist: &SourceCodeStyleDetector,
    autofix: flags::Autofix,
    package: Option<&Path>,
) -> Vec<Diagnostic> {
    let mut diagnostics = vec![];
    for block in tracker.into_iter() {
        if !block.imports.is_empty() {
            if let Some(diagnostic) =
                isort::rules::check_imports(&block, locator, settings, stylist, autofix, package)
            {
                diagnostics.push(diagnostic);
            }
        }
    }
    diagnostics
}

#[allow(clippy::too_many_arguments)]
pub fn check_imports(
    python_ast: &Suite,
    locator: &SourceCodeLocator,
    directives: &IsortDirectives,
    settings: &Settings,
    stylist: &SourceCodeStyleDetector,
    autofix: flags::Autofix,
    path: &Path,
    package: Option<&Path>,
) -> Vec<Diagnostic> {
    let mut tracker = ImportTracker::new(locator, directives, path);
    for stmt in python_ast {
        tracker.visit_stmt(stmt);
    }
    check_import_blocks(tracker, locator, settings, stylist, autofix, package)
}
