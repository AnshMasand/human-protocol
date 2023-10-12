# Class: EscrowUtils

[escrow](../wiki/escrow).EscrowUtils

## Table of contents

### Constructors

- [constructor](../wiki/escrow.EscrowUtils#constructor)

### Methods

- [getEscrow](../wiki/escrow.EscrowUtils#getescrow)
- [getEscrows](../wiki/escrow.EscrowUtils#getescrows)

## Constructors

### constructor

• **new EscrowUtils**()

## Methods

### getEscrow

▸ `Static` **getEscrow**(`chainId`, `escrowAddress`): `Promise`<`EscrowData`\>

Returns the escrow for a given address

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `chainId` | `ChainId` | Chain id. |
| `escrowAddress` | `string` | Escrow address. |

#### Returns

`Promise`<`EscrowData`\>

**`Throws`**

- An error object if an error occurred.

#### Defined in

[escrow.ts:1455](https://github.com/humanprotocol/human-protocol/blob/7d9221c2/packages/sdk/typescript/human-protocol-sdk/src/escrow.ts#L1455)

___

### getEscrows

▸ `Static` **getEscrows**(`filter`): `Promise`<`EscrowData`[]\>

Returns the list of escrows for given filter

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `filter` | `IEscrowsFilter` | Filter parameters. |

#### Returns

`Promise`<`EscrowData`[]\>

**`Throws`**

- An error object if an error occurred.

#### Defined in

[escrow.ts:1383](https://github.com/humanprotocol/human-protocol/blob/7d9221c2/packages/sdk/typescript/human-protocol-sdk/src/escrow.ts#L1383)
