#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Distributed under terms of the MIT license.
#
# Desc: Lucky Lottery based on Bihu Airdrop Tool.
# User: Robin@Exin
# Date: 2020-04-08
# Time: 17:26:36

import hashlib
import sys
from collections import OrderedDict

lucky_prefix = 'EXINLOCAL'
# block hash
block_hash = bytes.fromhex(sys.argv[1])
# total lottery num
total_lottery = 1024

def lucky_num_from_block_hash(h):
    hash_names = ['md5', 'md4', 'whirlpool', 'RIPEMD160', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
    print(str(len(hash_names)) + ": " + str(hash_names))

    repeat = 10000 * 400 * 20
    r = h
    for i in range(repeat):
        if i % 100000 == 0:
            print(str(i) + ":...")
        for n in hash_names:
            h = hashlib.new(n)
            h.update(r)
            r = h.digest()

    return r

def score_for_each_lottery(lucky_num, lottery_id):
    h = hashlib.sha256()
    h.update(lucky_num)
    h.update(bytes(lottery_id))

    base = 10**11
    score = int(h.hexdigest(), 16) % base
    return score

def compute_lucky_reward():
    r = {}
    lucky_num = lucky_num_from_block_hash(block_hash)

    for lottery_id in range(1, total_lottery + 1):
        s = score_for_each_lottery(lucky_num, lottery_id)
        r[lottery_id] = s
    return r

def lottery_format(n):
    return lucky_prefix + '-' + str(n).zfill(7)

def dump_rewards_to_file(rewards):
    c = 1
    f = open('rewards.txt', 'w')
    for r in rewards:
        f.write(str(c) + ',' + lottery_format(r) + ',' + str(rewards[r]) + '\n')
        c += 1

    f.close()

reward_map = compute_lucky_reward()
reward_sorted = OrderedDict(sorted(reward_map.items(), key=lambda t: t[1], reverse = True))
print("=======================Rewards result dumped into rewards.txt=======================")
dump_rewards_to_file(reward_sorted)