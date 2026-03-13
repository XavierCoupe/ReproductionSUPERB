## How to use it

### Environment initialisation

Make sure you have venv or conda environmnent before doing this step. We consider using **python=3.10** for the following.
You just have to launch

```sh
./init_env.sh
```

and all needed module ll'be installed into your environment.

One error can occure, if it's

_class Registry(collections.MutableMapping):
    AttributeError: module 'collections' has no attribute 'MutableMapping'_

from **catalyst** module, then you have to modify the _/python3.10/site-packages/catalyst/registry/registry.py_ file from your enironment.
Change class Registry(collections.MutableMapping) ==> class Registry(collections.**abc**.MutableMapping) and the rest should work.
### Downstream Task

For each task, you can use the following instruction at :

**s3prl/downstream/README.md**

You don't have to install any libraries, you just have to install corpora and update path into the .yaml provide.


### Limit

The following tasks may not work :

    * QbE
    
    * SD
    
    * SS
    
    * SE
    
    * VC
    
    * ST
    
    * OOD-ASR

