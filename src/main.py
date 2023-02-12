#!/bin/python3

import os
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


def main():
    # create the spi bus
    spi_bus = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

    # create the chip select
    chip_select = digitalio.DigitalInOut(board.D22)

    # create the mcp object
    mcp = MCP.MCP3008(spi_bus, chip_select)

    # create an analog input channel on pin 0
    input_channel = AnalogIn(mcp, MCP.P0)

    print('Raw ADC Value: ', input_channel.value)
    print('ADC Voltage: ' + str(input_channel.voltage) + 'V')

    last_read = 0       # this keeps track of the last potentiometer value
    tolerance = 250     # to keep from being jittery we'll only change
                        # volume when the pot has moved a significant amount
                        # on a 16-bit ADC


if __name__ == "__main__":
    main()

