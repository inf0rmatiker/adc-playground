#!/bin/python3

import os
import time
import sys
import signal
import busio
import digitalio
import board
import numpy as np
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


def signal_handler(sig, frame):
    print("\nExiting\n")
    sys.exit(0)


def capture_buffer(input_channel: AnalogIn, filename: str):

    # capture 1000 samples
    # samples = np.empty(1000, dtype=np.ushort)
    # for i in range(1000):
    #     samples[i] = np.ushort(input_channel.value)
    
    # np.savetxt(filename, samples, fmt="%d", delimiter=",")

    samples=np.empty(1000, dtype=np.float_)
    for i in range(1000):
        samples[i] = np.float_(input_channel.voltage)

    np.savetxt(filename, samples, fmt="%.5f", delimiter=",")


def main():

    # Create SIGINT handler for graceful shutdowns
    signal.signal(signal.SIGINT, signal_handler)

    # create the spi bus
    spi_bus = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

    # create the chip select
    chip_select = digitalio.DigitalInOut(board.D22)

    # create the mcp object
    mcp = MCP.MCP3008(spi_bus, chip_select)

    # create an analog input channel on pin 0
    input_channel = AnalogIn(mcp, MCP.P0)

    print('Initial ADC Value: ', input_channel.value)
    print('Initial ADC Voltage: ' + str(input_channel.voltage) + 'V')


    for i in range(10):
        capture_buffer(input_channel, f"buffer_{i}.csv")

    print("Done")


if __name__ == "__main__":
    main()

