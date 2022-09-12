# Setup the CLI

**Find the Terminal Application**

First, open up the Terminal application. On Mac and Linux, Terminal is the default application to interact witht the CLI. It should come on the home page for Linux distributions like Ubuntu, but on Mac it is located in the "Other" folder.

<figure><img src="../.gitbook/assets/Screen Shot 2022-09-06 at 2.28.52 PM.png" alt=""><figcaption><p>Pinch your fingers together to get here</p></figcaption></figure>

<figure><img src="../.gitbook/assets/Screen Shot 2022-09-06 at 2.28.57 PM.png" alt=""><figcaption></figcaption></figure>

You can also click CMD + Spacebar to get to spotlight and then type in terminal and hit enter.

<figure><img src="../.gitbook/assets/Screen Shot 2022-09-06 at 2.31.17 PM.png" alt=""><figcaption></figcaption></figure>

**Practice Basic Commands**

To begin, type:

```
cd Downloads
```

Now you're in your downloads directory.&#x20;

<figure><img src="../.gitbook/assets/Screen Shot 2022-09-06 at 2.34.06 PM.png" alt=""><figcaption></figcaption></figure>

Now type:

```
cd ..
```

You should be back in your home directory.

<figure><img src="../.gitbook/assets/Screen Shot 2022-09-06 at 2.35.45 PM.png" alt=""><figcaption></figcaption></figure>

Feel free to explore the CLI as you wish, but now it's back to business. Let's install Akash through the CLI so we can interact with the blockchain.&#x20;

**Install Akash on MacOS (Automated)**

If you already have Homebrew installed, you can download an install script that we wrote [here](../install\_akash/install.py). Save it to your Desktop and name it install.py. Then enter:

```
cd Desktop
python3 install.py
```

**Note:** This script also configures your environment, so you can skip the "Configure Akash Environment" section.

**Install Akash on MacOS (Manual)**

If you don't have Homebrew installed, we'll need to do that first. To install Homebrew, enter:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then to install Akash, enter:

```
brew install ovrclk/tap/akash
akash version
```

You should see the output v0.16.3 (current Akash version) which tells you that the download was successful.

**Install Akash on Linux**

To install Akash on Linux, enter:

```
AKASH_VERSION="$(curl -s "https://raw.githubusercontent.com/ovrclk/net/master/mainnet/version.txt")"
curl https://raw.githubusercontent.com/ovrclk/akash/master/godownloader.sh | sh -s -- "v$AKASH_VERSION"
sudo mv ./bin/akash /usr/local/bin
akash version
```

You should see the output v0.16.3 (current Akash version) which tells you that the download was successful.

**Configure Akash Environment**

