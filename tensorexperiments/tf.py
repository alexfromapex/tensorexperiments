import tensorflow as tf

def main():
    if any(["GPU" in device for device in tf.config.list_physical_devices()]):
        print("Congratulations, you have GPU support! \U0001F389")
        print("Modify the ./tensorexperiments/tf.py file to run your test TensorFlow code as needed")
    else:
        print("Sorry, it looks like GPU support isn't currently working")