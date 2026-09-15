# ICA Receipt Parser

An OCR pipeline that extracts and structures text from Swedish grocery receipts (ICA supermarket chain), built as a first hands-on project in computer vision and OCR.

## What it does

Given a photo of a receipt, the pipeline:
1. Runs OCR (EasyOCR, Swedish + English) to detect and read all text on the image
2. Extracts the bounding box coordinates of each detected text fragment
3. Sorts fragments top-to-bottom, left-to-right based on their position
4. Groups fragments that share a similar vertical position into single receipt lines

The result is a list of human-readable lines reconstructing the receipt's original layout — e.g. `Beer 2,8% burk 6,50` instead of a jumbled bag of words.

## Example output

Ica supermarket
Datun Fors [el . 046-2118370 2009-01-31 8027 Ka Tid 2148 18.39
Beer 2,8x burk 0,50 6,50
Pant 287xgr€
'69,9Okr /ka 55,71
Kasear  Kolontal Kavlar Knackebrod Btbart Tarok IcA 12,50 2 25 15.90 8
Lattdcyck Citron Lok Vit onka atbort 2st*3,90 7,80 7,90
Mossnor Fjal Ib 18,90
Morot IcA_ 5,00
ENud ar blffsmak 3st*4,90 70
Rabatt Papr #Nud kaRod/GuI  ICA ar kyck Nudl ar smek 4st 15kr 10,00 60
astkasse 50
Russin 'pack 12,90
Standaran jolk 8,50
Sylta ICA 200g 90
Ägg Guidgula 23,90
App 0-svenskt 5,73
Total 281 29
12,00 Erha) Jen rabatt; 25,Do Monsk 29,98 Mons 0,30 4,60 249,81 Netto 1,20 279 ,79 Brutto 1,50


## Tech stack

- **OpenCV** — image preprocessing (grayscale conversion, global and adaptive thresholding)
- **EasyOCR** — pretrained text detection and recognition
- **PyTorch** — used both as EasyOCR's backend and separately, to train a first classifier (MNIST) as a learning exercise
- **NumPy** — coordinate math and array manipulation

## Project structure