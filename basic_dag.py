from ray import serve

@serve.deployment(
    ray_actor_options={
        "num_cpus": 0.1,
    },
    autoscaling_config={
        "target_ongoing_requests": 2,
        "min_replicas": 0,
        "max_replicas": 5,
    }
)
def f(*args):
    return "wonderful world"


@serve.deployment(
    ray_actor_options={
        "num_cpus": 0.1,
    },
    autoscaling_config={
        "target_ongoing_requests": 2,
        "min_replicas": 0,
        "max_replicas": 5,
    }
)
class BasicDriver:
    def __init__(self, h):
        self._h = h.options(use_new_handle_api=True)

    async def __call__(self):
        return await self._h.remote()


FNode = f.bind()
DagNode = BasicDriver.bind(FNode)
