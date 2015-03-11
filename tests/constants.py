import os

EXAMPLE_FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'examples', 'indiana-example.csv')
ADJUSTED_EXAMPLE_FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'examples', 'adjusted-indiana-example.csv')
VALID_FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'examples', 'valid-template-1.3.1.csv')
INVALID_FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'examples', 'invalid-template-1.3.1.csv')
INVALID_CONTENT_FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'examples', 'invalid-content-template-1.3.1.csv')
TEMPLATE_RECORD_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates', 'min-template.xml')
SIMPLE_TRANSFORMER_FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'examples', 'simple-transformer.xslt')
SIMPLE_TRANSFORM_INPUT_FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'examples', 'simple-transform-input.xml')
OUTPUT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'outputs')