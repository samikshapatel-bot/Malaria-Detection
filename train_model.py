
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models

IMG_SIZE = 128
BATCH = 32

datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train = datagen.flow_from_directory(
    "dataset/cell_images",
    target_size=(IMG_SIZE,IMG_SIZE),
    batch_size=BATCH,
    class_mode="binary",
    subset="training"
)

val = datagen.flow_from_directory(
    "dataset/cell_images",
    target_size=(IMG_SIZE,IMG_SIZE),
    batch_size=BATCH,
    class_mode="binary",
    subset="validation"
)

model = models.Sequential([
    layers.Conv2D(32,(3,3),activation="relu",input_shape=(128,128,3)),
    layers.MaxPooling2D(),
    layers.Conv2D(64,(3,3),activation="relu"),
    layers.MaxPooling2D(),
    layers.Conv2D(128,(3,3),activation="relu"),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128,activation="relu"),
    layers.Dropout(0.5),
    layers.Dense(1,activation="sigmoid")
])

model.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])

model.fit(train,epochs=10,validation_data=val)

model.save("model/malaria_cnn.h5")
