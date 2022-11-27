#!/usr/bin/env bash

GIT_SSH_COMMAND='ssh -i ~/.ssh/leoalexanderbloom -o IdentitiesOnly=yes' eval "git $@"