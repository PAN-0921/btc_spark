### Install dependency
#### pre-requisite: install pipenv
```
brew install pipenv
```
#### dependency
```
source virtual-local
pipenv install
```
#### activate
```
pipenv shell
```
### Local Dev Environment
#### run map reduce example
```
python -m demo.mapre.reduce_service
```

### Directory
data: store CSV files
lib: store variables and functions
src: run pyspark.sql to generate results

### Example
```bash
python src/testBlocksizeMonth.py
```