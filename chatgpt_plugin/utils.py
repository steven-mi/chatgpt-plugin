import json


def extract_json(text):
    """
    Extracts JSON from a string of text.
    :param text: A string of text that may contain JSON.
    :return: The first JSON object found in the text, or None if no JSON is found.
    """
    start = text.find('{')
    if start == -1:
        return None

    depth = 0
    for i in range(start, len(text)):
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(text[start:i + 1])
                except json.JSONDecodeError:
                    pass

    return None
