![test and validate](https://github.com/600apples/dafi/actions/workflows/test_and_validate.yml/badge.svg)
![publish docs](https://github.com/600apples/dafi/actions/workflows/publish_docs.yml/badge.svg)
![coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/600apples/c64b2cee548575858e40834754432018/raw/covbadge.json)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://600apples.github.io/dafi/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
[![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg)
[![macOS](https://warehouse-camo.ingress.cmh1.psfhosted.org/f15e9d8a362a7c2ef7d13ec12cc03f96fdcfe2a3/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f68617463682e7376673f6c6f676f3d707974686f6e266c6162656c3d507974686f6e266c6f676f436f6c6f723d676f6c64)](hhttps://warehouse-camo.ingress.cmh1.psfhosted.org/f15e9d8a362a7c2ef7d13ec12cc03f96fdcfe2a3/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f68617463682e7376673f6c6f676f3d707974686f6e266c6162656c3d507974686f6e266c6f676f436f6c6f723d676f6c64)

Daffi is fast and lightweight library for RPC communication with ability to register and execute remote callbacks on many nodes.
 

### Features
 
- All processes where daffi is running have equal opportunities. Any process (Node) can trigger a remote callback on any other process (Node).
- Super fast and strong serialization/deserialization system based on [grpc](https://grpc.io/docs/) streams and [dill](https://pypi.org/project/dill/). You can serialize dataclasses, functions (with yield statements as well), lambdas, modules and many other types.
- Daffi works equally well with both synchronous and asynchronous applications. You can call asynchronous remote callback from synchronous application and vice versa.
- Very simple syntax. Unlike many other simular libraries, daffi has only a few high-level classes for registering callbacks and calling callbacks.
- Daffi can works via TCP or via UNIX socket.
