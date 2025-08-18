class EventBus:
    def __init__(self):
        self._subs = {}

    def on(self, name, cb):
        self._subs.setdefault(name, []).append(cb)

    def emit(self, name, payload=None):
        for cb in self._subs.get(name,[]):
            cb(payload or {})