from test_cat import Cat


from unittest import TestCase, main


class CatTests(TestCase):
    def test_cat_init(self):
        cat = Cat("Fatty")
        self.assertEqual(cat.name, "Fatty")
        self.assertEqual(cat.fed, False)
        self.assertEqual(cat.sleepy, False)
        self.assertEqual(cat.size, 0)

    def test_cat_eat(self):
        cat = Cat("Fatty")
        cat.eat()
        self.assertEqual(cat.fed, True)
        self.assertEqual(cat.sleepy, True)
        self.assertEqual(cat.size, 1)

    def test_cat_raise_exception(self):
        cat = Cat("Fatty")
        with self.assertRaises(Exception) as ex:
            cat.eat()
            cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_cat_sleepy(self):
        cat = Cat("Fatty")
        cat.eat()
        cat.sleep()
        self.assertEqual(cat.sleepy, True)

    def test_cat_sleep_exception(self):
        cat = Cat("Fatty")
        with self.assertRaises(Exception) as ex:
            cat.sleep()
            cat.eat()

        self.assertEqual("Cannot sleep while hungry", str(ex.exception))


if __name__ == '__main__':
    main()