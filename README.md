# Lucky Lottery

> Lucky Lottery based on [Bihu Airdrop Tool](https://github.com/bihu-id/bihu-tools).

[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger) [![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

## Table of Contents

- [Explanation](#explanation)
- [Features](#features)
- [Usage](#usage)
- [Contributing](#contributing)
- [Team](#team)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)

## Explanation

* ExinLocal will assign each eligible participant a lottery number, an integer number starting with 1.
* ExinLocal will announce a future block number for bitcoin, such as **624960**, before the event begins.
    - Using the hash of this block, calculate a luck number
    - luck_num = hash1(hash2(.. .hash(n)(block.hash)))
* For each lottery number, a score is calculated.
    - score = hash (luck_num + lottery number) % base
* The highest awarded 0.01 BTC according to score order.

## Features

* Lucky Lottery based on Bitcoin blocks hash.
* The algorithm is open source and the results can be verified.

## Usage

> Python 3.0+ required.

``` bash
$ git clone https://github.com/ExinLocal/lucky-lottery
# 00000000000000000010a34de0c20440b6804f61549e1c1b18d0b80afb589d6e is the hash of 624960 height blocks
$ cd lucky-lottery
$ python3 lucky-lottery.py \
  00000000000000000010a34de0c20440b6804f61549e1c1b18d0b80afb589d6e
```

## Contributing

To be continued.

## Team

@Exin

## FAQ

To be continued.

## Support

Reach out to us at one of the following places!

- Website at <a href="https://exin.one" target="_blank">`exin.one`</a>
- Twitter at <a href="http://twitter.com/ExinLocal" target="_blank">`@ExinLocal`</a>
- Email at `robin@exin.one`

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)
