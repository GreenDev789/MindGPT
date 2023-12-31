from mindgpt.llm import MindGPT

llm = MindGPT(model_name="gpt-3.5-turbo")

rules = llm.abstract(observations=[
    "in tunisian, I did not eat is \"ma khditech\"",
    "I did not work is \"ma khdemtech\"",
    "I did not go is \"ma mchitech\"",
])
llm.memorize(rules)

llm.memorize("in tunisian, I studied is \"9rit\"")

task = "translate to Tunisian: I didn't study"
print(llm.predict(task, remember=llm.remember(task)))
