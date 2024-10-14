from stackit.core.configuration import Configuration

"""
The configuration class will fetch all environment variables during initialization.
If no region is defined, it will use the default region of a service.
"""
config = Configuration()
print(vars(config))  # Will print out the values of all environment variables
