from spacy.tokens import Doc
Doc.set_extension("document_classification", default=None, force=True)


class DocumentClassifier:
    name = "document_classifier"

    def __init__(self, nlp=None):
        pass

    def __call__(self, doc):
        for ent in doc.ents:
            if ent.label_.upper() != "FLUID_COLLECTION":
                continue
            if any([ent._.is_negated, ent._.is_historical,
                    ent._.is_uncertain, ent._.is_family, ent._.is_hypothetical, ]):
                continue
            if not ent._.anatomical_location:
                continue
            doc._.document_classification = "POS"
            return doc

        doc._.document_classification = "NEG"
        return doc