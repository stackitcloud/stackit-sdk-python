[![GitHub License](https://img.shields.io/github/license/stackitcloud/stackit-sdk-go)](https://www.apache.org/licenses/LICENSE-2.0)

# Overview

This repository contains the published Python SDKs and releases.
The modules are structured into a core module with service clients, authentication and shared functionality as well as the different STACKIT services.
The usage of the SDK is shown in some examples.

# Getting started

The SDK is structured into several packages, each of them implementing the REST client for a service.
To use a specific service, you can install it as:

```bash
pip install stackit-redis
```

It will pull all needed dependencies automatically, so you can use the package right away.

To use all services, you can install the whole SDK with a single package:

```bash
pip install stackit
```

This allows you to use any services that the SDK offers.


## Installation from source

You can also install the packages from source by replacing the package-name by the path to the code.
The path can be local, but can also point to a git-repository. For an installation using local code from the root folder of the repository this can look like the following:
```bash
pip install services/<service-name>
```
Where `<service-name>` has to be replaced by the name of the service you want to install.
For `redis` the command would be:
```bash
pip install services/redis
```
If you want to install all services you can use the `Makefile` with the following command:
```bash
make install
```

> ⓘ INFO: The STACKIT Python SDK requires the STACKIT Python core package to be installed.
> The STACKIT Python SDK package, as well as the accompanying installation instructions, can be found [here](https://github.com/stackitcloud/stackit-sdk-python-core).


# Examples

You can find several examples on how to use the SDK and also on how to configure the SDK to use your own custom implementation (to set proxies or implement a more fine-grained retry behaviour) in the [examples folder](/examples).

There are also several examples for each service to help you get started right away.
The only thing you need is a STACKIT account and valid credentials.

## Authorization

To authenticate to the SDK, you will need a [service account](https://docs.stackit.cloud/stackit/en/service-accounts-134415819.html). Create it in the STACKIT Portal an assign it the necessary permissions, e.g. `project.owner`.

There are multiple ways to authenticate:

- Key flow (recommended)
- Token flow

When setting up authentication, the SDK will always try to use the key flow first and search for credentials in several locations, following a specific order:

1. Explicit configuration, e.g. by using the option `Configuration(service_account_key_path="path/to/sa_key.json")`
2. Environment variable, e.g. by setting `STACKIT_SERVICE_ACCOUNT_KEY_PATH`
3. Credentials file

   The SDK will check the credentials file located in the path defined by the `STACKIT_CREDENTIALS_PATH` env var, if specified,
   or in `$HOME/.stackit/credentials.json` as a fallback.
   The credentials file should be a json and each credential should be set using the name of the respective environment variable, as stated below in each flow. Example:

   ```json
   {
     "STACKIT_SERVICE_ACCOUNT_TOKEN": "foo_token",
     "STACKIT_SERVICE_ACCOUNT_KEY_PATH": "path/to/sa_key.json"
   }
   ```

Check the [authentication example](examples/authentication/basic_authentication.py) for more details.

### Key flow

The following instructions assume that you have created a service account and assigned it the necessary permissions, e.g. `project.owner`.

To use the key flow, you need to have a service account key, which must have an RSA key-pair attached to it.

When creating the service account key, a new pair can be created automatically, which will be included in the service account key.
This will make it much easier to configure the key flow authentication in the CLI, by just providing the service account key.

> **Optionally**, you can provide your own private key when creating the service account key, which will then require you to also provide it explicitly to the CLI, additionally to the service account key.
> Check the STACKIT Knowledge Base for an [example of how to create your own key-pair](https://docs.stackit.cloud/stackit/en/usage-of-the-service-account-keys-in-stackit-175112464.html#UsageoftheserviceaccountkeysinSTACKIT-CreatinganRSAkey-pair).

To configure the key flow, follow this steps:

1. Create a service account key:
    - Use the STACKIT Portal: go to the `Service Accounts` tab, choose a `Service Account` and go to `Service Account Keys` to create a key. For more details, see [Create a service account key](https://docs.stackit.cloud/stackit/en/create-a-service-account-key-175112456.html).
2. Save the content of the service account key by copying it and saving it in a JSON file. The expected format of the service account key is **JSON** with the following structure:

    ```json
    {
      "id": "uuid",
      "publicKey": "public key",
      "createdAt": "2023-08-24T14:15:22Z",
      "validUntil": "2023-08-24T14:15:22Z",
      "keyType": "USER_MANAGED",
      "keyOrigin": "USER_PROVIDED",
      "keyAlgorithm": "RSA_2048",
      "active": true,
      "credentials": {
        "kid": "string",
        "iss": "my-sa@sa.stackit.cloud",
        "sub": "uuid",
        "aud": "string",
        "privateKey": "(OPTIONAL) private key when generated by the SA service"
      }
    }
    ```

3. Configure the service account key for authentication in the SDK by following one of the alternatives below:
   - using the configuration options:
     ```python
     config = Configuration(
        ...
        service_account_key_path="/path/to/service_account_key.json"
        ...
     )
     ```
   - setting the environment variable: `STACKIT_SERVICE_ACCOUNT_KEY_PATH`
   - setting `STACKIT_SERVICE_ACCOUNT_KEY_PATH` in the credentials file (see above)

> **Optionally, only if you have provided your own RSA key-pair when creating the service account key**, you also need to configure your private key (takes precedence over the one included in the service account key, if present). **The private key must be PEM encoded** and can be provided using one of the options below:
>
> - using the configuration options:
>   ```python
>   config = Configuration(
>       ...
>       private_key_path="/path/to/private_key.json"
>       ...
>   )
>   ```
> - setting the environment variable: `STACKIT_PRIVATE_KEY_PATH`
> - setting `STACKIT_PRIVATE_KEY_PATH` in the credentials file (see above)

4. The SDK will search for the keys and, if valid, will use them to get access and refresh tokens which will be used to authenticate all the requests.

### Token flow

Using this flow is less secure since the token is long-lived. You can provide the token in several ways:

1. Using the configuration option:
    ```python
    config = Configuration(
       ...
       service_account_token="your token"
       ...
    )
    ```
2. Setting the environment variable `STACKIT_SERVICE_ACCOUNT_TOKEN`
3. Setting it in the credentials file (see above)

## Reporting issues

If you encounter any issues or have suggestions for improvements, please open an issue in the repository or create a ticket in the [STACKIT Help Center](https://support.stackit.cloud/).

## Contribute

### Installing in editable mode
For development it is best to install in editable mode.
You can install a single package in editable mode using the following command:
```bash
pip install -e services/<service-name>
```
Where `<service-name>` has to be replaced by the name of the service you want to install.
For `redis` the command would be:
```bash
pip install -e services/redis
```
If you want to install all services in editable mode you can use the `Makefile` with the following command:
```bash
make install-dev
```
## License

Apache 2.0
