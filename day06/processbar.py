#!/usr/bin/env python3
import time

import tqdm

for i in range(10):
    time.sleep(0.2)

for i in tqdm.tqdm(range(10)):
    time.sleep(0.2)
