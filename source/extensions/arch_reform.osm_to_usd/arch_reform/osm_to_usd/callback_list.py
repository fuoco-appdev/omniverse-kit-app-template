class CallbackList(list):
     def call(self, *args, **kwargs):
         for listener in self:
             listener(*args, **kwargs)