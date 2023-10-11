# Installation and Setup

Installation

1. 1.Install node.js.
2. 2.Install Postgres database. You can choose between:
   1. 1.Install Postgres locally.
   2. 2.Run Posrtgres using Docker. In this case you need to install Docker.
3. 3.Run `yarn` in the root folder of the monorepo to install package dependencies.

### Setup <a href="#setup" id="setup"></a>

The following steps should be done in order to setup a Job Launcher:

#### 1. Staking <a href="#1.-staking" id="1.-staking"></a>

In order to be allowed to launch jobs the Job Launcher needs to stake HMT. There 2 options to stake:

1. 1.​[Using a staking script](https://app.gitbook.com/o/gVcp9m9Bobj6V368GNOW/s/KdzSNb2tF2ABcQCulU6K/page/job-launcher/installation-and-setup#using-a-script).
2. 2.​[Using the block scanner](https://app.gitbook.com/o/gVcp9m9Bobj6V368GNOW/s/KdzSNb2tF2ABcQCulU6K/page/job-launcher/installation-and-setup#using-block-scanner).

**Using a script**

Available soon.

**Using block scanner**

1. 1.Go to the scanner website. For this example [Polygon Mumbai scanner](https://mumbai.polygonscan.com/).
2. 2.Search for the HMT token contract. Youn can find contract addresses [here](https://github.com/humanprotocol/human-protocol/blob/main/CONTRACTS\_LIST.md).
3. 3.Connect your wallet.
4. 4.Call approve function passing Staking contract address as spender and the amount desired to stake.![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FKdzSNb2tF2ABcQCulU6K%2Fuploads%2FEIS7NLL5TFAenY3uj3jK%2Fimage.png?alt=media\&token=9a525415-d7a1-4853-93b1-ba22d4c51a81)
5. 5.Search for the Staking contract. Youn can find contract addresses [here](https://github.com/humanprotocol/human-protocol/blob/main/CONTRACTS\_LIST.md).
6. 6.Connect your wallet.
7. 7.Call stake function with the amount approved previously.![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FKdzSNb2tF2ABcQCulU6K%2Fuploads%2FtA2EGCUOzzAeYp1d7nB4%2Fimage.png?alt=media\&token=b0a2deb6-4da9-4db9-9daa-ca0817e279ac)

#### 2. Server Environment Variables <a href="#2.-server-environment-variables" id="2.-server-environment-variables"></a>

A `.env` file with the following variables should be added in the root folder of the server&#x20;

| Name            | Description                            | Opt | Values                    | Default value                                     |
| --------------- | -------------------------------------- | --- | ------------------------- | ------------------------------------------------- |
| NODE\_ENV       | Environment type                       |     | development \| production | development                                       |
| HOST            | Host address                           |     | ​                         | localhost                                         |
| PORT            | Port to use for serving                |     | ​                         | 5000                                              |
| FE\_URL         | Frontend url                           |     | ​                         | ​[http://localhost:3005](http://localhost:3005/)​ |
| SESSION\_SECRET | Secret used to sign the session cookie |     | ​                         | session\_key                                      |

**Example**