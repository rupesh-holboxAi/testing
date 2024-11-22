# import unittest

# class TestSyncFunctions(unittest.TestCase):
#     def test_reconcile_inventory(self):
#         bricklink_data = [{'itemNo': '123', 'quantity': 5}]
#         brickowl_data = [{'sku': '123', 'quantity': 3}]
#         discrepancies = reconcile_inventory(bricklink_data, brickowl_data)
#         self.assertEqual(len(discrepancies), 1)
#         self.assertEqual(discrepancies[0]['brickowl_qty'], 3)

# if __name__ == '__main__':
#     unittest.main()
