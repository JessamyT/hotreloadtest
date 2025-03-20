import asyncio
from viam.module.module import Module
try:
    from models.mygeneric import Mygeneric
except ModuleNotFoundError:
    # when running as local module with run.sh
    from .models.mygeneric import Mygeneric


if __name__ == '__main__':
    asyncio.run(Module.run_from_registry())
