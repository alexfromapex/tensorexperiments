import tensorflow as tf

def main():
    if any(["GPU" in device for device in tf.config.list_physical_devices()]):
        print("Congratulations, you have GPU support for TensorFlow! \U0001F389")
        print("Modify the ./tensorexperiments/tf.py file to run your test TensorFlow code as needed")
    else:
        print("Sorry, it looks like something isn't working right with TensorFlow GPU support")