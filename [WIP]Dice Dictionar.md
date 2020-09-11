# Dice Dictionary

This dice dictionary is used by the program.
A slightly modified version will be used for logging.
```json
{
    "timestamp": "Fri Jan 17 10:47:13 2020[example]",
    "user": "username",
    "throws":1,
    "dice": [
        ["number of dice", "eyes", "modifier"]
    ],
    "results": [
        [0, 1, 2, 3]
    ]
}
```

> The key `user` contains the username.

> The key `throws` contains the number of times the dice in `dice` shall be thrown.

> The list `dice` contains lorem.

### `Dice`
This:
```json
["number of dice", "eyes", "modifier"]
```
is just a placeholder and the strings should be replaced by
numbers.

`number of dice` : This is an INT representing the number of dice (pl) for this dice, i.e.: **2**d6

`eyes` : This is an INT representing the number of eyes/sides the dice has. I.e.: d**20**

`modifier` : The modifier is an INT representing a fixed value that is being added at the end of the throw, it is seperately displayed, i.e.: 2d20+**2** (individual/non-individual?!s)
