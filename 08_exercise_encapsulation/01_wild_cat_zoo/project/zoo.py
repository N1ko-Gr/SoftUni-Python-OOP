from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self,name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self,animal, price):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif len(self.animals) < self.__animal_capacity and self.__budget < price:
            return "Not enough budget"
        return f"Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        w = next((w for w in self.workers if w.name == worker_name), None)
        if w:
            self.workers.remove(w)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = sum(w.salary for w in self.workers)
        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_need_for_tend = sum(a.money_for_care for a in self.animals)
        if self.__budget >= total_need_for_tend:
            self.__budget -= total_need_for_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetahs = []
        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                lions.append(repr(animal))
            if animal.__class__.__name__ == 'Tiger':
                tigers.append(repr(animal))
            if animal.__class__.__name__ == 'Cheetah':
                cheetahs.append(repr(animal))

        result = [f'You have {len(self.animals)} animals', f'----- {len(lions)} Lions:']
        result.extend(lions)
        result.append(f'----- {len(tigers)} Tigers:')
        result.extend(tigers)
        result.append(f'----- {len(cheetahs)} Cheetahs:')
        result.extend(cheetahs)
        return '\n'.join(result)

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []

        for worker in self.workers:
            if worker.__class__.__name__ == 'Keeper':
                keepers.append(repr(worker))
            if worker.__class__.__name__ == 'Caretaker':
                caretakers.append(repr(worker))
            if worker.__class__.__name__ == 'Vet':
                vets.append(repr(worker))

        result = [f'You have {len(self.workers)} workers', f'----- {len(keepers)} Keepers:']
        result.extend(keepers)
        result.append(f'----- {len(caretakers)} Caretakers:')
        result.extend(caretakers)
        result.append(f'----- {len(vets)} Vets:')
        result.extend(vets)
        return '\n'.join(result)

