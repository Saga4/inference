class WorkflowMemoryCache:
    cache = {}

    @classmethod
    def get_dict(cls, namespace):
        return cls.cache.setdefault(namespace, {})

    @classmethod
    def clear_namespace(cls, namespace):
        if namespace in WorkflowMemoryCache.cache:
            del WorkflowMemoryCache.cache[namespace]
