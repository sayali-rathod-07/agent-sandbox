def get_user_config():
    # Intentional Bug: This will raise a KeyError because 'theme' isn't in the dict
    settings = {"user": "Sayali", "status": "active"}
    print(f"Current theme: {settings.get('theme', 'default')}") 
    return settings

if __name__ == "__main__":
    get_user_config()