Now that we have Akash downloaded, let's use it. The full list of CLI commands specific to Akash can be found [here](https://github.com/ovrclk/docs/tree/ed6bc0143968bc6e4e92c26c5dad6427f048bc2d/cli). We'll start off by trying to query this [transaction](https://www.mintscan.io/akash/txs/ACF35CCBD4DA831471C77943994C9040E88E88069F6693B666B5F78880FBEB9A). Querying a transaction essentially means retrieving its information. The command to query a transaction is:

```
akash query tx [tx_hash]
```

So, enter the transaction hash from the link above and enter it into your terminal:

```
akash query tx ACF35CCBD4DA831471C77943994C9040E88E88069F6693B666B5F78880FBEB9A
```

<figure><img src="../.gitbook/assets/Screen Shot 2022-09-06 at 2.49.11 PM.png" alt=""><figcaption></figcaption></figure>

You should have received an error. What gives? I thought we had just downloaded the Akash software? Well, each session you also need to configure your environment prior to executing commands. This error message is telling us that we're trying to query our local environment, which has no blockchain data, and we need to connect to an external source to fetch the proper data.&#x20;

You can configure your environment manually, or you can run scripts to do it for you. To run our script, download it [here](../configure\_environment/configure\_environment.py). Save it to your Desktop and name it configure\_environment.py. Then run:

```
cd Desktop
python3 configure_environment.py
```

The query should now successfully go through and return a long output similar to this:

```
code: 0
codespace: ""
data: 0A2E0A2C2F616B6173682E6465706C6F796D656E742E763162657461322E4D7367436C6F73654465706C6F796D656E74
events:
- attributes:
  - index: true
    key: c3BlbmRlcg==
    value: YWthc2gxdGVnNW52bjk3cTBneXphcDdrZnprZDBwZDZqZW43Mmhna2twdGw=
  - index: true
    key: YW1vdW50
    value: ODYwNXVha3Q=
  type: coin_spent
- attributes:
  - index: true
    key: cmVjZWl2ZXI=
    value: YWthc2gxN3hwZnZha20yYW1nOTYyeWxzNmY4NHoza2VsbDhjNWxhenc4ajg=
  - index: true
    key: YW1vdW50
    value: ODYwNXVha3Q=
  type: coin_received
- attributes:
  - index: true
    key: cmVjaXBpZW50
    value: YWthc2gxN3hwZnZha20yYW1nOTYyeWxzNmY4NHoza2VsbDhjNWxhenc4ajg=
  - index: true
    key: c2VuZGVy
    value: YWthc2gxdGVnNW52bjk3cTBneXphcDdrZnprZDBwZDZqZW43Mmhna2twdGw=
  - index: true
    key: YW1vdW50
    value: ODYwNXVha3Q=
  type: transfer
- attributes:
  - index: true
    key: c2VuZGVy
    value: YWthc2gxdGVnNW52bjk3cTBneXphcDdrZnprZDBwZDZqZW43Mmhna2twdGw=
  type: message
- attributes:
  - index: true
    key: ZmVl
    value: ODYwNXVha3Q=
  type: tx
- attributes:
  - index: true
    key: YWNjX3NlcQ==
    value: YWthc2gxdGVnNW52bjk3cTBneXphcDdrZnprZDBwZDZqZW43Mmhna2twdGwvMTY=
  type: tx
- attributes:
  - index: true
    key: c2lnbmF0dXJl
    value: ZXAyMVIyaTd3UlRCaDVUUUlQU0d5K25hODdHUzg5RXlINExRZ1Q0VktDd3BWVkJ5RkFYeXZSVWppdjVLK1dhMEMyc0pwenJmVjdnTkYyNWhxcUw5NEE9PQ==
  type: tx
- attributes:
  - index: true
    key: YWN0aW9u
    value: L2FrYXNoLmRlcGxveW1lbnQudjFiZXRhMi5Nc2dDbG9zZURlcGxveW1lbnQ=
  type: message
- attributes:
  - index: true
    key: c3BlbmRlcg==
    value: YWthc2gxNHBwaHNzNzI2dGhwd3dzM3ljNDU4aGdndWZ5bm05eDc3bDRsMnU=
  - index: true
    key: YW1vdW50
    value: NDk5ODAwNnVha3Q=
  type: coin_spent
- attributes:
  - index: true
    key: cmVjZWl2ZXI=
    value: YWthc2gxdGVnNW52bjk3cTBneXphcDdrZnprZDBwZDZqZW43Mmhna2twdGw=
  - index: true
    key: YW1vdW50
    value: NDk5ODAwNnVha3Q=
  type: coin_received
- attributes:
  - index: true
    key: cmVjaXBpZW50
    value: YWthc2gxdGVnNW52bjk3cTBneXphcDdrZnprZDBwZDZqZW43Mmhna2twdGw=
  - index: true
    key: c2VuZGVy
    value: YWthc2gxNHBwaHNzNzI2dGhwd3dzM3ljNDU4aGdndWZ5bm05eDc3bDRsMnU=
  - index: true
    key: YW1vdW50
    value: NDk5ODAwNnVha3Q=
  type: transfer
- attributes:
  - index: true
    key: c2VuZGVy
    value: YWthc2gxNHBwaHNzNzI2dGhwd3dzM3ljNDU4aGdndWZ5bm05eDc3bDRsMnU=
  type: message
- attributes:
  - index: true
    key: c3BlbmRlcg==
    value: YWthc2gxNHBwaHNzNzI2dGhwd3dzM3ljNDU4aGdndWZ5bm05eDc3bDRsMnU=
  - index: true
    key: YW1vdW50
    value: MTk5M3Vha3Q=
  type: coin_spent
- attributes:
  - index: true
    key: cmVjZWl2ZXI=
    value: YWthc2gxeGZ6cXo1ejR4bXV0djlzeTdmMnN4aDhxc3plazRnZG1uN2pqajc=
  - index: true
    key: YW1vdW50
    value: MTk5M3Vha3Q=
  type: coin_received
- attributes:
  - index: true
    key: cmVjaXBpZW50
    value: YWthc2gxeGZ6cXo1ejR4bXV0djlzeTdmMnN4aDhxc3plazRnZG1uN2pqajc=
  - index: true
    key: c2VuZGVy
    value: YWthc2gxNHBwaHNzNzI2dGhwd3dzM3ljNDU4aGdndWZ5bm05eDc3bDRsMnU=
  - index: true
    key: YW1vdW50
    value: MTk5M3Vha3Q=
  type: transfer
- attributes:
  - index: true
    key: c2VuZGVy
    value: YWthc2gxNHBwaHNzNzI2dGhwd3dzM3ljNDU4aGdndWZ5bm05eDc3bDRsMnU=
  type: message
- attributes:
  - index: true
    key: bW9kdWxl
    value: ZGVwbG95bWVudA==
  - index: true
    key: YWN0aW9u
    value: ZGVwbG95bWVudC1jbG9zZWQ=
  - index: true
    key: b3duZXI=
    value: YWthc2gxdGVnNW52bjk3cTBneXphcDdrZnprZDBwZDZqZW43Mmhna2twdGw=
  - index: true
    key: ZHNlcQ==
    value: NzUwOTE5Nw==
  type: akash.v1
- attributes:
  - index: true
    key: bW9kdWxl
    value: ZGVwbG95bWVudA==
  - index: true
    key: YWN0aW9u
    value: Z3JvdXAtY2xvc2Vk
  - index: true
    key: b3duZXI=
    value: YWthc2gxdGVnNW52bjk3cTBneXphcDdrZnprZDBwZDZqZW43Mmhna2twdGw=
  - index: true
    key: ZHNlcQ==
    value: NzUwOTE5Nw==
  - index: true
    key: Z3NlcQ==
    value: MQ==
  type: akash.v1
- attributes:
  - index: true
    key: bW9kdWxl
    value: bWFya2V0
  - index: true
    key: YWN0aW9u
    value: b3JkZXItY2xvc2Vk
  - index: true
    key: b3duZXI=
    value: YWthc2gxdGVnNW52bjk3cTBneXphcDdrZnprZDBwZDZqZW43Mmhna2twdGw=
  - index: true
    key: ZHNlcQ==
    value: NzUwOTE5Nw==
  - index: true
    key: Z3NlcQ==
    value: MQ==
  - index: true
    key: b3NlcQ==
    value: MQ==
  type: akash.v1
- attributes:
  - index: true
    key: c3BlbmRlcg==
    value: YWthc2gxNHBwaHNzNzI2dGhwd3dzM3ljNDU4aGdndWZ5bm05eDc3bDRsMnU=
  - index: true
    key: YW1vdW50
    value: NTAwMDAwMHVha3Q=
  type: coin_spent
- attributes:
  - index: true
    key: cmVjZWl2ZXI=
    value: YWthc2gxeGZ6cXo1ejR4bXV0djlzeTdmMnN4aDhxc3plazRnZG1uN2pqajc=
  - index: true
    key: YW1vdW50
    value: NTAwMDAwMHVha3Q=
  type: coin_received
- attributes:
  - index: true
    key: cmVjaXBpZW50
    value: YWthc2gxeGZ6cXo1ejR4bXV0djlzeTdmMnN4aDhxc3plazRnZG1uN2pqajc=
  - index: true
    key: c2VuZGVy
    value: YWthc2gxNHBwaHNzNzI2dGhwd3dzM3ljNDU4aGdndWZ5bm05eDc3bDRsMnU=
  - index: true
    key: YW1vdW50
    value: NTAwMDAwMHVha3Q=
  type: transfer
- attributes:
  - index: true
    key: c2VuZGVy
    value: YWthc2gxNHBwaHNzNzI2dGhwd3dzM3ljNDU4aGdndWZ5bm05eDc3bDRsMnU=
  type: message
- attributes:
  - index: true
    key: bW9kdWxl
    value: bWFya2V0
  - index: true
    key: YWN0aW9u
    value: YmlkLWNsb3NlZA==
  - index: true
    key: b3duZXI=
    value: YWthc2gxdGVnNW52bjk3cTBneXphcDdrZnprZDBwZDZqZW43Mmhna2twdGw=
  - index: true
    key: ZHNlcQ==
    value: NzUwOTE5Nw==
  - index: true
    key: Z3NlcQ==
    value: MQ==
  - index: true
    key: b3NlcQ==
    value: MQ==
  - index: true
    key: cHJvdmlkZXI=
    value: YWthc2gxeGZ6cXo1ejR4bXV0djlzeTdmMnN4aDhxc3plazRnZG1uN2pqajc=
  - index: true
    key: cHJpY2UtZGVub20=
    value: dWFrdA==
  - index: true
    key: cHJpY2UtYW1vdW50
    value: Mzk4LjcyMDAwMDAwMDAwMDAwMDAwMA==
  type: akash.v1
- attributes:
  - index: true
    key: bW9kdWxl
    value: bWFya2V0
  - index: true
    key: YWN0aW9u
    value: bGVhc2UtY2xvc2Vk
  - index: true
    key: b3duZXI=
    value: YWthc2gxdGVnNW52bjk3cTBneXphcDdrZnprZDBwZDZqZW43Mmhna2twdGw=
  - index: true
    key: ZHNlcQ==
    value: NzUwOTE5Nw==
  - index: true
    key: Z3NlcQ==
    value: MQ==
  - index: true
    key: b3NlcQ==
    value: MQ==
  - index: true
    key: cHJvdmlkZXI=
    value: YWthc2gxeGZ6cXo1ejR4bXV0djlzeTdmMnN4aDhxc3plazRnZG1uN2pqajc=
  - index: true
    key: cHJpY2UtZGVub20=
    value: dWFrdA==
  - index: true
    key: cHJpY2UtYW1vdW50
    value: Mzk4LjcyMDAwMDAwMDAwMDAwMDAwMA==
  type: akash.v1
gas_used: "240179"
gas_wanted: "344166"
height: "7509217"
info: ""
logs:
- events:
  - attributes:
    - key: module
      value: deployment
    - key: action
      value: deployment-closed
    - key: owner
      value: akash1teg5nvn97q0gyzap7kfzkd0pd6jen72hgkkptl
    - key: dseq
      value: "7509197"
    - key: module
      value: deployment
    - key: action
      value: group-closed
    - key: owner
      value: akash1teg5nvn97q0gyzap7kfzkd0pd6jen72hgkkptl
    - key: dseq
      value: "7509197"
    - key: gseq
      value: "1"
    - key: module
      value: market
    - key: action
      value: order-closed
    - key: owner
      value: akash1teg5nvn97q0gyzap7kfzkd0pd6jen72hgkkptl
    - key: dseq
      value: "7509197"
    - key: gseq
      value: "1"
    - key: oseq
      value: "1"
    - key: module
      value: market
    - key: action
      value: bid-closed
    - key: owner
      value: akash1teg5nvn97q0gyzap7kfzkd0pd6jen72hgkkptl
    - key: dseq
      value: "7509197"
    - key: gseq
      value: "1"
    - key: oseq
      value: "1"
    - key: provider
      value: akash1xfzqz5z4xmutv9sy7f2sxh8qszek4gdmn7jjj7
    - key: price-denom
      value: uakt
    - key: price-amount
      value: "398.720000000000000000"
    - key: module
      value: market
    - key: action
      value: lease-closed
    - key: owner
      value: akash1teg5nvn97q0gyzap7kfzkd0pd6jen72hgkkptl
    - key: dseq
      value: "7509197"
    - key: gseq
      value: "1"
    - key: oseq
      value: "1"
    - key: provider
      value: akash1xfzqz5z4xmutv9sy7f2sxh8qszek4gdmn7jjj7
    - key: price-denom
      value: uakt
    - key: price-amount
      value: "398.720000000000000000"
    type: akash.v1
  - attributes:
    - key: receiver
      value: akash1teg5nvn97q0gyzap7kfzkd0pd6jen72hgkkptl
    - key: amount
      value: 4998006uakt
    - key: receiver
      value: akash1xfzqz5z4xmutv9sy7f2sxh8qszek4gdmn7jjj7
    - key: amount
      value: 1993uakt
    - key: receiver
      value: akash1xfzqz5z4xmutv9sy7f2sxh8qszek4gdmn7jjj7
    - key: amount
      value: 5000000uakt
    type: coin_received
  - attributes:
    - key: spender
      value: akash14pphss726thpwws3yc458hggufynm9x77l4l2u
    - key: amount
      value: 4998006uakt
    - key: spender
      value: akash14pphss726thpwws3yc458hggufynm9x77l4l2u
    - key: amount
      value: 1993uakt
    - key: spender
      value: akash14pphss726thpwws3yc458hggufynm9x77l4l2u
    - key: amount
      value: 5000000uakt
    type: coin_spent
  - attributes:
    - key: action
      value: /akash.deployment.v1beta2.MsgCloseDeployment
    - key: sender
      value: akash14pphss726thpwws3yc458hggufynm9x77l4l2u
    - key: sender
      value: akash14pphss726thpwws3yc458hggufynm9x77l4l2u
    - key: sender
      value: akash14pphss726thpwws3yc458hggufynm9x77l4l2u
    type: message
  - attributes:
    - key: recipient
      value: akash1teg5nvn97q0gyzap7kfzkd0pd6jen72hgkkptl
    - key: sender
      value: akash14pphss726thpwws3yc458hggufynm9x77l4l2u
    - key: amount
      value: 4998006uakt
    - key: recipient
      value: akash1xfzqz5z4xmutv9sy7f2sxh8qszek4gdmn7jjj7
    - key: sender
      value: akash14pphss726thpwws3yc458hggufynm9x77l4l2u
    - key: amount
      value: 1993uakt
    - key: recipient
      value: akash1xfzqz5z4xmutv9sy7f2sxh8qszek4gdmn7jjj7
    - key: sender
      value: akash14pphss726thpwws3yc458hggufynm9x77l4l2u
    - key: amount
      value: 5000000uakt
    type: transfer
  log: ""
  msg_index: 0
raw_log: '[{"events":[{"type":"akash.v1","attributes":[{"key":"module","value":"deployment"},{"key":"action","value":"deployment-closed"},{"key":"owner","value":"akash1teg5nvn97q0gyzap7kfzkd0pd6jen72hgkkptl"},{"key":"dseq","value":"7509197"},{"key":"module","value":"deployment"},{"key":"action","value":"group-closed"},{"key":"owner","value":"akash1teg5nvn97q0gyzap7kfzkd0pd6jen72hgkkptl"},{"key":"dseq","value":"7509197"},{"key":"gseq","value":"1"},{"key":"module","value":"market"},{"key":"action","value":"order-closed"},{"key":"owner","value":"akash1teg5nvn97q0gyzap7kfzkd0pd6jen72hgkkptl"},{"key":"dseq","value":"7509197"},{"key":"gseq","value":"1"},{"key":"oseq","value":"1"},{"key":"module","value":"market"},{"key":"action","value":"bid-closed"},{"key":"owner","value":"akash1teg5nvn97q0gyzap7kfzkd0pd6jen72hgkkptl"},{"key":"dseq","value":"7509197"},{"key":"gseq","value":"1"},{"key":"oseq","value":"1"},{"key":"provider","value":"akash1xfzqz5z4xmutv9sy7f2sxh8qszek4gdmn7jjj7"},{"key":"price-denom","value":"uakt"},{"key":"price-amount","value":"398.720000000000000000"},{"key":"module","value":"market"},{"key":"action","value":"lease-closed"},{"key":"owner","value":"akash1teg5nvn97q0gyzap7kfzkd0pd6jen72hgkkptl"},{"key":"dseq","value":"7509197"},{"key":"gseq","value":"1"},{"key":"oseq","value":"1"},{"key":"provider","value":"akash1xfzqz5z4xmutv9sy7f2sxh8qszek4gdmn7jjj7"},{"key":"price-denom","value":"uakt"},{"key":"price-amount","value":"398.720000000000000000"}]},{"type":"coin_received","attributes":[{"key":"receiver","value":"akash1teg5nvn97q0gyzap7kfzkd0pd6jen72hgkkptl"},{"key":"amount","value":"4998006uakt"},{"key":"receiver","value":"akash1xfzqz5z4xmutv9sy7f2sxh8qszek4gdmn7jjj7"},{"key":"amount","value":"1993uakt"},{"key":"receiver","value":"akash1xfzqz5z4xmutv9sy7f2sxh8qszek4gdmn7jjj7"},{"key":"amount","value":"5000000uakt"}]},{"type":"coin_spent","attributes":[{"key":"spender","value":"akash14pphss726thpwws3yc458hggufynm9x77l4l2u"},{"key":"amount","value":"4998006uakt"},{"key":"spender","value":"akash14pphss726thpwws3yc458hggufynm9x77l4l2u"},{"key":"amount","value":"1993uakt"},{"key":"spender","value":"akash14pphss726thpwws3yc458hggufynm9x77l4l2u"},{"key":"amount","value":"5000000uakt"}]},{"type":"message","attributes":[{"key":"action","value":"/akash.deployment.v1beta2.MsgCloseDeployment"},{"key":"sender","value":"akash14pphss726thpwws3yc458hggufynm9x77l4l2u"},{"key":"sender","value":"akash14pphss726thpwws3yc458hggufynm9x77l4l2u"},{"key":"sender","value":"akash14pphss726thpwws3yc458hggufynm9x77l4l2u"}]},{"type":"transfer","attributes":[{"key":"recipient","value":"akash1teg5nvn97q0gyzap7kfzkd0pd6jen72hgkkptl"},{"key":"sender","value":"akash14pphss726thpwws3yc458hggufynm9x77l4l2u"},{"key":"amount","value":"4998006uakt"},{"key":"recipient","value":"akash1xfzqz5z4xmutv9sy7f2sxh8qszek4gdmn7jjj7"},{"key":"sender","value":"akash14pphss726thpwws3yc458hggufynm9x77l4l2u"},{"key":"amount","value":"1993uakt"},{"key":"recipient","value":"akash1xfzqz5z4xmutv9sy7f2sxh8qszek4gdmn7jjj7"},{"key":"sender","value":"akash14pphss726thpwws3yc458hggufynm9x77l4l2u"},{"key":"amount","value":"5000000uakt"}]}]}]'
timestamp: "2022-09-06T18:46:08Z"
tx:
  '@type': /cosmos.tx.v1beta1.Tx
  auth_info:
    fee:
      amount:
      - amount: "8605"
        denom: uakt
      gas_limit: "344166"
      granter: ""
      payer: ""
    signer_infos:
    - mode_info:
        single:
          mode: SIGN_MODE_DIRECT
      public_key:
        '@type': /cosmos.crypto.secp256k1.PubKey
        key: AqeCqYAuASMth0IC6huobTkuLv64AkFgmOh3wjVBQVUW
      sequence: "16"
  body:
    extension_options: []
    memo: ""
    messages:
    - '@type': /akash.deployment.v1beta2.MsgCloseDeployment
      id:
        dseq: "7509197"
        owner: akash1teg5nvn97q0gyzap7kfzkd0pd6jen72hgkkptl
    non_critical_extension_options: []
    timeout_height: "0"
  signatures:
  - ep21R2i7wRTBh5TQIPSGy+na87GS89EyH4LQgT4VKCwpVVByFAXyvRUjiv5K+Wa0C2sJpzrfV7gNF25hqqL94A==
txhash: ACF35CCBD4DA831471C77943994C9040E88E88069F6693B666B5F78880FBEB9A
```

Your CLI is now setup, and you are ready to dive into the world of auditing.
