# eokulapi
eokul vbs api

## install
`pip install eokulapi`

## usage
```python
from eokulapi.eokulapi import EokulAPI

user=EokulAPI(uid=...)
st=user.students[0]
user.update_student_data(st)
...
```