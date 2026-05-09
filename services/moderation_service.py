import re
from config import BLACKLIST_WORDS

OFF_TOPIC_PATTERNS = [
    r'\b(receita|futebol|novela|jogo|game|música|filme|série)\b',
    r'\b(namorad|noivad|casament)\b',
]

def is_inappropriate(text):
    # type: (str) -> bool
    for word in BLACKLIST_WORDS:
        pattern = r'\b' + re.escape(word.lower()) + r'\b'
        if re.search(pattern, text.lower()):
            return True

    for pattern in OFF_TOPIC_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return True

    return False