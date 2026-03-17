from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "./college_model"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

prompt = "<s>[INST] Tell me about Abhay Krishna [/INST]"

inputs = tokenizer(prompt, return_tensors="pt")

output = model.generate(**inputs, max_new_tokens=80)

print(tokenizer.decode(output[0]))