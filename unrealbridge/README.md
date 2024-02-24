# UnrealAdapter

## How It Works

This module interacts Unreal through the [LE Socket Connection](https://www.unrealengine.com/marketplace/en-US/product/low-entry-socket-connection) interface. It exposes a TCP server that allows the LE Blueprint script in Unreal engine to connect to. It also exposes a UDP connection for other scripts to read and write data.

## Unreal TCP Package Format

| Data Type | Field | Desc |
| --------- | ----- | ---- |
| int64     | timestamp | Time Stamp |
| int32     | size      | number of transforms in the following data |
| float32   | x | Location X |
| float32   | y | Location Y |
| float32   | z | Location Z |
| float32   | rw | Rotation quat W |
| float32   | rx | Rotation quat X |
| float32   | ry | Rotation quat Y |
| float32   | rz | Rotation quat Z |

## Installation

```bash
pip install -e .
```
