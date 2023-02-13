# single-source-shortest-path
## LIMITATION
only with Integer Dictionarys.

## known bugs
if the dictionary does not start with 0 you get an 
> IndexError: list index out of range


# How to use plain
```py
from main import Djikstra

Djk = Djikstra(0,0,7)

sample_dict = Djk.get_sample_dict()

Djk.set_graph(sample_dict)

Djk.get_shortest_path()
```

Output:
> [0, 4, 5, 6, 7]

# How to use Custom
```py
from main import Djikstra

my_nodes = {
    '0': { '1': 1, '2': 4 },
    '1': { '0': 1, '3': 6 },
    '2': { '0': 1, '3': 2, '4': 4},
    '3': { '1': 6, '2': 2 },
    '4': { '2': 4, '5': 5 },
    '5': { '4': 5 }    
}

Djk = Djikstra(1, 4, 5)
Djk.set_graph(my_nodes)
Djk.get_shortest_path()
```

Output:
> [1, 0, 2, 4, 5]
