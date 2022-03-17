from scalecodec.base import RuntimeConfigurationObject, ScaleBytes
from scalecodec.type_registry import load_type_registry_preset
import json

runtime_config = RuntimeConfigurationObject()
runtime_config.update_type_registry(load_type_registry_preset(name="metadata_types"))

def decode_event_data(event_data: str):
    metadata = runtime_config.create_scale_object(
            'MetadataVersioned', data=ScaleBytes(event_data)
     )   

    return json.dumps(metadata.decode()[1], indent=4, sort_keys=True)



