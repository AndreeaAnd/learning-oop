# class Singleton:
#     _instance=None
#
#     def __new__(self, *args, **kwargs):
#         if self._instance is None:
#             print('Creating Singleton')
#             self._instance=super().__new__(self, *args, **kwargs)
#         else:
#             print('Already created, returning the existing one')
#         return self._instance
#
#
# class DatabaseConnection(Singleton):
#     pass
#
# a=DatabaseConnection()
# b=DatabaseConnection()
# c=DatabaseConnection()
#
# print(a)
# print(b)
# print(a is b)




x=Person('John', 'Doe')
print(x)
