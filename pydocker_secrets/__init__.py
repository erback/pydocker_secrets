import os
def load_secrets_from_dir(directory='/var/run/secrets/'):
    """
    Yields content of files in directory
    """
    for filename in os.listdir(directory):
        with open("%s%s" % (directory, filename)) as f:
            yield filename, f.read().strip()

def get_secrets():
    """
    Loads secrets into dict
    """
    secrets = {}
    for filename, secret in load_secrets_from_dir():
        secrets[filename] = secret
    return secrets
