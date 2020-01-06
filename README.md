# APROS MCDL Data file (JSON) to Image (PNG)

[![Actions Status](https://github.com/eunchurn/data-to-image/workflows/Python%20application/badge.svg)](https://github.com/eunchurn/data-to-image/actions) [![Build Status](https://travis-ci.org/eunchurn/data-to-image.svg?branch=master)](https://travis-ci.org/eunchurn/data-to-image)

수집된 4채녈 가속도 데이터 Time domain, Frequency domain (Power spectral density)를 이미지 파일로 출력

## Requirements

- [Python 3.7](https://www.python.org/downloads/release/python-374/)

## Installation

```bash
pip install -r requirements.txt
```

### Dependencies

- [`scipy`](https://scipy.org/)
- [`matplotlib`](https://matplotlib.org/)

## Configuration

### 데이터 폴더 지정

- `main.py`을 열고 JSON 데이터 경로 수정
- Windows의 경우 `C:\\Users\\eunchurn\\APROS\\36-20191120` 방식으로 수정

```python
# JSON 데이터 폴더 지정
json_path = '/Users/eunchurn/APROS/36-20191120'
```

### 출력 폴더 지정

- `main.py`열고 출력 폴더 지정
- Windows의 경우 `C:\\Users\\eunchurn\\APROS\\36-2019112\png` 방식으로 수정

```python
# PNG 출력 저장할 폴더 지정
output_path = '/Users/eunchurn/APROS/36-20191120/png'
```

## Run script

```python
python main.py
```

## Result

Result will be in `output_path` as `png` files.

![result1](doc/1574177392234.png)
![result2](doc/1574221804469.png)
