
<div align="center">
  <p style="text-align:center;">
    <img src="images/pyunitgen.png">
  </p>
</div>

# `Pyunitgen`

Creating a software application or program is an easy task, howerver a great functional software application is a task that require you to master different level of the SDLC, this, my friend is the haderst task for you as a software developer. One of the area that most software developer lake expertize is the ability to write a `unittest`. A unit testing is another application within your application, is like a `RY(Repeat Yourself)` principale. But we do that often when it comes to unittesting our code. `unittest` is the driver of any software application, failed to do that, make your software look like a water basket with unseen hole, when looking into the basket, there is no way you can tell whether the basket has a hole or not, but when trying pouring water into it, you will know that the basket is not in the great shape, so it is your software application. Believe it or not , most of us do a `unittest`, either manually or using a python `unittest tools`, but the question we will ask is , which one is efficient and can proove to other team member, that your code works well.
Some developers want to write the unittest code, but they lake time due to the deadline. Others use manually testing, which in one hand a lot of time consumming, again Others prefer use of `TDD` approach which is double the time of the application delivery. With all that different approaches, do you think that the user cares ?, at the end of the day the `unittest` is made for developers to developers and no one has time to read all your `unittest` codes. So if no one has time to read all your `unittest` codes, can developers fake `unittest`?, yes they can. To make your life easier and solve all above problems, I came up with `pyunitgen`, the first python automatic `unittest` generator that allow you to focus on your actual features. With `pyunitgen`, you are forcing the developer to describe/comment his code and `pyunitgen` will take care of the `unittest`.


## `Requirement`
---
  - `Environment`

    - `Operating System` : GNU/Linux Ubuntu 18.04

  - `Software packages`

    | **Packages** | **Version** |
    |:-------------|:--------------------------------|
    | python   | 3.5+             |


## `How it works`
---

  `pyunitgen` allows you to describe the type of data you need to be generate for your `unittest` using a docstring annotation. 

## `Installation Guide`
---

  - `Automatic installation`

    Download the installation script following the below command.
    ```sh
    ~$ sudo curl -L "https://raw.githubusercontent.com/eirtdev/shell/pyunitgen" -o /usr/local/bin/pyunitgen && sudo chmod +x /usr/local/bin/pyunitgen
    ```

    Now go ahead and run the below command and wait.

    ```sh
    ~$ pyunitgen --help
    ```

