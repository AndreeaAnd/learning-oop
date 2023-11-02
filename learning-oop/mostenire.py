# class A:
#
#     def method_a(self):
#         print('Sunt in A')
#
#
# class B(A):
#
#     def method_a(self):
#         super().method_a()
#         print('Sunt tot in B')
#
#     def method_b(self):
#         print('Sunt in B')
#
#
# class C(B):
#     def method_a(self):
#         print('Sunt in C')
#
#
# test = B()
# test.method_a()
# test.method_b()
#
# test_c = C()
# test_c.method_a()
# test_c.method_b()
#
#
# print(C.__mro__)
# print(C.mro())


# list = [0, 1, 2, 3, 4]
# list.append(5)
# print(list)

