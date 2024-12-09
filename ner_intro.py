from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import torch

model_id = "dslim/bert-base-NER"

tokenizer = AutoTokenizer.from_pretrained(model_id)

ner_model = AutoModelForTokenClassification.from_pretrained(model_id)
# print(ner_model)
device = 'cpu'

nlp = pipeline('ner',
                model = ner_model,
                tokenizer = tokenizer,
                aggregation_strategy='max',
                device=None)

print(nlp('My name is Sanad, i work at Juniper Networks'))

