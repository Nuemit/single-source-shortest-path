# single-source-shortest-path

# how to use
```py
from main import Djikstra

Djk = Djikstra(0,0,7)

sample_dict = Djk.get_sample_dict()

Djk.set_graph(sample_dict)

Djk.get_shortest_path()
```

Output:
> [0, 4, 5, 6, 7]
