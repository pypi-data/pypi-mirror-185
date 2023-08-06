Project daskcheck
=================

This should allow an easy use of **dask**.

Instalation
-----------

``` {.example}
pip install daskcheck
```

Usage
-----

``` {.python}
from daskcheck import daskcheck

from fire import Fire
import time
import platform
import datetime as dt
import json

def main( parlist ):
    parameters = daskcheck.prepare_params( parlist )

    if type(parameters)==list:
        print("i... viable for DASK ....")
        daskcheck.submit( daskcheck.get_cpu_info , parameters)
    else:
        print("i... running only locally")
        my_results = xcorefunc( 1 , parameters )
        # Write LOG file.
        now = dt.datetime.now()
        stamp = now.strftime("%Y%m%d_%H%M%S")
        with open(f"dask_results_log_{stamp}.json", "w") as fp:
            json.dump( my_results , fp, sort_keys=True, indent='\t', separators=(',', ': '))
    return

def xcorefunc( order, param):
    """
    Function to be sent to dask server with order# + parameter
    """
    import ROOT # I need to avoid breaking pickle
    start_time = time.perf_counter()

    return order, [platform.node(),  f"{time.perf_counter() - start_time:.1f} s" , ni]


if __name__=="__main__":
    Fire(main)

```
