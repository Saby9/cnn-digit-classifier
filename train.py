history = model.fit(x_train, y_train, epochs=5, batch_size=64, validation_data=(x_test, y_test))
