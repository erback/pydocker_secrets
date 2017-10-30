import os


def load_secrets_from_dir(directory):
    """
    Yields content of files in directory
    """

    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename)) as f:
            # Yield the filename on the format "UPPER_UNDERSCORE" instead of "lower-dash"
            yield filename.replace('-', '_').upper(), f.read().strip()


def get_secrets(directory='/var/run/secrets/'):
    """
    Loads secrets into dict
    """
    secrets = {}

    if not os.path.exists(directory):
        return secrets

    for filename, secret in load_secrets_from_dir(directory):
        secrets[filename] = secret
    return secrets


def get_secret_or_load_from_env(key, secrets, default=None):
    """
    Tries to load from secrets dict else load from env
    """

    ret_val = secrets.get(key)

    if ret_val:
        return ret_val

    return os.environ.get('key', default)

