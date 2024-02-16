from collections import Counter
from operator import itemgetter
import streamlit as st
import pandas as pd

import graphviz

import ner


example = (
        "When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")

if "view" not in st.session_state:
    st.session_state.view = None 

# st.set_page_config(layout='wide')
st.markdown('## spaCy Named Entity Recognition')
st.sidebar.radio('#### select views', ['Entities', 'Dependencies'], key = "view", index = None)

text = st.text_area('Text to process', value=example, height=100)

doc = ner.SpacyDocument(text)

entities = pd.DataFrame(doc.get_entities(),columns=['Start', 'End', 'label', 'word'])
dependencies = pd.DataFrame(doc.get_dependency(),columns=['word', 'Dependency', 'Head Text'])
tokens = doc.get_tokens()
counter = Counter(tokens)
words = list(sorted(counter.most_common(30)))


table_tab, graph_tab, = st.tabs(["Table", "Graph"])

with table_tab:
    if st.session_state.view ==  None:
        st.error('Please select a **view**',icon="⚠️")
    else:
        if st.session_state.view == 'Entities':
            st.table(entities)
        elif st.session_state.view == 'Dependencies':
            st.table(dependencies)
        st.markdown(f'Total number of tokens: {len(tokens)}<br/>'
            f'Total number of types: {len(counter)}', unsafe_allow_html=True)
        
with graph_tab:
    if st.session_state.view ==  None:
        st.error('Please select a **view**',icon="⚠️")

    elif st.session_state.view == 'Entities':
        doc.get_ents_graph()

    elif st.session_state.view == 'Dependencies':
        graph = graphviz.Digraph()
        for index, row in dependencies.iterrows():
            word = row['word']
            dependency = row['Dependency']
            head_text = row['Head Text']
            graph.edge(head_text, word, label=dependency)

        st.graphviz_chart(graph)