# pyautogui-cli

## Usage

Putting the function name of `pyautogui` as the first argument, and all the arguments (anything inside the parentheses) as the second.

### Example

`pyautogui.moveTo()`:

```
>>> pyautogui.moveTo(100, 200)  # moves mouse to X of 100, Y of 200.
```

should be translated as:

```
$ pyautogui moveTo "100, 200"
```
