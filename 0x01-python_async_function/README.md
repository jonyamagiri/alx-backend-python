# 0x01. Python - Async

> This repository contains the tasks for `Python - Async` project and a description of what each program or function does:


## Learning Objectives

	* async and await syntax
	* How to execute an async program with asyncio
	* How to run concurrent coroutines
	* How to create asyncio tasks
	* How to use the random module


* In Python, asynchronous programming is used to write programs that can handle multiple tasks concurrently. The `async` and `await` syntax are used to define and work with asynchronous functions.

* An asynchronous function is a function that can be paused while waiting for some operation to complete, without blocking the execution of the program. When the operation completes, the function can be resumed from the point where it was paused.

* Here's an example of an asynchronous function that uses `async` and `await` syntax to fetch data from a website:

```
import aiohttp
import asyncio

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
```

* In the example above, the `async` keyword is used to define an asynchronous function called `fetch_data()`. Inside the function, the `await` keyword is used to pause the execution of the function until the data is fetched from the website. Once the data is fetched, the function resumes and returns the text of the response.

* To call an asynchronous function, you can use the `await` keyword to pause the execution of the current function until the asynchronous function completes. Here's an example of calling the `fetch_data()` function:

```
async def main():
    data = await fetch_data('https://example.com')
    print(data)

asyncio.run(main())
```

* In the example above, the `main()` function is also defined as an asynchronous function using the `async` keyword. Inside the function, the `await` keyword is used to pause the execution until the `fetch_data()` function completes. Once the data is fetched, the `print()` function is called to display the data.

* Note that to use `async` and `await` syntax, you need to have Python 3.5 or later installed on your system.


## Tasks

- [x] Task: 0-basic_async_syntax.py

- [x] Task: 1-concurrent_coroutines.py

- [x] Task: 2-measure_runtime.py

- [x] Task: 3-tasks.py

- [x] Task: 4-tasks.py


___

* [test_files](https://github.com/jonyamagiri/alx-backend-python/tree/main/0x01-python_async_function/test_files)


