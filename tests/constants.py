import os

EXAMPLE_FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'examples', 'indiana-example.csv')
VALID_FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'examples', 'valid-template-1.3.1.csv')
INVALID_FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'examples', 'invalid-template-1.3.1.csv')
INVALID_CONTENT_FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'examples', 'invalid-content-template-1.3.1.csv')
TEMPLATE_RECORD_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates', 'min-template.xml')