# Connection to "public" nodes

This solution is designed for non-technical users who may have difficulty configuring their own JSON-RPC node, or for those who do not want to waste their time repeating what others have done before and have made publicly available :-)

From the user's point of view, the solution is based on several JSON-RPC nodes made available by the Polis community to the users of the *Polis Masternode Tool* and *polismnb* apps. At the time of writing, these nodes are operated by Hans.

## Technical information

These nodes are based on the following components:
 * Polis daemon (*polisd*) processing JSON-RPC requests
 * *Nginx* web server, as a frontend serving SSL requests sent by the applications
 * A Lua script, as a broker between *nginx* and *polisd*

Configuration is based on ethereum-nginx-proxy, adapted to Polis requirements by @chaeplin: https://github.com/chaeplin/dash-ticker/tree/master/web/nginx

## Configuration

When version 0.9.5 or higher of the PMT application is run the first time, "public" connections will automatically be added to the configuration. Open PMT and click the `Configure` button. In the `Configuration` dialog you should see the following two connections:
 * https://seattle.polis.tools:443
 * https://frankfurt.polis.tools:443

![Public connection configuration window](img/pmt-config-dlg-public.png)

If you see connections and all three are checked (enabled) you don't need to do anything. If you see connections but they are not enabled, you just need to enable them. I also suggest deactivating all other connections, since these may be connections from an old configuration.

If any of the listed "predefined" nodes are missing or are incomplete, follow these steps:
 * Select all the text from the block below and copy to the clipboard (do not miss the square brackets at the beginning and the end of the text), for Polis MAINNET:
```﻿
[
    {
        "use_ssh_tunnel": false,
        "host": "seattle.polis.tools",
        "port": "443",
        "username": "pmtuser",
        "password": "67414141414142647168396b4832714d6f58632d6959734c44535864444e656872794b52366c53693867727847753173516e5971625358303933584c68776975387942695259724e5f3456722d5532573363524266395262706c4241735a637669513d3d",
        "use_ssl": true
    },
    {
        "use_ssh_tunnel": false,
        "host": "frankfurt.polis.tools",
        "port": "443",
        "username": "pmtuser",
        "password": "67414141414142647168396b69646b31692d784d37717a7442323534724d2d434e375650512d486f5432657267394e6e656e6f48545f50692d797831626c433142495a785f3862675855394c496e706e4c3264672d436d63724c3731702d637433673d3d",
        "use_ssl": true
    }
]
```

 * Right-click on the `Connections` box.
 * From the popup menu choose the `Paste connection(s) from cliboard` action:
    ![Paste connections from clipboard](img/pmt-config-dlg-public-recover.png)
 * Click `Yes` to the question whether you want to import connections.

All three connections should then be added to the configuration.

## Security

To perform its job, the application must send some data to the JSON-RPC node that may be perceived as sensitive. Specifically, these are the client's IP address and the JSON-RPC commands themselves, with their respective arguments.

For example, the action initiated by the `Get status` button sends the following data to the node:
```python
{"version": "1.1", "id": 2, "params": ["full", "19e7eba493a026f205078469566e4df6a5a4b1428965574b55bec2412ddc9c48-0"], "method": "masternodelist"}
```

To maximize user anonymity, all three published nodes have disabled logging of any information related to JSON-RPC commands. The logging configuration is exactly the same as the example scripts provided by @chaeplin here: [https://github.com/chaeplin/dash-ticker/tree/master/web/nginx](https://github.com/chaeplin/dash-ticker/tree/master/web/nginx).

Despite this, if you would prefer not to risk sharing this information, it is suggested to disable the configuration options for the "public" nodes and choose a different type of connection:

- [Connection to a local Polis daemon](config-connection-direct.md)
- [Connection to a remote Polis daemon through an SSH tunnel](config-connection-ssh.md)
