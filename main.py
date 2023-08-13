import os

from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain
# from langchain.memory import ConversationBufferMemory
# from langchain.utilities import WikipediaAPIWrapper

from langchain.prompts.chat import HumanMessagePromptTemplate, ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser

from langchain.chains.api import open_meteo_docs
from langchain.chains import APIChain


class Country(BaseModel):
    capital: str = Field(description="capital of the country")
    name: str = Field(description="name of the country")

load_dotenv()



OPENAI_MODEL = "gpt-3.5-turbo"
# OPENAI_MODEL = "gpt-4"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
PROMPT_COUNTRY_INFO = """Provide information about {country}.{format_instructions}. If the country is doesn't exist, make up a response."""

# using prompt and chat llm model 
def main():
    # llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL)
    parser = PydanticOutputParser(pydantic_object=Country)
    country = input("Enter the name of a country: ")
    
    message = HumanMessagePromptTemplate.from_template(template=PROMPT_COUNTRY_INFO)
    chat_prompt = ChatPromptTemplate.from_messages(messages=[message])
    chat_prompt_with_values = chat_prompt.format_prompt(country=country, format_instructions=parser.get_format_instructions())
    try:
        # result = llm.predict(
        #     "Give me 5 topics for interesting YouTube videos about Python"
        #     )
        # print(result)
        response = llm(chat_prompt_with_values.to_messages())
        # print(response)
        data = parser.parse(response.content)
        # print(data)
        print(f"The capital of {data.name} is {data.capital}")
    except Exception as e:
        print(f"Failure to fetch response: {e}")

# using API chain 
# def main():
#     llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL)

#     chain_new = APIChain.from_llm_and_api_docs(
#         llm, open_meteo_docs.OPEN_METEO_DOCS, verbose=False
#     )
#     result = chain_new.run(
#         "What is the weather like right now in Lagos, Nigeria, in degrees Celsius"
#     )
#     print(result)


if __name__ == "__main__":
    main()