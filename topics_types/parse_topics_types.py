import os
import inspect
import importlib.util

# Specificera bas-klassen du vill hitta arvtagare till
BASE_CLASS_NAME = 'mqtt_leaf_topic'

def is_subclass_of_base_class(obj, base_class):
    """Kontrollera om ett objekt är en subclass av bas-klassen."""
    return inspect.isclass(obj) and issubclass(obj, base_class) and obj is not base_class

def find_subclasses(base_class_name, directory):
    """Hitta alla klasser som ärver från bas-klassen i alla moduler i ett visst katalog."""
    subclasses = []
    base_class = None

    # Gå igenom alla Python-filer i katalogen
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                module_path = os.path.join(root, file)
                module_name = os.path.splitext(os.path.relpath(module_path, directory))[0].replace(os.sep, '.')

                # Ladda modulen dynamiskt
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                try:
                    spec.loader.exec_module(module)
                except Exception as e:
                    print(f"Kan inte ladda modulen {module_name}: {e}")
                    continue

                # Hitta bas-klassen om vi inte redan har gjort det
                if base_class is None and hasattr(module, base_class_name):
                    base_class = getattr(module, base_class_name)

                # Inspektera alla medlemmar i modulen
                for name, obj in inspect.getmembers(module):
                    if is_subclass_of_base_class(obj, base_class):
                        subclasses.append(obj)

    return subclasses

def get_all_topic_typed():
    # Specificera sökkatalogen
    path = os.path.abspath(__file__)
    search_directory = os.path.dirname(path)
    #search_directory = 'path/to/your/project'

    subclasses = find_subclasses(BASE_CLASS_NAME, search_directory)
    if subclasses:
        print(f"Följande klasser ärver från {BASE_CLASS_NAME}:")
        for subclass in subclasses:
            print(subclass.__name__)
    else:
        print(f"Inga klasser som ärver från {BASE_CLASS_NAME} hittades.")

    return subclasses