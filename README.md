
<div align="center">
  <p style="text-align:center;">
    <img src="images/pyunitgen.png">
  </p>
</div>

# `Pyunitgen`

Creating a software application or program is an easy task, howerver a great functional software application is a task that require you to master different level of the SDLC, this, my friend is the haderst task for you as a software developer. One of the area that most software developer lake expertize is the ability to write a `unittest`. A unit testing is another application within your application, is like a `RY(Repeat Yourself)` principale. But we do that often when it comes to unittesting our code. `unittest` is the driver of any software application, failed to do that, make your software look like a water basket with unseen hole, when looking into the basket, there is no way you can tell whether the basket has a hole or not, but when trying pouring water into it, you will know that the basket is not in the great shape, so it is your software application.
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

    Describe the return value of your Function/Method.

    Usage: @apiParam {Number} id

    | **Name** | **Description** |
    |:---------|:----------------|
    | `{type}`   | Parameter type, e.g. {Boolean}, {Number}, {String}, {Object}, {List} ,{Dict}, {apiParam}...|
    | `[value]`  | The return value of the function.This can be any atomic string , boolean, list, dict , number,self or class_name in lower case with another method name  | 

    - `Example`

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