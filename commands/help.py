from utils.format_message import InlineFormatter


def help() -> str:
    commands = [
        {"command": "[INFO]", "params": "Available commands:\n", "desc": "", "tag_color": "cyan", "param_color": "red", "desc_color": "white"},
        
        {"command": "hello", "params": "", "desc": "- Greet the bot"},

        {
            "command": "add",
            "params": "<name> <phone> | <name> note <text> | <name> tag <note_id> <tag>",
            "desc": "- Adds a new contact or updates an existing one:\n"
            " - <name> <phone>: add a phone number to the contact\n"
            "- <name> note <text>: add a note to the contact\n"
            "- <name> tag <note_id> <tag>: add a tag to a specific note by ID"
        
        },
        {
            "command": "change",
            "params": "<name> <old_phone> <new_phone> | <name> <property> <old_value> <new_value>",
            "desc": "- Updates contact information:\n"
            "- <old_phone> <new_phone>: replaces a phone number\n"
            "- <property> <old_value> <new_value>: updates a property (name, note, email, birthday, or address)"
        },

        {
            "command": "delete",
            "params": "<name> | <name> <property> | <name> <property> <value>",
            "desc": "- Deletes a contact or a specific item from it:\n"
            "- <name>: removes the entire contact\n"
            "- <property>: removes a single-value field (birthday, address, email)\n"
            "- <property> <value>: removes a specific phone or note by its number/index"
        },

        {
            "command": "find",
            "params": "<property> <value>",
            "desc": "- Searches for contacts by a specific property:\n"
            "- property: name | phone | birthday | email | address | tag | note-pattern\n"
            "- value: the value to search for (e.g. part of a note, a phone number, etc.)"
        },
        
        {
            "command": "find-notes",
            "params": "<name> <tag>",
             "desc": "- Finds and displays all notes for a contact that have the specified tag"
        },

        {
            "command": "birthdays",
            "params": "<days>",
            "desc": "- Shows contacts with upcoming birthdays within the next <days> days"
        },

        {   "command": "help", "params": "", "desc": "- Show this help message"},
        {   "command": "close", "params": "", "desc": "- Exit the bot"},
    ]

    lines = []
    for cmd in commands:
        tag = InlineFormatter(f"{cmd['command']:<12}").color(cmd.get("tag_color", "yellow")).format()
        params = InlineFormatter(f"{cmd['params']:<30}").color(cmd.get("param_color", "green")).format()
        desc = InlineFormatter(f"{cmd['desc']}").color(cmd.get("desc_color", "white")).format()

        lines.append(f"{tag} {params} {desc}\n")

    return "".join(lines)
