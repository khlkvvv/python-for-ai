test_settings = {
    'theme':'dark',
    'notifications':'enabled',
    'volume':'high'
}
def add_setting(setting_dict, key_value):
    key = str(key_value[0]).lower()
    value = str(key_value[1]).lower()

    if key in setting_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        setting_dict[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(setting_dict, key_value):
    key = str(key_value[0]).lower()
    new_value = str(key_value[1]).lower()

    if key in setting_dict:
        setting_dict[key] = new_value
        return f"Setting '{key}' updated to '{new_value}' successfully!"
    else: 
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(setting_dict, key_value):
    key = str(key_value).lower()
    if key in setting_dict:
        del setting_dict[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(setting_dict):
    if not setting_dict:
        return "No settings available."
    
    output = "Current User Settings:\n"
    for key, value in setting_dict.items():
        output = output + f"{key.capitalize()}: {value}\n"
    return output
add_setting("Language", "english")