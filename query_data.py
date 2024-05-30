import argparse
import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""


def query_rag(query_text: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    # print(prompt)

    model = Ollama(model="llama3")
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)
    return response_text, sources


# Streamlit app
def main():
    st.title("Chatbot with Local LLM using llama3 and RAG")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    query_text = st.text_input("Enter your question:")
    
    if st.button("Submit"):
        if query_text:
            response_text, sources = query_rag(query_text)
            st.session_state.chat_history.append((query_text, response_text, sources))

    if st.session_state.chat_history:
        for query, response, sources in st.session_state.chat_history:
            st.write(f"**You:** {query}")
            st.write(f"**Bot:** {response}")
            st.write(f"**Sources:** {', '.join(map(str, sources))}")

if __name__ == "__main__":
    main()