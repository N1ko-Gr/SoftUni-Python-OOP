from typing import List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:

    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self,equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = next((x for x in self.subscriptions if x.id == subscription_id), None)

        customer = next((x for x in self.customers if x.id == subscription.customer_id), None)
        trainer = next((x for x in self.trainers if x.id == subscription.trainer_id), None)
        equipment = next((x for x in self.equipment if x.id == subscription.exercise_id), None)
        plan = next((x for x in self.plans if x.id == subscription.exercise_id), None)

        return (f"{subscription.__repr__()}\n"
                f"{customer.__repr__()}\n"
                f"{trainer.__repr__()}\n"
                f"{equipment.__repr__()}\n"
                f"{plan.__repr__()}")

