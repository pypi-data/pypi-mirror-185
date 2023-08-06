Lets create very simple apps based on classic one-to-one architecture where the `Controller` is running together with one of the nodes:

![image.png](images/one-to-one.png)
`Process 1` can trigger remote callbacks `func1` and `func2` from `Process2`. Communication between `Node` runinning in `Process1` and `Node` running in `Process2` is happen to be through `Controller` running in `Process1` 


![one-to-one-reverse](images/one-to-one-reverse.png) 
<br /><br /><br /><br /><br /><br />
---
But if `func3` is registered as callback in `Process1` and `Process1` has `Node` running. This also means that `Process2` can call this callback asynchronously

<br /><br /><br /><br /><br /><br /><br /><br /><br />

---

Let's see the full example first, and we'll break it down piece by piece
<br /><br />

Process1:
```python
import time
import threading
from daffi import Global, callback, FG, NO_RETURN


@callback
def func3(a: int, b: int) -> int:
    """Add 2 numbers and return sum"""
    # Simulate long running job
    time.sleep(3)
    return a + b


def remote_process_executor(g: Global):
    """Execute remote callbacks"""

    for _ in range(10):
        delta = g.call.func1(10, 3) & FG

        print(f'Calculated delta = {delta}')

        g.call.func2() & NO_RETURN

        time.sleep(5)


def main():
    """Main entrypoint"""
    process_name = 'proc1'

    g = Global(process_name=process_name, init_controller=True, host='localhost', port=8888)

    g.wait_process('proc2')

    re = threading.Thread(target=remote_process_executor, args=(g,))
    re.start()
    re.join()

    g.stop()


if __name__ == '__main__':
   main()
```
(This script is complete, it should run "as is")



Process2:
```python
"""Lets make process 2 asynchronous! Daffi works great with any type of applications"""
import asyncio
from daffi import Global, callback, BG


@callback
async def func1(a: int, b: int) -> int:
    """Subtracts 2 numbers and return delta"""
    return a - b


@callback
def func2() -> None:
    """Just print text to console"""
    print('Func2 has been triggered!')



async def remote_process_executor(g: Global):
    """Execute remote callbacks"""
    for _ in range(5):
        future = g.call.func3(4, 6) & BG

        # Do smth while result is processing
        await asyncio.sleep(2)

        # Get result
        result = await future.get_async()
        print(f"Calculated sum is {result!r}")


async def main():
    """Main entrypoint"""

    process_name = 'proc2'

    g = Global(process_name=process_name, host='localhost', port=8888)
    asyncio.create_task(remote_process_executor(g))

    # Wait forever
    await g.join_async()


if __name__ == '__main__':
   asyncio.run(main())
```
(This script is complete, it should run "as is")


### Explanation

On the top level daffi has 2 main components. It is `Global` object and `callback` decorator

- `Global` is the main initialization entrypoint and remote callbacks executor at the same time.

In `Process1` we have following `Global` initialization statement:
```python
g = Global(process_name=process_name, init_controller=True, host='localhost', port=8888)
```
 
 where:
 
 - `process_name` is optional `Node` identificator. 
 
!!! note
    If `process_name` argument is omitted then randomly generated name will be used.
    But in some cases it is helpful to give nodes meaningful names. 
    
    For example on next line we are waiting `proc2` to be started.
    
    It is possible since we gave `proc2` name to `Node` that is running in `Process2` script.

     ```python
    g.wait_process('proc2')
    ```

- `init_controller=True` Means we want to start `Controller` in this process.

!!! note
    `init_node` argument is True
    by default so if you want to start only controller in particular process you should be explicit:


    ```python
    g = Global(process_name=process_name, init_controller=True, init_node=False, host='localhost', port=8888)
    ```

- `host` and `port` arguments give `Controller` and `Node` information how to connect.


!!! note
    `host` and `port` arguments are also optional.
    For instance you can specify only `host`. In this case `Controller`/`Node` or both will be connected to random port

    You can also skip these two arguments:
    ```python
    g = Global(process_name=process_name, init_controller=True)
    ```
    In this case `Controller`/`Node` will be connected using UNIX socket. By default UNIX socket is created using path
    ```bash
    < temp directory >/daffi/.sock
    ```
    Where `< temp directory >` is temporary directory of machine where `Controller`/`Node` is running. For instance it is going to be `/tmp/daffi/.sock` on Ubuntu.


Next point is `callback` decorator


```python
@callback
def func3(a: int, b: int) -> int:
    """Add 2 numbers and return sum"""
    # Simulate long running job
    time.sleep(3)
    return a + b

```
You can decorate any function despite it is synchronous or asynchronous. 
This statement register `func3` as remote callback on `Node` running in `Process1`. This wait 
`func3` becomes visible for all other nodes connected to the same controller.


!!! warning
    Do not use the same callback names in different processes unless you want to use `BROADCAST` feature of daffi.
    
    For singular execution, for instance if you have `some_method` callback registered in process `A` and in process `B` then
    only one of them will be triggered. Daffi use random strategy to execute callback by name. You cannot control which one
    will be triggered.

 
