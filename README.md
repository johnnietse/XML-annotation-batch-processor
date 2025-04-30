# XML Annotation Batch Processing Script

A lightweight Python script to automatically round bounding box coordinates in XML files (PASCAL VOC format) to integer values **without opening them manually**. Processes entire folders of annotations with one click.

## Purpose

This tool processes XML annotation files and rounds the `xmin`, `ymin`, `xmax`, and `ymax` values of bounding boxes to the nearest integer. This is useful for cleaning up annotations that might contain fractional coordinates from annotation tools.


## How did I initially come up with this idea?
- Developed to solve the specific challenge in training our vehicle's object detection model in our autonomous vehicle dataset pipeline as a part of my Level 4 Autonomous Vehicle course project at Queen's University:
  - **Manual Effort Reduction**: Aim to process annotations from multiple .xml files with one command
  - **Pipeline Integration**: Aim to process model-ready datasets from LabelImg/Make Sense exports
  - **Manual editing limitations**: Manually editing 500+ XML files individually is error-prone and time-consuming  
  - **Automotive-scale needs**: Real-world vehicle datasets require batch processing capabilities. Manual annotation adjustment is infeasible for large datasets 
  - 🚫 Discovered Google Colab throws errors with decimal values in XML annotations during model training 
  - ⚡ Created to automatically convert floating-point coordinates to integers for Google Colab compatibility
  - **Pixel Coordinates**: Object detection models expect integer positions (whole pixels)
  - **TFOD (TensorFlow Object Detection) Parsing**: tf.train.Example requires int64 for bounding boxes
  - **Annotation Consistency**: Mixed float/int values cause shape mismatches


## 🚗 Project Context
This tool supports development of our vehicle's perception system by:
- Processing raw annotations from labeling tools
- Ensuring numerical validity of bounding box coordinates
- Preparing dataset for object detection model training
- Maintaining compatibility with automotive-focused ML pipelines
- 🔧 Colab-Ready Conversion: Makes XML files compatible with TFOD (TensorFlow Object Detection) and PyTorch


## Features
- 🎯 Precision handling: Rounds all bounding box coordinates (xmin, ymin, xmax, ymax) to nearest integer
- Preserves XML structure while updating coordinates
- ⚠️ Error skipping: Ignores bad values while processing other files and handles invalid coordinate values gracefully
- Processes entire directories of XML files
- 🔄 Automatic folder creation: - Creates output directory automatically if it doesn't exist
- 🧹 Non-destructive: Never modifies your original files

## Prerequisites

- Python 3.x
- XML annotation files in PASCAL VOC format

## Usage

### Quick Start
Clone the Repository
```bash
git clone https://github.com/johnnietse/XML-annotation-batch-processor.git
cd XML-annotation-batch-processor
```

### Continuation from Quick Start
1. Update the input/output paths in the script (edit these lines in the script):
   ```python
   input_folder = "path/to/your/input/annotations" # Folder with raw XMLs
   output_folder = "path/to/your/output/annotations_fixed" # New folder for corrected files
   ```

2. Run the script:
  ```bash
  python main.py
  ```

3. Processed files will be saved in the output directory

Example Folder Structure

<pre>
XML-annotation-batch-processor/
├── dataset/
│      ├── annotations/          # Original annotation files
│      ├── annotations_fixed/    # Processed annotation files (created automatically)
│      └── images/               # the dataset
├── main.py                      # Python Script          
└── README.md
</pre>




4. Done - Your rounded annotations will appear in the output folder with the following output shown in the terminal:
```bash
C:\Users\Johnnie\AppData\Local\Programs\Python\Python310\python.exe C:\Users\Johnnie\PycharmProjects\XML-annotation-batch-processor\main.py 
Updated team01_001.xml -> dataset/annotations_fixed\team01_001.xml
Updated team01_002.xml -> dataset/annotations_fixed\team01_002.xml
Updated team01_003.xml -> dataset/annotations_fixed\team01_003.xml
Updated team01_004.xml -> dataset/annotations_fixed\team01_004.xml
Updated team01_005.xml -> dataset/annotations_fixed\team01_005.xml
Updated team01_006.xml -> dataset/annotations_fixed\team01_006.xml
Updated team01_007.xml -> dataset/annotations_fixed\team01_007.xml
Updated team01_008.xml -> dataset/annotations_fixed\team01_008.xml
Updated team01_009.xml -> dataset/annotations_fixed\team01_009.xml
Updated team01_010.xml -> dataset/annotations_fixed\team01_010.xml
Updated team01_011.xml -> dataset/annotations_fixed\team01_011.xml
...
Process finished with exit code 0
```

Notes:
- Always back up your original annotations before processing
- The script skips files with non-numeric coordinate values and prints warnings
- Tested with standard PASCAL VOC format XML files
- Output files maintain the same naming convention as input files


## What It Solves
- 🛠️ **Avoid opening individual XML files to fix coordinates**
- ⚡ **Instant processing**: Convert hundreds of files in seconds
- 📂 **Clean workflow**: Keeps original files intact while saving corrected versions to a new folder


## Why Round Coordinates?
- Some computer vision frameworks require integer coordinates for bounding boxes. This script helps:
  - Remove decimal precision from annotation tools
  - Fix potential rendering issues in visualization tools
  - Ensure compatibility with strict coordinate requirements

## Why This Exists
Created for those moments when you realize:
- Your annotation tool exported fractional coordinates
- You need integer values for your object detection model 
- **Format compliance**: Ensures Google Colab-compatible integer coordinates consistently  

---

**Important:** The datasets processed by this tool belong to and remain the intellectual property of respective groups from the Queen's University Level 4 Autonomous Vehicle course. This program neither claims ownership nor provides rights to redistribute these datasets. All annotation files are used with explicit permission for academic project purposes only.




## Copyright Notice
- Datasets: © Copyright 2025 by original creator groups
- Commercial use/replication of data prohibited without written consent

**Important Clarifications**:
- Dataset copyright remains with original owners (see [Copyright Notice](#copyright-notice)

