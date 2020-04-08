# Lucky Lottery

> Lucky Lottery based on [Bihu Airdrop Tool](https://github.com/bihu-id/bihu-tools).

[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger) [![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

## Table of Contents

- [Explanation](#explanation)
- [Features](#features)
- [Contributing](#contributing)
- [Team](#team)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)

## Explanation

* ExinLocal will assign a lottery number, an integer starting from 1 to each qualified participant;
* ExinLocal will announce a certain block number of Bitcoin in the future before the event, such as **624960**;
    - Use the hash of this block to calculate a luck number
    - luck_num = hash1(hash2(...hash(n)(block.hash)))
* For each lottery number, calculate the score;
    - score ＝ hash (luck_num + lottery number) ％ base
* Sort by score, the highest reward is 0.01 BTC.

## Features

- Lucky Lottery based on Bitcoin blocks hash;
- The algorithm is open source and the results can be verified.

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