!!! note
    instead of decorating functions you can create a decorated class:
    
    ```python
    @callback
    class RemoteCallbackGroup:
    
        def method1(self):
            ...
        
        def method2(self):
            ...
        
        @staticmethod
        def method3():
            ...
    ```   
    In this case all public methods of decorated class become remote callbacks (`public` means witout undersore in the beginning of name)
    
    !!! But be carefull. Not all methods of class are visible without class instance. Only `static` methods and `class` methods
    can be triggered without class instance. For example on example above only `method3` is remote callback by default.
    For all other methods to be registered you need to create instance of `RemoteCallbackGroup`
    
    Also it is worth to mention that such decorated classes are singletons. You cannot create more then one instance of class in application.
    It has simple explanation:
    
    In case of many registered methods with the same name it is not clear for daffi which one should be triggered.
 
    And last important point for classes:
    
    Do not decorate particular methods. Only class decoration is valid for classes!!!

`Process1` scripts represents `Controller` and `Node` all in one. 


And last important topic for `Process1` script is `FG` and `NO_RETURN` callback modificators:

There are following modificators are available to trigger remote callback:

| Modificator class             | Description                                                           | Optional arguments  |
|------------------|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| `FG` | Stands for `foreground`. It means current process execution should be blocked until result of execution is returned.<br/>Another syntax is `g.call.<callback_name>(*args, **kwargs).fg(timeout=15)` | - `timeout`: The time to wait result. If exeeded `TimeoutError` will be thrown |
| `BG` | Stands for `background`. This modificator returns `AsyncResult` instance instead of result. Fits for long running tasks where caller execution cannot be blocked for a long time. <br/>Another syntax is `g.call.<callback_name>(*args, **kwargs).bg(timeout=15, eta=3)` | - `timeout`:  The time to wait result. If exeeded `TimeoutError` will be thrown <br/> - `eta`: The time to sleep in the background before sending request for execution | 
| `NO_RETURN` | Use it if you don't need result of remote execution. <br/>Another syntax is `g.call.<callback_name>(*args, **kwargs).no_return(eta=3)` | - `eta`: The time to sleep in the background before sending request for execution | 
| `PERIOD` | Use for scheduling reccuring tasks or tasks which should be executed several times. <br/>Another syntax is `g.call.<callback_name>(*args, **kwargs).period(at_time=[datetime.utcnow().timestamp() + 3, datetime.utcnow().timestamp() + 10])` | - `at_time`: One timestamp or list of timestamps. Timestamps should be according to utc time and it should be timestamp in the future. This argument forces remote callback to be triggered one or more times when when timestamp == datetime.utcnow().timestamp<br/> - `period`: Duration in seconds to trigger remote callback on regular bases. <br/> One can provide either `at_time` argument or `period` argument in one request. Not both! | 
| `BROADCAST` | Trigger all available callbacks on nodes by name. If `return_result` argument is set to True then aggregated result will be returned as dictionary where keys are node names and values are computed results. <br/>Another syntax is `g.call.<callback_name>(*args, **kwargs).broadcast(timeout=15, eta=3, return_result=True)` | - `timeout`:  The time to wait result. If exeeded `TimeoutError` will be thrown <br/> - `eta`: The time to sleep in the background before sending request for execution <br/> `return_result`: If provided aggregated result from all nodes where callback exist will be returned. | 


And last step. Lets go through `Process2` script:

In contrast to `Process1`, `Process2` script use asyncio. It doesnt matter for daffi which type of callback execute remotely.

`Global` instance initialization looks like this:

```python
g = Global(process_name=process_name, host='localhost', port=8888)
```

If `init_controller` is skipped then only `Node` will be initialized in current process.
Also this process sleeps forever on this line: 

```python
await g.join_async()
```

Usually it is the case for long running daffi processes to wait requests forever.

!!! warning
    Most of daffi methods works fine with both sync and async applications but some of them blocks event loop. 
    Blocking methods have async conterparts which should be used for asynchronous processes.
    For example `Global` object has method `join` which is blocking method and cannot be used for applications 
    which leverage on event loop. 
    But `Global` also has `join_async` method which fits async non blocking model.
    Also in example above `Process2` uses `result = await future.get_async()` statement to take result asynchronously.
    In synchronous applications there is method `get` does this job.
    
    Another methods category is generic methods. For instance in `Process1` we used statement:
    ```python
    delta = g.call.func1(10, 3) & FG
    ```
    to wait for result.
    
    For async applications it is also possible to use this statement as coroutine:
    ```python
    delta = await g.call.func1(10, 3) & FG
    ```
    
    But async waing doing this has certain limitation. For example following syntax is not valid:
    ```python
     fg = FG(timeout=10)
    delta = await g.call.func1(10, 3) & fg
    ```
    
    Only one-liner expression will be treated as coroutine:
    ```python
    delta = await g.call.func1(10, 3) & FG(timeout=10)
    ```

