# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for
# full license information.

import json
from azureml.core import Workspace, Model, VERSION
from azureml.core.authentication import ServicePrincipalAuthentication

print(VERSION)

with open("aml/config.json", "r") as f:
    config = json.load(f)

auth = ServicePrincipalAuthentication(
    config["tenant_id"],
    config["service_principal_id"],
    config["service_principal_password"]
)

ws = Workspace.create(
    name=config["workspace_name"],
    auth=auth,
    subscription_id=config['subscription_id'],
    resource_group=config['resource_group'],
    location=config['location']
    exist_ok=True,
    show_output=True,
)

Model.register(ws, 'models/TinyYOLO.onnx', 'TinyYOLO')