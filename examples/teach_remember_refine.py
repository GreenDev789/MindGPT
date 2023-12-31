from mindgpt.helper import PythonREPL
from mindgpt.llm import MindGPT
from examples.knowledge_base import knowledge

llm = MindGPT(model_name="gpt-3.5-turbo", verbose=False)

llm.memorize(knowledge)

task = 'generate python code that uses langchain to send a request to OpenAI LLM and ask it suggest 3 recipes using gpt-4 model, Only give the code between `` and nothing else'

code = llm.predict(task, remember=llm.remember(task, limit=10, sort_by_order=True))
output, error = PythonREPL().run(code.strip('`'))
if error:
    print('found an error to be refined:', error)
    code = llm.refine(
        code,
        instruction_hint='Fix the provided code. Only print the fixed code between `` and nothing else.',
        critics=[error],
    )
print(code)
