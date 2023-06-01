import os
import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

def run_tweet_analysis(external_data) -> None:
    os.environ['OPENAI_API_KEY'] = API_KEY
    # os.environ['OPENAI_API_KEY'] = API_KEY

    # App Framework
    st.title('🦜️🔗 Twitter tweet analysis (GPT) - Twitter')
    # prompt = st.text_input('Type in your Twitter username')
    # make 'prompt' accessible to other module. Define as variable
    writings = external_data
    # prompt =

    # prompt template 
    # title_template = PromptTemplate(input_variables = ['topic'], template = 'What ideas and topics are  {topic}')
    analysis_template = PromptTemplate(input_variables = ['writings'], template = 'You are an excellent literature specialist. These sentences are the personal essays and tweets written by the author. What ideas and topics are present in these writings? Are there any themes or repeated motifs? For example, politics, sports, depression, parties etc. What categories of discouse are identifiable in these writings? Present your analysis in an expository tone, inviting the author to discover insights. Leverage these WRITINGS: {writings}')

    # Memory 
    # title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
    analysis_memory = ConversationBufferMemory(input_key='writings', memory_key='chat_history')

    # LLMs 
    llm = OpenAI(temperature=0.9)
    # title_chain = LLMChain(llm=llm, prompt=title_template, verbose = True, output_key='title', memory=title_memory)
    analysis_chain = LLMChain(llm=llm, prompt=analysis_template, verbose = True, output_key='analysis', memory=analysis_memory)
    # sequential_chain = SimpleSequentialChain(chains=[title_chain, script_chain], verbose = True)
    # sequential_chain = SequentialChain(
    #     chains=[title_chain, script_chain],
    #     input_variables=['topic'],
    #     output_variables=['title', 'script'],
    #     verbose = True)
    # wiki = WikipediaAPIWrapper()
    

    # Display response if there is a prompt 
    if writings:
        # title = title_chain.run(prompt)
        # wiki_research = wiki.run(prompt)
        analysis = analysis_chain.run(writings = writings)
        # st.write(title)
        st.write(analysis)

        # with st.expander('Title History'):
        #     st.info(title_memory.buffer)

        with st.expander('SCript History'):
            st.info(script_memory.buffer)
        with st.expander('Wikipedia Research'):
            st.info(wiki)


# # App Framework
# st.title('🦜️🔗 Youtube Script generator (GPT)')
# prompt = st.text_input('Type in your prompt')

# # prompt template 
# title_template = PromptTemplate(input_variables = ['topic'], template = 'write me a youtube video title about {topic}')
# script_template = PromptTemplate(input_variables = ['title', 'wiki_research'], template = 'write me a youtube video script based on this title. TITLE: {title} while leveraging this wikipedia research: {wiki_research}')

# # Memory 
# title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
# script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')

# # LLMs 
# llm = OpenAI(temperature=0.9)
# title_chain = LLMChain(llm=llm, prompt=title_template, verbose = True, output_key='title', memory=title_memory)
# script_chain = LLMChain(llm=llm, prompt=script_template, verbose = True, output_key='script', memory=script_memory)
# # sequential_chain = SimpleSequentialChain(chains=[title_chain, script_chain], verbose = True)
# # sequential_chain = SequentialChain(
# #     chains=[title_chain, script_chain],
# #     input_variables=['topic'],
# #     output_variables=['title', 'script'],
# #     verbose = True)
# wiki = WikipediaAPIWrapper()

# # Display response if there is a prompt 
# if prompt:
#     title = title_chain.run(prompt)
#     wiki_research = wiki.run(prompt)
#     script = script_chain.run(title=title, wiki_research=wiki)
#     st.write(title)
#     st.write(script)
#     # response = llm(prompt)
#     # response = title_chain.run(topic=prompt)
#     # response = sequential_chain.run(prompt)
#     # st.write(response)
#     # response = sequential_chain({'topic': prompt})
#     # st.write(response['title'])
#     # st.write(response['script'])

#     with st.expander('Title History'):
#         st.info(title_memory.buffer)

#     with st.expander('SCript History'):
#         st.info(script_memory.buffer)
#     with st.expander('Wikipedia Research'):
#         st.info(wiki)


# =====


# # SimpleSequentialChain 
# # App Framework
# st.title(' Youtube GPT Creator')
# prompt = st.text_input('Type in your prompt')

# # prompt template 
# title_template = PromptTemplate(
#     input_variables = ['topic'],
#     template = 'write me a youtube video title about {topic}'
# )

# script_template = PromptTemplate(
#     input_variables = ['title'],
#     template = 'write me a youtube video script based on this title. TITLE: {title}'
# )

# # LLMs 
# llm = OpenAI(temperature=0.9)
# title_chain = LLMChain(llm=llm, prompt=title_template, verbose = True)
# script_chain = LLMChain(llm=llm, prompt=script_template, verbose = True)
# sequential_chain = SimpleSequentialChain(chains=[title_chain, script_chain], verbose = True)


# # Display response if there is a prompt 
# if prompt:
#     # response = llm(prompt)
#     # response = title_chain.run(topic=prompt)
#     response = sequential_chain.run(prompt)
#     st.write(response)
