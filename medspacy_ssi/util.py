from os import path

# Filepath to default rules which are included in package
from pathlib import Path

from .document_classifier import DocumentClassifier

DEFAULT_PIPENAMES = {
    "sentencizer",
    "target_matcher",
    "context",
    "tokenizer",
}

RESOURCES_DIR = path.join(Path(__file__).resolve().parents[1], "resources")

CONTEXT_ATTRS = {
    'NEGATED_EXISTENCE': {'is_negated': True},
    'POSSIBLE_EXISTENCE': {'is_uncertain': True},
    'HISTORICAL': {'is_historical': True},
    'HYPOTHETICAL': {'is_hypothetical': True},
    'FAMILY': {'is_family': True},
    'INDICATION': {'is_uncertain': True},
}

def load():
    import medspacy
    nlp = medspacy.load(enable=["sentencizer", "tokenizer"])

    # Add components
    from medspacy.target_matcher import TargetMatcher, TargetRule
    target_matcher = TargetMatcher(nlp)
    target_filepath = path.join(RESOURCES_DIR, "target_rules.json")
    target_rules = TargetRule.from_json(target_filepath)
    target_matcher.add(target_rules)
    nlp.add_pipe(target_matcher)

    from medspacy.context import ConTextComponent, ConTextRule
    context_filepath = path.join(RESOURCES_DIR, "context_rules.json")
    context = ConTextComponent(nlp, rules=None, add_attrs=CONTEXT_ATTRS)
    context_rules = ConTextRule.from_json(context_filepath)
    context.add(context_rules)
    nlp.add_pipe(context)

    from medspacy.section_detection import Sectionizer
    # TODO: Add radiology section rules
    sectionizer = Sectionizer(nlp)
    nlp.add_pipe(sectionizer)

    clf = DocumentClassifier(nlp)
    nlp.add_pipe(clf)

    return nlp

