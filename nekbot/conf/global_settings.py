PLUGIN_AUTHOR_NAME = 'Your name'
PLUGIN_AUTHOR_EMAIL = 'your@email'
PLUGIN_AUTHOR_WEBSITE = 'https://yourwebsite'

STORAGE_DIR = 'storage'

PERMISSIONS_TREE = {
    'root': ['admin'],
    'admin': ['execution'],
    'execution': []
}

PROTOCOLS = [
]

PLUGINS = [
    'bot',
    'hello',
]

PERMS_METHODS = [
    'nekbot.core.permissions.perms_from_settings',
]

SYMBOL = '!'