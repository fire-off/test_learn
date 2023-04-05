# import unittest
# class Search:
#
#   def search_fun(self):
#     print("search")
#     return True
#
# class TestSearch(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:
#         print("setupclass")
#         cls.search=Search()
#     @classmethod
#     def tearDownClass(cls) -> None:
#         print("teardown class")
#         cls.search=Search()
#     def test_search1(self):
#         print("testsearch1")
#         # search=Search()
#         assert True==self.search.search_fun()
#
#     def test_search2(self):
#         print("testsearch2")
#         # search=Search()
#         assert True==self.search.search_fun()
#     def test_search3(self):
#         print("testsearch3")
#         # search=Search()
#         assert True==self.search.search_fun()
#     def test_equal(self):
#         print("断言相等")
#         self.assertEqual(1,1,"判断1=1")
# class TestSearch1(unittest.TestCase):
#     def test_case1(self):
#         print("testcase1")
#     def test_case2(self):
#         print("testcase2")
# class Tesrsearch2(unittest.TestCase):
#     def tesr_search1(self):
#         print("ceshi ")
#     def tesr_search2(self):
#         print("ceshi1 ")
#
#
#
#
# if __name__=="__main__":
#
#     # # suite.addTest(TestSearch("test_search1"))
#     # # suite.addTest(TestSearch("test_search2"))
#     suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
#     suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch1)
#     suite = unittest.TestSuite([suite1,suite2])
#     unittest.TextTestRunner(verbosity=2).run(suite)

