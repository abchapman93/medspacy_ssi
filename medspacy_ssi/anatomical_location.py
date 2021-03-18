from spacy.tokens import Span

def get_anatomical_location(span):
    for modifier in span._.modifiers:
        if modifier.category == "ANATOMY":
            return modifier.span
    return None

Span.set_extension("anatomical_location", getter=get_anatomical_location)
