---
title: Protocol Buffers
weight: 33
---

![GitHub Repo stars](https://img.shields.io/github/stars/protocolbuffers/protobuf?style=social) ![GitHub last commit](https://img.shields.io/github/last-commit/protocolbuffers/protobuf) ![GitHub](https://img.shields.io/github/license/protocolbuffers/protobuf)

Protocol buffers provide a serialization format for packets of typed, structured data that are up to a few megabytes in size. The format is suitable for both ephemeral network traffic and long-term data storage. Protocol buffers can be extended with new information without invalidating existing data or requiring code to be updated. They are the most commonly-used data format at Google.

**Extension:** `.proto`

## Protocol Buffers Official Documentation

https://developers.google.com/protocol-buffers/docs/overview

## Protocol Buffers Advantages

- Compact data storage
- Fast parsing
- Available in [several programming languages](https://developers.google.com/protocol-buffers/docs/overview#cross-lang)

## Protocol Buffers Disadvantages

- Not suitable for data larger than a few megabytes
- Messages are not compressed. You can compress them but sometimes special-purpose compression algorithms (JPEG, PNG) will produce more optimal results.
- Not optimal for scientific and engineering use cases involving multi-dimensional arrays of floating point numbers.

