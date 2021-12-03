# Warning
This code may not beautiful or powerful

## Using
```python
import Correcting

commands = ["Test", "Tet"]
correct = Correcting.Correcting(commands)

command = input("Enter commands here >>> ")

if command not in commands:
    c = correct.correct(command)
    print(f"May u mean {c}")
```

```shell
Input: Tes
Output: May u mean Test
```
# Enjoy