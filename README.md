# btc_spark

## Setup

```bash
pipenv install
pipenv shell
```

## Test Usage

```bash
python src/test/test_blocksize_month.py
```

Similarly, any test can be run by `python src/test/test_*.py`

- `test_blocksize_month.py`: the test to use spark to figure out blocksize were traded in each month in 2018 and 2019
- `test_load_csv_from.py`: the test to load csv file as DataFrame
- `test_aggregate_blocks.py`: the test to aggregate certain column(e.g. "blockCount") by sum and return the result.


## Data Source

https://www.kaggle.com/mczielinski/bitcoin-historical-data

Bitcoin is the longest running and most well known cryptocurrency, first released as open source in 2009 by the anonymous Satoshi Nakamoto. Bitcoin serves as a decentralized medium of digital exchange, with transactions verified and recorded in a public distributed ledger (the blockchain) without the need for a trusted record keeping authority or central intermediary. Transaction blocks contain a SHA-256 cryptographic hash of previous transaction blocks, and are thus "chained" together, serving as an immutable record of all transactions that have ever occurred. As with any currency/commodity on the market, bitcoin trading and financial instruments soon followed public adoption of bitcoin and continue to grow. Included here is historical bitcoin market data at 1-min intervals for select bitcoin exchanges where trading takes place. Happy (data) mining!
