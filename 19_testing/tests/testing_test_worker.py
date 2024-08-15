from test_worker import Worker


from unittest import TestCase, main


class WorkerTests(TestCase):
    def test_worker_init(self):
        worker = Worker('John Doe', 3000, 100)
        self.assertEqual(worker.name, 'John Doe')
        self.assertEqual(worker.salary, 3000)
        self.assertEqual(worker.energy, 100)
        self.assertEqual(worker.money, 0)

    def test_worker_raise_exception(self):
        worker = Worker('John Doe', 3000, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

        worker = Worker('John Doe', 3000, -1)
        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))


    def test_work(self):
        worker = Worker('John Doe', 3000, 100)
        worker.work()
        self.assertEqual(worker.money, 3000)
        self.assertEqual(worker.energy, 99)


    def test_worker_rest(self):
        worker = Worker('John Doe', 3000, 100)
        worker.rest()
        self.assertEqual(worker.energy, 101)

    def test_worker_get_info(self):
        worker = Worker('John Doe', 3000, 100)
        info = worker.get_info()
        self.assertEqual(info, 'John Doe has saved 0 money.')



if __name__ == '__main__':
    main()