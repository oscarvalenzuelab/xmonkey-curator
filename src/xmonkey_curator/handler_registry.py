# handler_registry.py

from .base_handler import BaseFileHandler
from .handlers import TextFileHandler, ElfFileHandler
# Import other handlers as needed

HANDLER_REGISTRY = {
    'text/plain': TextFileHandler,
    'application/x-executable': ElfFileHandler,
    # Add more MIME type and handler class mappings here
}

def register_handler(mime_type, handler_class):
    """Registers a new handler for a given MIME type."""
    HANDLER_REGISTRY[mime_type] = handler_class

def get_handler(file_path, mime_type):
    """Returns an instance of the appropriate handler for the given MIME type."""
    handler_class = HANDLER_REGISTRY.get(mime_type, BaseFileHandler)
    return handler_class(file_path)