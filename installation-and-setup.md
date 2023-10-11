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

A `.env` file with the following variables should be added in the root folder of the server project:POSTGRES\_HOST Postgres database host 127.0.0.1POSTGRES\_USER Postgres database user operatorPOSTGRES\_PASSWORD Postgres database password qwertyPOSTGRES\_DATABASE Postgres database name job-launcherPOSTGRES\_PORT Postgres database port 5432POSTGRES\_SSL Use ssl for database connection true | false falseWEB3\_ENV Use testnets or mainnets testnet | mainnet testnetWEB3\_PRIVATE\_KEY Eth format private key for blockchain interactionsJOB\_LAUNCHER\_FEE Percentage fee taken by the Job Launcher 10EXCHANGE\_ORACLE\_FEE Percentage fee taken by the Exchange Oracle 10RECORDING\_ORACLE\_FEE Percentage fee taken by the Recording Oracle 10REPUTATION\_ORACLE\_FEE Percentage fee taken by the Reputation Oracle 10FORTUNE\_EXCHANGE\_ORACLE\_ADDRESS Blockchain address of the Exchange Oracle for Fortune jobsFORTUNE\_RECORDING\_ORACLE\_ADDRESS Blockchain address of the Exchange Oracle for Fortune jobsFORTUNE\_REPUTATION\_ORACLE\_ADDRESS Blockchain address of the Exchange Oracle for Fortune jobsCVAT\_EXCHANGE\_ORACLE\_ADDRESS Blockchain address of the Exchange Oracle for CVAT jobsCVAT\_EXCHANGE\_ORACLE\_WEBHOOK\_URL Webhook url of the Exchange Oracle for CVAT jobsFORTUNE\_RECORDING\_ORACLE\_ADDRESS Blockchain address of the Recording Oracle for CVAT jobsCVAT\_REPUTATION\_ORACLE\_ADDRESS Blockchain address of the Reputation Oracle for CVAT jobsHASH\_SECRET Secret used for hashing passwords on databaseJWT\_SECRET Secret used to generate jwtJWT\_ACCESS\_TOKEN\_EXPIRES\_IN Duration of the acces jwt expressed in seconds or a string describing a time span 1000000000JWT\_REFRESH\_TOKEN\_EXPIRES\_IN Duration of the refresh jwt expressed in seconds or a string describing a time span 1000000000S3\_ENDPOINT S3 service endpointS3\_PORT S3 service portS3\_ACCESS\_KEY S3 access keyS3\_SECRET\_KEY S3 secret keyS3\_BUCKET S3 bucket nameS3\_USE\_SSL Use ssl for S3 connection true | false falseSTRIPE\_SECRET\_KEY Stripe payments secret keySTRIPE\_API\_VERSION Stripe API version 2022-11-15STRIPE\_APP\_NAME App name in StripeSTRIPE\_APP\_VERSION App version in StripeSTRIPE\_APP\_INFO\_URL App url in StripeSENDGRID\_API\_KEY Sengrid API key used for sending emails

| Name            | Description                            | Opt | Values                    | Default value                                     |
| --------------- | -------------------------------------- | --- | ------------------------- | ------------------------------------------------- |
| NODE\_ENV       | Environment type                       |     | development \| production | development                                       |
| HOST            | Host address                           |     | ​                         | localhost                                         |
| PORT            | Port to use for serving                |     | ​                         | 5000                                              |
| FE\_URL         | Frontend url                           |     | ​                         | ​[http://localhost:3005](http://localhost:3005/)​ |
| SESSION\_SECRET | Secret used to sign the session cookie |     | ​                         | session\_key                                      |

**Example**

\# GeneralNODE\_ENV=developmentHOST=localhostPORT=3000FE\_URL=http://localhost:3001SESSION\_SECRET=test​# DatabasePOSTGRES\_HOST=0.0.0.0POSTGRES\_USER=operatorPOSTGRES\_PASSWORD=qwertyPOSTGRES\_DATABASE=job-launcherPOSTGRES\_PORT=5432POSTGRES\_SSL=false​#Web3WEB3\_ENV=testnetWEB3\_PRIVATE\_KEY=JOB\_LAUNCHER\_FEE=1EXCHANGE\_ORACLE\_FEE=1RECORDING\_ORACLE\_FEE=1REPUTATION\_ORACLE\_FEE=1FORTUNE\_EXCHANGE\_ORACLE\_ADDRESS=FORTUNE\_EXCHANGE\_ORACLE\_WEBHOOK\_URL=FORTUNE\_RECORDING\_ORACLE\_ADDRESS=FORTUNE\_REPUTATION\_ORACLE\_ADDRESS=CVAT\_EXCHANGE\_ORACLE\_ADDRESS=CVAT\_EXCHANGE\_ORACLE\_WEBHOOK\_URL=CVAT\_RECORDING\_ORACLE\_ADDRESS=CVAT\_REPUTATION\_ORACLE\_ADDRESS=​# AuthHASH\_SECRET=a328af3fc1dad15342cc3d68936008faJWT\_SECRET=test-secretJWT\_ACCESS\_TOKEN\_EXPIRES\_IN=1dJWT\_REFRESH\_TOKEN\_EXPIRES\_IN=1d​# S3S3\_ENDPOINT=localhostS3\_PORT=9000S3\_ACCESS\_KEY=access-keyS3\_SECRET\_KEY=secret-keyS3\_BUCKET=manifestsS3\_USE\_SSL=false​# StripeSTRIPE\_SECRET\_KEY=STRIPE\_API\_VERSION=STRIPE\_APP\_NAME=STRIPE\_APP\_VERSION=STRIPE\_APP\_INFO\_URL=​# SendgridSENDGRID\_API\_KEY=
