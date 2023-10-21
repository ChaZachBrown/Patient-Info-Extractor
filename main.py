import langchain
from chains.import_patient_data import parse_data

""" Main entry point for manual LLM response testing """

langchain.debug = True


test = parse_data('')

print(test)

