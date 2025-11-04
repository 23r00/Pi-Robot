#!/bin/bash

nmcli device wifi hotspot con-name Robot_Pi ssid Robot_Pi band bg channel 1 password 12345678
nmcli dev wifi show-password