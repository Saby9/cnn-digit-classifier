predictions = model.predict(x_test)
predicted_classes = tf.argmax(predictions, axis=1)
