# spezialist

![PyPI Version](https://img.shields.io/pypi/v/spezialist)
![License](https://img.shields.io/pypi/l/spezialist)

A lightweight Python utility for **special listing methods**. `spezialist` provides simple functions to filter directory listings, exclude unwanted or hidden files, and streamline specialized list processing tasks.

---

## Features

* 📁 **Clean Directory Listings**: Exclude system files like `.DS_Store` or hidden entries.
* 🌐 **Absolute or Relative Paths**: Choose to return full filesystem paths or just filenames.
* 🔄 **Pure Python, Zero Dependencies**: Only uses the standard library (`os` module).
* 🧩 **Modular Functions**: Import only what you need.

---

## Installation

Install via pip:

```bash
pip install spezialist
```

---

## Quickstart

```python
from spezialist import (
    list_dir_without_ds,         # filenames, no .DS_Store
    list_dir_without_ds_abs,     # absolute paths, no .DS_Store
    list_dir_without_dot,        # filenames, no hidden files
    list_dir_without_dot_abs,    # absolute paths, no hidden files
)

# List only visible filenames
files = list_dir_without_dot("./my_folder")
print(files)

# List absolute paths excluding .DS_Store
paths = list_dir_without_ds_abs("./Downloads")
print(paths)
```

---

## Contributing

Contributions are welcome! Please:

1. Fork the repo on GitHub
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Write tests and update documentation
4. Submit a pull request

Ensure all tests pass:

```bash
pytest
```

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
