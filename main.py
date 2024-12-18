import torch 
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments, GPT2Model, GPT2Tokenizer, set_seed

model_id = "meta-llama/Llama-3.2-1B"
device = "cuda" if torch.cuda.is_available() else "cpu"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
# pipe = pipeline("text-generation",
#                 model = model_id ,
#                 torch_dtype = torch.bfloat16,
#                 device_map = "auto")
model.to(device)
training_arguments = TrainingArguments(output_dir="./results", per_device_train_batch_size=4, num_train_epochs=3)
trainer = Trainer(model, args = training_arguments, train_dataset="")
trainer.train()

model.save_pretrained("./model")
tokenizer.save_pretrained("./tokenizer")