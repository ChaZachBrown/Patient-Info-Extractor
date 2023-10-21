""" This was a test to try and create an advanced agent that the user could talk to and have extract patient data.
    More time was needed to get this to work and was not needed for core functionality """


# import datetime
# import json
# import os
#
# import sqlalchemy
# from langchain import PromptTemplate
# from langchain.agents import initialize_agent, AgentType
# from langchain.chat_models import ChatOpenAI
# from langchain.llms import HuggingFaceEndpoint
# from langchain.memory import ConversationBufferMemory, ConversationTokenBufferMemory
# from langchain.schema import SystemMessage
# from langchain.tools import Tool, StructuredTool
# from pydantic import BaseModel, Field
#
#
#
# HUGGING_FACE_KEY = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
#
# imported_patient_info = ""
# with open('C:/Users/Chaza/Documents/Langchain/patientInfo/database/doctorVisit.txt', 'r') as file:
#     imported_patient_info = file.read()
#
# class InfoAgent(BasePatientTools):
#
#     open_ai_llm = ChatOpenAI(temperature=.3, model_name="gpt-3.5-turbo")
#
#     endpoint_url = "https://yyolen6rrlt1acst.us-east-1.aws.endpoints.huggingface.cloud"
#     hf = HuggingFaceEndpoint(
#         endpoint_url=endpoint_url,
#         huggingfacehub_api_token=HUGGING_FACE_KEY,
#         task="text-generation",
#     )
#
#     # class SearchInput(BaseModel):
#     #     patient_name: str = Field(description="should be a patients name")
#
#     tools_for_agent = [
#         # StructuredTool.from_function(BasePatientTools.import_patient_data)
#         # Tool(
#         #     name="Import patient data",
#         #     func=BasePatientTools.import_patient_data,
#         #     description="Useful for when you need import new data for a specific patient",
#         #     # args_schema=SearchInput
#         # )
#     ]
#     system_message = SystemMessage(
#         content=(
#             "You are a helpful assistant that re-writes the user's text to "
#             "sound more upbeat."
#         )
#     ),
#     memory = ConversationTokenBufferMemory(
#         llm=open_ai_llm, memory_key="chat_history", max_token_limit=4000
#     )
#     agent_chain = initialize_agent(
#         tools=tools_for_agent,
#         llm=open_ai_llm,
#         agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
#         verbose=True,
#         memory=memory,
#         agent_kwargs={"system_message": system_message}
#     )
#
#     # patient_info = None
#
#     def run_agent(self, user_input):
#         if imported_patient_info:
#             patient = self.get_patient_by_name("John")
#             template = """Patient's structured data from the Database: ({patient_DB_data})
#              Patient's unstructed data that was imported: ({patient_imported_data})
#              ________________________________________
#              New user query: {user_input}"""
#             # template = """{name_of_person}. my name is zach"""
#
#             prompt_template = PromptTemplate(
#                 template=template, input_variables=["patient_DB_data", "patient_imported_data", "user_input"]
#             )
#
#             response = self.agent_chain.run(input=prompt_template.format_prompt(
#                 patient_DB_data=json.dumps(patient.__dict__, default=lambda x: x.isoformat() if isinstance(x, (datetime.date, datetime.datetime)) else None, indent=4),
#                 patient_imported_data=imported_patient_info,
#                 user_input=user_input))
#             return response
#             # return self.agent_chain.run(input=user_input)
#         else:
#             return self.agent_chain.run(input=user_input)
