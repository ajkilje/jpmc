# ExampleAssignment_StockMarket

This project provides a Python script for analyzing stock exchange data, including calculating dividend yield, P/E ratio, volume weighted stock price, and the GBCE All Share Index.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Sample Usage](#sample-usage)

## Introduction

This Python script is designed to fulfill the requirements of analyzing stock exchange data provided in the project requirements. It includes functionality to calculate dividend yield, P/E ratio, volume weighted stock price, and the GBCE All Share Index.

## Requirements

The script requires Python to be installed on your system. It uses standard Python libraries such as `datetime` and `numpy`.

## Usage

1. Clone the repository to your local machine:
git clone <repository-url>

2. Run the Python script `ExampleAssignment_StockMarket.py` using Python:
python ExampleAssignment_StockMarket.py

3. Follow the instructions in the script to perform various analyses on the provided stock exchange data.

## Sample Usage

Here's a sample usage of the script:

```python
# Sample usage of the StockExchange class
gbce = StockExchange()
gbce.add_stock('TEA', 'Common', 0, np.nan, 100)
gbce.add_stock('POP', 'Common', 8, np.nan, 100)
gbce.record_trade('TEA', 10, 'Buy', 110)
gbce.record_trade('POP', 20, 'Sell', 90)
print("Dividend Yield for TEA:", gbce.calculate_dividend_yield('TEA', 110))
print("P/E Ratio for POP:", gbce.calculate_pe_ratio('POP', 90))
print("Volume Weighted Stock Price for TEA:", gbce.calculate_volume_weighted_stock_price('TEA'))
print("GBCE All Share Index (Geometric Mean of Prices):", gbce.calculate_geometric_mean())
