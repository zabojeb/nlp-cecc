from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from context_extracting import extract_context
from NER import get_companies
from parser import parse
from translator import translate

absa_model_name = "yangheng/deberta-v3-large-absa-v1.1"
absa_tokenizer = AutoTokenizer.from_pretrained(absa_model_name)
absa_model = AutoModelForSequenceClassification.from_pretrained(absa_model_name)

classifier = pipeline("text-classification", model=absa_model, tokenizer=absa_tokenizer)


def absa(text, aspect):
    return classifier(f'[CLS] {extract_context(text, aspect)} [SEP] {aspect} [SEP]')


def process_url(url):
    # 1. Parsing
    parsed_text = parse(url)['text']

    # 2. Translation
    translated_text = translate(parsed_text)

    # 3. NER
    companies = get_companies(translated_text)

    # 4. ABSA
    result = {}
    for company in companies:
        result[company] = absa(translated_text, company)[0]['label'].lower()

    return result