## `Getting Start`
---


  - `@apiParam`

    ```py
      @apiParam [{type=typeOfData}] [field=defaultValue]
    ```

    Describe a parameter passed to your Function/Method.

    Usage: @apiParam {Number} id

    | **Name** | **Description** |
    |:---------|:----------------|
    | `{type}`   | Parameter type, e.g. {Boolean}, {Number}, {String}, {Object}, {List} ,{Dict}, ...|
    | `=typeOfData`|The parameters typeOfData e.g =Email, =first_name, =name, =street_address and so on|
    | `[field]`  | Fieldname. |
    | `field`    | Fieldname with brackets define the Variable as optional. |
    |`=defaultValue`| The parameters default value.  |


    - `Examples`
      ```py

      def ask_first_name(first_name):
          '''
          @apiParam {String} first_name
          '''
          if isinstance(first_name, str):
              return True
          return None

      class MyClass:

        def test_unit_with_email(self, test1):
            '''
            @apiParam {String=Email} [test1]

            '''
            pass

        def test_unit_with_default_test2_value_and_string(self, test1, test2):
            '''
            @apiParam {String=first_Name} [test1]

            @apiParam {String} test2="Another String parameter"
            '''
            pass

        def test_unit_with_number_and_string(self, test1, test2):
            '''
            @apiParam {String=first_Name} [test1]

            @apiParam {Number} test2
            '''
            pass
      ```

    - `Supported type`

        | **Name** | **Description** |
        |:---------|:----------------|
        | `Number`   | |
        | `String`   | |        
        | `Boolean`   | |
        | `Dict`   | |
        | `List`   | |

    - `typeOfData`

      This data value represents python `Fake` module data method.

      - `Example`

         To create a fake data in python , we use the below code.

         ```py
          fake=Fake()
          email_address=fake.email()
         ```

         in `pyunitgen` you write `{type=email}`

         ```py
          {String=email}
         ```



  - `@apiReturn`

    ```py
      @apiReturn {type} [value]
    ```

    Describe the return value of your Function/Method. There is a difference between testing a return for a function and testing the return value for an object. This has to be put in mind when using the return annotation. 

    Usage: @apiParam {Number} id

    | **Name** | **Description** |
    |:---------|:----------------|
    | `{type}`   | Parameter type, e.g. {Boolean}, {Number}, {String}, {Object}, {List} ,{Dict}, {apiParam}...|
    | `[value]`  | The return value of the function.This can be any atomic string , boolean, list, dict , number,self or class_name in lower case with another method name  | 

    - `Example`

        Create a folder called `sample` where all, the code will be located.

        Create a file called `pet_main.py` with the below content.

        ```py
        #file: sample/animal.py

        class Animal(object):
          def __init__(self, species):
            self.species = species

          def getSpecies(self):
            return self.species
        ```

        ```py
        #file: sample/pet.py

        from sample.animal import Animal

        class Pet(Animal):
            def __init__(self, name, *args):
                '''
                @apiParam {String} [name]
                @apiParam {String} [args]
                '''
                Animal.__init__(self, *args)
                self._name = name

            def get_name(self):
                '''
                The below declaration make sure that the function return match the value return. This only allow when the class has the init function
                @apiReturn {String}
                '''
                return self._name

            @staticmethod
            def lower(s):
                '''
                @apiParam {String} [s]
                @apiReturn {String}
                '''
                return s.lower()

            def __str__(self):
                return '%s is a %s aged %d' % (

                    self.get_name(),

                    Pet.lower(self.get_species()), self.get_age()

                )

        class Dog(Pet):
            pass

        ```

        ```py
        #file: sample/pet_main.py

        from sample.pet import Pet as AnimalPet, Dog
        from sample.pet import Pet
        from sample.animal import Animal

        def create_pet(name, species, age=0):
            '''
            @apiParam {String} [name]
            @apiParam {String} [species]
            @apiParam {Number=random_int} [age]
            @apiReturn {Object} [Pet(apiParam.name,apiParam.species)]
            '''
            return Pet(name, species).get_name()


        def create_pet_with_empty_return_object(name, species, age=0):
            '''
            @apiParam {String} [name]
            @apiParam {String} [species]
            @apiParam {Number=random_int} [age]
            @apiReturn {Object}
            '''
            return Pet(name, species)


        def create_pet_return_true(name, species, age=0):
            '''
            @apiParam {String} [name]
            @apiParam {String} [species]
            @apiParam {Number=random_int} [age]
            @apiReturn {String}
            '''
            return Pet(name, species).getSpecies()


        def create_animal(species):
            '''
            @apiParam {String} [species]
            @apiReturn {Object}
            '''
            return Animal(species)


        def create_pet_return_false(name, species, age=0):
            '''
            @apiParam {String} [name]
            @apiParam {String} [species]
            @apiParam {Number=random_int} [age]
            @apiReturn {Boolean} [False]
            '''
            Pet(name, species)
            return False

        def create_pet_return_none(name, species, age=0):
            '''
            @apiParam {String} [name]
            @apiParam {String} [species]
            @apiParam {Number} [age]
            @apiReturn {Boolean} [False]    
            '''
            Pet(name, species)
        ```

      - `Output`

        ```py
          from sample.pet_main import create_pet,create_pet_with_empty_return_object,create_pet_return_true,create_animal,create_pet_return_false,create_pet_return_none
          from sample.pet import Pet as AnimalPet
          from sample.pet import Dog
          from sample.pet import Pet
          from sample.animal import Animal
          import unittest

              
          class pet_mainTest(unittest.TestCase):
              """
              Tests for functions in the "pet_main" file.
              """

              @classmethod
              def setUpClass(cls):
                  pass #TODO

              @classmethod
              def tearDownClass(cls):
                  pass #TODO

              def setUp(self):
                  pass #TODO

              def tearDown(self):
                  pass #TODO
              
              def test_create_pet(self):
                  
                  pet_main = create_pet(name='Erika Perkins',species='Charlene Torres',age=9858) 
                  
                  self.assertEqual(pet_main, Pet('Erika Perkins','Charlene Torres')) 

              def test_create_pet_with_empty_return_object(self):
                  
                  pet_main = create_pet_with_empty_return_object(name='Lynn Russell',species='Jonathan Boyd',age=7279) 
                  
                  self.assertIsInstance(pet_main, Pet) 

              def test_create_pet_return_true(self):
                  
                  pet_main = create_pet_return_true(name='Christopher Campbell',species='Mia Robertson',age=9057) 
                  
                  self.assertEqual(pet_main, 'Christopher Campbell') 

              def test_create_animal(self):
                  
                  pet_main = create_animal(species='Malik Holloway') 
                  
                  self.assertIsInstance(pet_main, Animal) 

              def test_create_pet_return_false(self):
                  
                  pet_main = create_pet_return_false(name='Joshua Johnson',species='Christopher Jackson',age=4464) 
                  
                  self.assertFalse(pet_main,False)

              def test_create_pet_return_none(self):
                  
                  pet_main = create_pet_return_none(name='Ashley Aguilar',species='Richard Taylor',age=910676837) 
                  
                  self.assertFalse(pet_main,False)
        ```

      ```py
      username = None

      def name():
          '''
          @apiReturn {String} [Evarist]
          '''
          return "Evarist"


      def set_username(name):
          '''
          @apiParam {String} [name]
          @apiReturn {Boolean} [True]
          '''
          global username
          username = name
          return True


      def get_username():
          global username
          return username


      def test_boolean_true(first_name):
          '''
          @apiParam {String} first_name
          @apiReturn {Boolean} [True]
          '''
          if isinstance(first_name, str):
              return True
          return None


      def test_boolean_false(first_name):
          '''
          @apiParam {String} first_name
          @apiReturn {Boolean} [False]    
          '''
          if not isinstance(first_name, str):
              return False
      ```

        ```py
        class Person:
            name = []

            def set_name(self, user_name):
                '''
                @apiParam {String} [user_name]
                @apiReturn {apiParam.user_name} [self.get_name(0)]
                '''
                self.name.append(user_name)
                return len(self.name) - 1

            def get_name(self, user_id):
                '''
                @apiParam {Number} [user_id=1]
                @apiReturn {String} [There is no such user]
                '''
                if user_id >= len(self.name):
                    return 'There is no such user'
                else:
                    return self.name[user_id]
        ```

        ```py
        from .server import Server

        class AnchorPeer:

            def __init__(self, name, org_name=None):

                self.name = name
                self.org_name = org_name
                self.server = Server()

            def dump(self):
                if self.org_name.lower() not in self.server.host:
                    self.server.host = "{}.{}".format(
                        self.org_name.lower(), self.server.host)

                return "\n\n\n\t\t\t- Host: {}.{}\n\t\t\t  Port: {}".format(self.name, self.server.host, self.server.port)

            def test_unit_that_return_dict(self):
                '''
                @apiReturn {Number} [{"name":4}]
                '''
                print("hi there ")
                return

            def test_unit_that_return_dict_with_a_dictionary_type(self):
                '''
                @apiReturn {Dict} [{"name":4}]
                '''
                print("hi there ")
                return

            def test_unit_with_email(self, test1):
                '''
                @apiParam {String=Email} [test1]

                @apiReturn {Boolean} [True]
                '''
                pass

            def test_unit_with_default_test2_value_and_string(self, test1, test2):
                '''
                @apiParam {String=first_Name} [test1]

                @apiParam {String} test2="Fangnikoue Evarist"

                @apiReturn {Boolean} [True]
                '''
                pass

            def test_unit_with_number_and_string(self, test1, test2):
                '''
                @apiParam {String=first_Name} [test1]

                @apiParam {Number} test2

                @apiReturn {Boolean} [True]
                '''
                pass

            def test_unit_with_address(self, address):
                '''
                @apiParam {String=street_address} [address]

                @apiReturn {Boolean} [True]
                '''
                pass

            def test_unit_with_boolean_and_string(self, test1, test2):
                '''
                @apiParam {String} [test1]

                @apiParam {Boolean} [test2]

                @apiReturn {Boolean} [True]
                '''
                pass

            def test_unit_that_return_a_list(self, test1, test2):
                '''
                @apiReturn {Number} [1,2,3,4]
                '''
                pass

            def test_unit_that_return_a_list_with_a_list_type(self, test1, test2):
                '''
                @apiReturn {List} [1,2,3,4]
                '''
                pass

            def test_unit_3(self, test1, test2):
                '''


                '''
                pass

            def test_unit_4(self, test1, test2):
                pass
        ```

  
