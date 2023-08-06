<h1 align="center">🤷 Option and Result</h1>

This library uses code copied and pasted from [Peijun Ma's `option` library](https://github.com/MaT1g3R/option), which they have generously published under the MIT license. 🙏

This is a Python implementation of Rust's [`Option`](https://doc.rust-lang.org/std/option/index.html) and [`Result`](https://doc.rust-lang.org/std/result/index.html) types in order to help make fallible functions identifiable and more robust than typical exceptions.

## 💻 Installation

This package is [published to PyPI as `babichjacob-option-and-result`](https://pypi.org/project/babichjacob-option-and-result/).

## 🛠 Usage

```py
from option_and_result import NONE, Some, Ok, Err

maybe_a_number = Some(17)
assert maybe_a_number.unwrap() == 17

nothing = NONE()
assert nothing.is_none()

number_result = maybe_a_number.ok_or("not a number")
assert number_result == Ok(17)

result_that_is_err = Err("gah! an error!")
combinatoric_result = number_result.and_(result_that_is_err)

assert combinatoric_result.unwrap_err() == "gah! an error!"

# more methods on Options and Results are available like the Rust documentation shows

# there is also MatchesNone, MatchesSome, MatchesOk, and MatchesErr
# for use with Python 3.10's new structural pattern matching feature
```

## 😵 Help! I have a question

Create an issue and I'll try to help.

## 😡 Fix! There is something that needs improvement

Create an issue or pull request and I'll try to fix.

## 📄 License

MIT

## 🙏 Attribution

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
