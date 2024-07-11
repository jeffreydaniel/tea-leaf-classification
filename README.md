# Tea Leaf Classification Project

## Overview

This project focuses on the classification of tea leaves into different grades using the YOLOv8 object detection model. The classification is based on various factors such as stem length, presence of buds, and other relevant features. The tea grades are categorized into Grade A, Grade B, and Grade C.

## Dataset

The dataset used for training and evaluation consists of images of tea leaves with corresponding annotations. The annotations include information about the grade of the tea leaves, such as the presence of buds, stem length, and other relevant attributes .

## YOLOv8 Model

The YOLOv8 (You Only Look Once version 8) model is employed for object detection and classification tasks. YOLOv8 is known for its speed and accuracy, making it suitable for real-time applications. The model is trained on the annotated tea leaf dataset to classify tea leaves into Grade A, Grade B, and Grade C.

## Tea Grades Criteria

The classification into Grade A, Grade B, and Grade C is based on the following criteria:

- **Stem Length:** The length of the stem is a crucial factor in determining the grade of the tea leaf.
- **Presence of Buds:** The presence or absence of buds contributes to the overall quality and grade of the tea.
- **Colour of the leaves:** The lighter colored leaves represent a higher grade, while the darker colored ones represent lower grades.

# Training
## Dataset Details:
The data for the project was gathered by TANSAM employees at Ooty, Tamilnadu. The data includes various collections of grouped and single leaf pictures.
Each leaf grade had their own set of grouped and single data. The dataset was thoroughly cleaned and checked by various members. Proper care was taken to ensure the confidentiality of the data.

## Annotation:
Annotation for the data was done using Roboflow's annotation tools. The dataset was later exported and used in order to train the model locally.

## Preprocessing steps:
- Auto-Orient
- Resizing: Stretch to 640x640

## Augmentation steps:
- Flip: Horizontal, Vertical
- Hue: Between -25° and +25°
- Saturation: Between -25% and +25%
- Brightness: Between -25% and +25%

## Dependencies

- Python 3.x
- Ultralytics and YOLOv8

## Acknowledgments
I extend my sincere gratitude to TANSAM (Tamilnadu Smart and Advanced Manufacturing) for providing us with a valuable project and dataset during our internship. 

- Various members who worked on the project:
- Jeffrey Terrance Daniel I.
- Pranav Kumar G.
- Naga Arjun V.
- Rahul A.
- Tanisha M.
- Jerusha C.R.
- Ishwarya P.
