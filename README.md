# Yet Another arXiv Filter

A hacky keyword/author search through daily arxiv emails. There are probably some edge cases this doesn't handle.

![Image](img/result.png)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Disclaimer](#license)

## Installation

Clone the repo.

## Usage

1. `pip install rich` for pretty output. 
2. Fill `keywords.txt` and `authors.txt` (one per line). Keywords are searched in the title and abstract.
3. Copy mail contents into `mail_text.txt`.
4. `python arxiv_filter.py`

## Contributing

Any feedback is welcome. 

## Disclaimer

The author(s) of this repository are not responsible for any potential loss of career opportunities due to missed arXiv papers. Use at your own risk.  