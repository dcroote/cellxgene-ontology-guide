import os

PACKAGE_ROOT = os.path.dirname(os.path.realpath(__file__))
RAW_ONTOLOGY_DIR = os.path.join(PACKAGE_ROOT, "raw-files")
PROJECT_ROOT_DIR = os.path.realpath(__file__).rsplit("/", maxsplit=4)[0]
ONTO_INFO_YAML = os.path.join(PROJECT_ROOT_DIR, "ontology_info.yml")
PARSED_ONTOLOGIES_FILE = os.path.join(PROJECT_ROOT_DIR, "all_ontology.json.gz")
SCHEMA_DIR = os.path.join(PROJECT_ROOT_DIR, "artifact-schemas")
ONTOLOGY_ASSETS_DIR = os.path.join(PROJECT_ROOT_DIR, "ontology-assets")
