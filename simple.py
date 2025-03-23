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
class BasicDriver:
    def __init__(self):
        pass

    async def __call__(self):
        return "wonderful world"


DagNode = BasicDriver.bind()