## `Pyunitgen command line options`

  | **Option** | **Description** |
  |:---------|:----------------|
  | `{type}`   | Parameter type, e.g. {Boolean}, {Number}, {String}, {Object}, {List} ,{Dict}, {apiParam}...|
  | `[value]`  | The return value of the function.This can be any atomic string , boolean, list, dict , number,self or class_name in lower case with another method name  | 


  parser.add_argument('module',
                    help='The module directory')

parser.add_argument('-F', '--footer',
                    help='File to use as a footer.')
parser.add_argument('-H', '--header',
                    help='File to use as a header.')
parser.add_argument('-X', '--exclude', action='append', default=[],
                    help='Add a child directory name to exclude.')

parser.add_argument('-f', '--force', action='store_true',
                    help='Force files to be generated, even if they already exist.')
parser.add_argument('-i', '--internal', action='store_true',
                    help='Include internal classes and methods starting with a _.')
parser.add_argument('-m', '--test-module', default='test',
                    help='The path of the test module to generate.')
parser.add_argument('-p', '--test-prefix', default='test_',
                    help='The prefix for test files.')
parser.add_argument('-t', '--tab-width', type=int,
                    help='The width of a tab in spaces (default actual tabs).')

parser.add_argument('-nw', '--no-watch', default=False, action='store_true',
                    help='Do not watch the directory. When the file been modified.')