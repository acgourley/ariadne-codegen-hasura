This repo only exists to show a slow import case of pydantic types. The `gql_client` dir was generated using ariadne-codegen pointed at a Hasura endpoint modeling an election and ballot items as part of a open government project. 


ariadne-codegen was run with these options on:

plugins = ["ariadne_codegen.contrib.client_forward_refs.ClientForwardRefsPlugin", "ariadne_codegen.contrib.no_reimports.NoReimportsPlugin"]

Although performance is similar with or without them. 