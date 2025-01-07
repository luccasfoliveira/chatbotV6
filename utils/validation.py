def is_valid_input(user_input: str) -> bool:
    valid_keywords = ["verdade", "fato", "confirmar"]
    return any(keyword in user_input.lower() for keyword in valid_keywords)
