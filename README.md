# APROS MCDL Data file (JSON) to Image (PNG)

## Requirements

- Python 3.7

## Installation

```bash
pip install
```

### Dependencies

- [`scipy`](https://scipy.org/)
- [`matplotlib`](https://matplotlib.org/)

## Configuration

- `main.py`에서 JSON 데이터 경로 수정
- Windows의 경우 `C:\\Users\\eunchurn\\APROS\\36-20191120` 방식으로 수정

```python
# JSON 데이터 폴더 지정
json_path = '/Users/eunchurn/APROS/36-20191120'
```

- `main.py`에서 출력 폴더 지정
- Windows의 경우 `C:\\Users\\eunchurn\\APROS\\36-2019112\png` 방식으로 수정

```python
# PNG 출력 저장할 폴더 지정
output_path = '/Users/eunchurn/APROS/36-20191120/png'
```

## Run script

```python
python main.py
```
