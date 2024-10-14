from stackit.core.configuration import Configuration

"""
You can set your own custom endpoint here.
Be aware that this will override the default endpoint and the definition of a region does
not work.
"""
config = Configuration(custom_endpoint="https://postgresql.my-awesome-company.cloud/")
