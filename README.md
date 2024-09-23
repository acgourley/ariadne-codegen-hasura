# Background

This repo only exists to show a slow import case of pydantic types. The `gql_client` dir was generated using ariadne-codegen pointed at a Hasura endpoint modeling an election and ballot items as part of a open government project. 

ariadne-codegen was run with these options on:

plugins = ["ariadne_codegen.contrib.client_forward_refs.ClientForwardRefsPlugin", "ariadne_codegen.contrib.no_reimports.NoReimportsPlugin"]

Although performance is similar with or without them. 

# Install

`poetry install`

# Running Benchmark

`poetry run python3 main.py`

Which on a M2 Mac will output:

```
Import times:
gql_client.client: 0.141862 seconds
gql_client.enums: 0.004654 seconds
gql_client.input_types: 3.033241 seconds
```

(or over 3x longer if in debug mode!)