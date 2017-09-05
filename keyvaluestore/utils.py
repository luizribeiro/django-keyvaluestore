from keyvaluestore.models import KeyValueStore

def get_value_for_key(key):
    return KeyValueStore.objects.get_value_for_key(key)


def get_value_or_default(key, default):
    try:
        value = get_value_for_key(key)
    except KeyError:
        value = default
    return value


def set_key_value(key, value):
    KeyValueStore.objects.update_or_create(key=key, defaults={'value': value})
    return True
