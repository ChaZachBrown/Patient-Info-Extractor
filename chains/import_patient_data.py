import json
import os

from langchain import LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.llms import HuggingFaceEndpoint
from database_tools import save_patient_from_json

""" OpenAI gpt-3 and Open Source LLM Interface """

HUGGING_FACE_KEY = os.environ.get("HUGGINGFACEHUB_API_TOKEN")


def parse_result_save_data(LLM_result):
    patient_data = json.loads(LLM_result)
    save_patient_from_json(patient_data)


def parse_data(template_file_path):
    open_ai_llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    endpoint_url = ""
    # hf = HuggingFaceEndpoint(
    #     endpoint_url=endpoint_url,
    #     huggingfacehub_api_token=HUGGING_FACE_KEY,
    #     task="text-generation",
    # )

    with open(template_file_path, 'r', encoding='utf-8') as file:
        parse_data_template = file.read()

    parse_data_prompt_template = PromptTemplate(
        input_variables=["patient_data"],
        template=parse_data_template,
    )

    chain = LLMChain(llm=open_ai_llm, prompt=parse_data_prompt_template)

    result = chain.run(patient_data="")

    parse_result_save_data(result)

    return result

