#!/bin/python3

import os
import time
import sys
import signal
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


def signal_handler(sig, frame):
    print("\nExiting\n")
    sys.exit(0)


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

    last_read = -1
    tolerance = 250

    while True:
        current_value = input_channel.value
        if abs(current_value - last_read) > tolerance:
            print(f"value={current_value},voltage={input_channel.voltage}")
            last_read = current_value


if __name__ == "__main__":
    main()

