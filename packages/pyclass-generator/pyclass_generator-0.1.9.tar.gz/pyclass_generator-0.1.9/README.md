# pyclass-generator

## How to develop?

1. create a source distribution after updating this source.

   ```bash
   python setup.py sdist
   ```

2. regiser your package to `PyPi`

    ```bash
    twine upload --skip-existing dist/*
    ```

## Install Package

    - using github url
        ```bash
        $ pip install -e git+https://github.com/Venus713/pyclass-generator.git#egg=pyclass-generator
        ```

    - using pip
        ```bash
        $ pip install pyclass-generator
        ```

## How to use it?

    - example

        ```python
            import os
            from pathlib import Path
            from pyclass_generator import main


            if __name__ == '__main__':
                BASE_DIR: Path = Path(__file__).resolve().parent
                DEST_DIR: Path = os.path.join(BASE_DIR, ".storage")
                data = {
                    "ex1.py": {
                        "classes": [{
                            "name": "test",
                            "description": "This is a test class.",
                            "base_classes": ["ABC"],
                            "attributes": [
                                {
                                    "name": "a",
                                    "type": "int",
                                    "value": "3"
                                },
                                {
                                    "name": "b",
                                    "type": "str",
                                    "value": "4"
                                },
                                {
                                    "name": "c",
                                    "type": "bool",
                                    "value": "True"
                                }
                            ],
                            "instance_attributes": [{
                                "name": "test",
                                "value": "None",
                                "type": "str"
                            }],
                            "instance_methods": [
                                {
                                    "definition": {
                                        "decorators": ["staticmethod"],
                                        "name": "add_card",
                                        "arguments": [
                                            {
                                                "name": "a",
                                                "type": "int",
                                                "value": "1"
                                            },
                                            {
                                                "name": "b",
                                                "type": "str",
                                                "value": "None"
                                            }
                                        ],
                                        "statements": ["a = b", "return a"],
                                        "return_type": "str"
                                    }
                                },
                                {
                                    "github": {
                                        "url": "https://github.com/Venus713/pytestsource.git",
                                        "filename": "blackjack.py",
                                        "target": "deal"
                                    }
                                },
                            ]
                        }],
                        "functions": [
                            {
                                "definition": {
                                    "decorators": ["my_decorator"],
                                    "name": "abc",
                                    "arguments": [
                                        {
                                            "name": "player",
                                            "type": "int",
                                            "value": "1"
                                        },
                                        {
                                            "name": "dealer",
                                            "type": "str",
                                            "value": "None"
                                        }
                                    ],
                                    "statements": ["a = b", "return a"],
                                    "return_type": "str"
                                }
                            },
                            {
                                "github": {
                                    "url": "https://github.com/Venus713/pytestsource.git",
                                    "filename": "blackjack.py",
                                    "target": "hit_or_stand"
                                }
                            }
                        ],
                        "imports": ["import my_decorator", "from datetime import datetime"],
                        "data_structures": [{"name": 'player', "expression": 99}, {"name": "dealer", "expression": [9, "hello", ["list2", 14, {}]]}]
                    },
                    "ex2.py": {
                        "classes": [],
                        "functions": [],
                        "imports": [],
                        "data_structures": []
                    }
                }
                pyclass = main(data, DEST_DIR)
        ```

    - output(`ex.py` is saved to `.storage` folder)

        ```python

            import my_decorator
            from datetime import datetime
            player = 99
            dealer = [9, 'hello', ['list2', 14, {}]]
            class Test(ABC):
                '''
                This is a test class.
                '''

                a: int = 3

                b: str = 4

                c: bool = True
                def test_method(self):
                    self.test = None

                @property
                def test(self, test: str) -> str:
                    return self._test

                @test.setter
                def test(self, test : str) -> str:
                    self._test = test

                @staticmethod
                def add_card(a: int = 1, b: str = None, ) -> str:
                    a = b
                    return a

                def deal(self):
                    single_card = self.deck.pop()
                    return single_card

            @my_decorator
            def abc(player: int = 1, dealer: str = None, ) -> str:
                a = b
                return a


            def hit_or_stand(deck, hand):
                global playing

                while True:
                    x = input("\nWould you like to Hit or Stand? Enter [h/s] ")

                    if x[0].lower() == "h":
                        hit(deck, hand)  # hit() function defined above

                    elif x[0].lower() == "s":
                        print("Player stands. Dealer is playing.")
                        playing = False

                    else:
                        print("Sorry, Invalid Input. Please enter [h/s].")
                        continue
                    break
        ```
