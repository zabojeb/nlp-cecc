import re


def extract_context(text, aspect):
    # Разбиваем текст на предложения
    sentences = re.split(r'(?<=[.!?]) +', text)

    # Найдем индексы предложений, содержащих аспект
    aspect_indices = [i for i, sentence in enumerate(sentences) if aspect in sentence]

    # Выбираем предложения вокруг найденных аспектов
    context_sentences = []
    for index in aspect_indices:
        start_index = max(0, index - 2)
        end_index = min(len(sentences), index + 2)
        context_sentences.extend(sentences[start_index:end_index])

    # Объединяем выбранные предложения в один текст
    context_text = ' '.join(context_sentences)

    return context_text