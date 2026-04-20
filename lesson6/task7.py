def create_profile(name: str, **kwargs: str) -> dict:

    profile = {"name": name}
    for key, value in kwargs.items():
        profile[key] = value
    return profile



