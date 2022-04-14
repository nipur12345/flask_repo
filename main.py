# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def hello_python():
   async def speak_async():
      for i in range(100):
         print("Hello I'm nipur, we are in async speak function!")
         return "successfully!"
   value = speak_async()
   print(value,"<<<<<This is the output of the async function")
   # return render_template("index.html")
   return "value"

hello_python()