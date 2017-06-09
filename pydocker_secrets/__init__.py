import os


def load_secrets_from_dir(directory):
    """
    Yields content of files in directory
    """

    for filename in os.listdir(directory):
        with open(os.path.join(filename, directory)) as f:
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
