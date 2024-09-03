from abc import ABC, abstractmethod
from typing import List, Dict

class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """
    
    @abstractmethod
    def attach(self, observer: 'Observer', interest: str) -> None:
        pass

    @abstractmethod
    def detach(self, observer: 'Observer', interest: str) -> None:
        pass

    @abstractmethod
    def notify(self, condition: str) -> None:
        pass

class WeatherNotifier(Subject):
    """
    The WeatherNotifier owns the weather condition state and notifies observers
    when the condition changes.
    """
    
    _observers: Dict[str, List['Observer']] = {
        "cold": [],
        "warm": [],
        "rainy": [],
        "sunny": [],
        "windy": []
    }
    
    def attach(self, observer: 'Observer', interest: str) -> None:
        if interest in self._observers:
            self._observers[interest].append(observer) # add obsevers to weather to specific weather
            print(f"Observer {observer.name} subscribed to {interest} weather.")

    def detach(self, observer: 'Observer', interest: str) -> None:
        if interest in self._observers:
            self._observers[interest].remove(observer)
            print(f"Observer {observer.name} unsubscribed from {interest} weather.")

    def notify(self, condition: str) -> None:
        if condition in self._observers:
            print(f"\nNotifying observers about {condition} weather:")
            for observer in self._observers[condition]:
                observer.update(condition)

    def check_weather(self, condition: str) -> None:
        condition = condition.strip().lower()
        if condition in self._observers:
            self.notify(condition)
        else:
            print(f"No observers subscribed to {condition} weather.")

class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """
    
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def update(self, condition: str) -> None:
        pass

class ConcreteObserver(Observer):
    """
    ConcreteObserver reacts to the updates issued by the WeatherNotifier
    when the condition matches their interest.
    """
    
    def update(self, condition: str) -> None:
        print(f"{self.name} is notified: The condition is {condition} now.")

if __name__ == "__main__":
    # Create the subject 
    notifier = WeatherNotifier()

    # Create observers with their names
    observer1 = ConcreteObserver("Abebe")
    observer2 = ConcreteObserver("Getahun")
    observer3 = ConcreteObserver("Chala")
    observer4 = ConcreteObserver("jhon")
    observer5 = ConcreteObserver("messi")

    # Attach observers with their interests
    notifier.attach(observer1, "cold")
    notifier.attach(observer2, "warm")
    notifier.attach(observer3, "rainy")
    notifier.attach(observer4, "sunny")
    notifier.attach(observer5, "windy")

    #event to the subject to notify observers
    test_condition = "windy"  
    notifier.check_weather(test_condition)
