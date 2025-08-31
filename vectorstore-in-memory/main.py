# to chat with the pdf document

import os
os.environ['OPENAI_API_KEY'] = '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'

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings, OpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain import hub

# FAISS helps us take objects like PDF chunks and perform similarity search
# advantage is that the size of the objects will fit into the RAM so the search is efficient

# takes the .pkl file we created as the dump of the vector store and then loads it back into memory

if __name__ == "__main__":
    print('hi')
    path = 'C:\\Users\\Lenovo\\Documents\\LangChain_Course\\vectorstore-in-memory\\2210.03629v3.pdf'
    loader = PyPDFLoader(file_path=path)
    document = loader.load()        # holds the PDF chunks

    # we need to break into chunks one more time to get a control on the chunk size
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=30, separator="\n")
    chunks = text_splitter.split_documents(documents=document)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents=chunks, embedding=embeddings)  # func to create vectors out of the chunks
    # it also turns these vectors into files and stores them in the RAM
    vectorstore.save_local(folder_path='faiss_index', index_name='faiss_index_react')

    new_vectorstore = FAISS.load_local(
        folder_path='faiss_index', 
        index_name='faiss_index_react', 
        embeddings=embeddings, 
        allow_dangerous_deserialization=True)

    # chain to link everything together
    # using the create_retrieval_chain function which recieves as the first argument the vector store but we use it as a retriever
    # when we run the function, Langchain uses this retriever to find relevant documents to the original query
    # fetched documents are then piped into the create_stuff_documents_chain function
    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    stuff_docs = create_stuff_documents_chain(llm=ChatOpenAI(temperature=0), prompt=retrieval_qa_chat_prompt)
    retrieval_chain = create_retrieval_chain(new_vectorstore.as_retriever(), stuff_docs)

    res = retrieval_chain.invoke({"input": "What is the gist of ReACT in 3 sentences?"})
    print(res)
