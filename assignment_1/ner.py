import io
import pandas as pd
import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

class SpacyDocument:

    def __init__(self, text: str):
        self.text = text
        self.doc = nlp(text)

    def get_tokens(self) -> list:
        return [token.lemma_ for token in self.doc]

    def get_entities(self) -> str:
        entities = [(e.start_char, e.end_char, e.label_, e.text) for e in self.doc.ents]
        return entities
    
    def get_dependency(self)-> str:
        dependencies = [(token.text, token.dep_, token.head.text) for token in self.doc]
        return dependencies

    def get_markup_html(self) -> str:
        html = displacy.render(self.doc, style="ent", page=True)+ "<br>"
        html += pd.DataFrame(self.get_dependency(), columns=['Word', 'Dependency', 'Head Text']).to_html(index=False)
        return html

if __name__ == '__main__':

    example = (
        "When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")

    doc = SpacyDocument(example)
    print(doc.get_tokens())
    for entity in doc.get_entities():
        print(entity)
    print(doc.get_entities_with_markup())