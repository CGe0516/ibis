from multipledispatch import Dispatcher

import ibis.backends.pandas.core as core_dispatch
import ibis.backends.pandas.dispatch as pandas_dispatch
from ibis.backends.dask.trace import TraceTwoLevelDispatcher

execute_node = TraceTwoLevelDispatcher('dask_execute_node')
for types, func in pandas_dispatch.execute_node.funcs.items():
    execute_node.register(*types)(func)

execute = Dispatcher('dask_execute')
execute.funcs.update(core_dispatch.execute.funcs)

pre_execute = Dispatcher('dask_pre_execute')
pre_execute.funcs.update(core_dispatch.pre_execute.funcs)

execute_literal = Dispatcher('dask_execute_literal')
execute_literal.funcs.update(core_dispatch.execute_literal.funcs)

post_execute = Dispatcher('dask_post_execute')
post_execute.funcs.update(core_dispatch.post_execute.funcs)
