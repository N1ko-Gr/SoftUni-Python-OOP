from List.extended_list import IntegerList


from unittest import TestCase, main


class TestIntegerList(TestCase):

    def setUp(self):
        self.list = IntegerList(1, 2, 3, 4, 5)

    def test_init_list(self):
        list = IntegerList()
        self.assertEqual(list.get_data(), [])

        list = IntegerList(1, 2, 3, 4, 5)
        self.assertEqual(list.get_data(), [1, 2, 3, 4, 5])

    def test_add_element(self):
        list = IntegerList()
        list.add(10)
        self.assertEqual(list.get_data(), [10])

    def test_add_element_value_error(self):
        list = IntegerList()
        with self.assertRaises(ValueError) as ex:
            list.add("ten")

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_element(self):
        list = IntegerList(1, 2, 3, 4, 5)
        list.remove_index(2)
        self.assertEqual(list.get_data(), [1, 2, 4, 5])

    def test_remove_element_index_error(self):
        list = IntegerList(1, 2, 3, 4, 5)
        with self.assertRaises(IndexError) as ex:
            list.remove_index(6)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_item(self):
        list = IntegerList(1, 2, 3, 4, 5)
        self.assertEqual(list.get(2), 3)


    def test_get_item_index_error(self):
        list = IntegerList(1, 2, 3, 4, 5)
        with self.assertRaises(IndexError) as ex:
            list.get(5)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert(self):
        list = IntegerList(1, 2, 3, 4, 5)
        list.insert(2, 10)
        self.assertEqual(list.get_data(), [1, 2, 10, 3, 4, 5])

    def test_insert_index_error(self):
        list = IntegerList(1, 2, 3, 4, 5)
        with self.assertRaises(IndexError) as ex:
            list.insert(6, 10)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_value_error(self):
        list = IntegerList(1, 2, 3, 4, 5)
        with self.assertRaises(ValueError) as ex:
            list.insert(2, "ten")

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_get_biggest_value(self):
        list = IntegerList(1, 2, 3, 4, 5)
        self.assertEqual(list.get_biggest(), 5)

    def test_get_index_value(self):
        list = IntegerList(1, 2, 3, 4, 5)
        self.assertEqual(list.get_index(3), 2)


if __name__ == '__main__':
    main()