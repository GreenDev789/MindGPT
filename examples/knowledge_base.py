knowledge = [
    """
LangChain is a python framework for developing applications powered by language models.
    """,
    """
Langchain offers the OpenAI class, use it when you want to send a request to OpenAI LLMs
    """,
    """
You can import OpenAI class from langchain like this: from langchain.llms import OpenAI
    """,
    """
Use the OpenAI class like so:
llm = OpenAI(model_name="text-ada-001", n=2, best_of=2
llm("Tell me a joke"
'Why did the chicken cross the road? To get to the other side.'
    """,
    """
Available model names in open ai: "text-ada-001", "gpt-3.5-turbo", "gpt-4"
    """,
    """
something else that you will almost never need
    """,
    """
DocArray allows you to represent your data, in an ML-native way. Put simply, DocArray lets you represent your data in a dataclass-like way, with ML as a first class citizen
    """,
    """
Generate a DocARray v2 schema:
from docarray import BaseDoc
from docarray.typing import TorchTensor, ImageUrl

# Define your data model
class MyDocument(BaseDoc:
    description: str
    image_url: ImageUrl  # could also be VideoUrl, AudioUrl, etc.
    image_tensor: TorchTensor[1704, 2272, 3]  # you can express tensor shapes!
    """,
    """
MindGPT is a library to prompt LLMs to perform thinking actions
    """,
    """
import MindGPT from MindGPT: from MindGPT.llm import MindGPT
    """,
    """
instantiate an llm instance from MindGPT: llm = MindGPT(model_name="gpt-3.5-turbo")
    """,
    """
memorize information: llm.memorize('DocArray V2 allows you to represent your data, in an ML-native way')
    """,
    """
Finally predict with the memory: llm.predict('write python code about DocArray v2', remember=llm.remember('DocArray V2'))
    """
]

