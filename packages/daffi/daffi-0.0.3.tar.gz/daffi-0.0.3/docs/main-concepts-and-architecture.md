When developing daffi, we wanted to get away from the concept of a client-server architecture and make each of the processes equal.


## Controller
But server is still there. In daffi terminology, this is called `Controller`.

The `Controller` serves only as a broker and cannot call remote callbacks on its own.

`Controller` also does not do any hard work and can be run in any of the processes where remote callbacks are registered, 
but it can also work as stand-alone application. Both variants are fine depends on your requirements.


## Node
`Node` is worker that is running along with `Controller` or as stand-alone process.

The application where the `Node` is running gets the opportunity to register callbacks and call the callbacks of other nodes.


### main features and architectural approaches

Following is the short list of features which we will cover in more detail in the following sections of the documentation: 

1. Base communication between two proccesses. One-to-one architecture
2. Schedulers. Running reccuring tasks on remote `Node`
3. Isolated systems. It is also possible to have more then one `Controller`. Part of nodes can be connected to one `Controller` and rest to another
4. Broadcasting. It is possible to register the same callback on different nodes. Particular node can trigger all callback at once and get one combined result as response.
