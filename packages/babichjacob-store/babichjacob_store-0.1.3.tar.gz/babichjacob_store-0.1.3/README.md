<h1 align="center">💾 Store</h1>

This library is a Python implementation of `svelte/store`.

## 💻 Installation

This package is [published to PyPI as `babichjacob-store`](https://pypi.org/project/babichjacob-store/).

## 🛠 Usage

```py
from store import writable

my_store = writable(17)
my_store.subscribe(lambda value: print(f"Store value changed to {value}"))
my_store.set(23)

# readable and derived are also available but I didn't feel like documenting them because this is just for myself
```

## 😵 Help! I have a question

Create an issue and I'll try to help.

## 😡 Fix! There is something that needs improvement

Create an issue or pull request and I'll try to fix.

## 📄 License

MIT

## 🙏 Attribution

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
