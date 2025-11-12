# Uzbek Sign Language (UzSL) Data Collector  
  
**Python:** `3.9.23`  
**Author:** Custom-built for isolated dynamic sign collection  
**Purpose:** Record **videos** + **per-frame MediaPipe landmarks** in a structured, scalable way  

---

## Overview

This is a **CLI-based 3-stage data collection system** for **Uzbek Sign Language (UzSL)** using **MediaPipe Holistic**.  

It supports:  
- Multiple **signers** (`signer01`, `signer02`, ...)  
- Dynamic **sign word list** (add words anytime)  
- **Multiple repetitions** per sign  
- **Real-time feedback** (countdown, rep count, tree view)  
- **Automatic folder & file management**  

---

## 3 Stages of Workflow

| Stage | Description | Key Press |
|------|-------------|-----------|
| **1. Signer Selection** | Choose or create `signerXX` | Type ID |
| **2. Sign Word Selection** | Pick from numbered list (green = recorded) | Number / `a` / `b` |
| **3. Recording** | Press `s` → countdown → record **64 frames** | `s` = again, `d` = done |

> **After 64 frames**, only then can you press `s` or `d`.

---

## Project Structure (Files)

```text
uzsl-collector/
│
├── config.py          # Global settings (paths, FPS, landmarks)
├── storage.py         # Folder creation, progress, tree view
├── ui.py              # CLI menus (signer, sign, post-recording)
├── recorder.py        # OpenCV + MediaPipe (core processing)
├── main.py            # Entry point – run this!
└── extract_keypoints.py (optional) # Post-process old videos
```

## Dataset Structure (Example)

```tree
Data_Numpy_Arrays_RSL_UzSL/
└── signer01/
    ├── meta.json                         # List of sign words for this signer
    ├── nima/
    │   ├── videos/
    │   │   ├── rep-0/
    │   │   │   └── video.mp4             # 64 frames, 30 FPS metadata
    │   │   ├── rep-1/
    │   │   └── rep-2/
    │   └── landmarks/
    │       ├── rep-0/
    │       │   ├── frame-00.npy          # 1662-dim vector
    │       │   ├── frame-01.npy
    │       │   └── ... (64 total)
    │       ├── rep-1/
    │       └── rep-2/
    └── salom/
        ├── videos/...
        └── landmarks/...
```
Each .npy = 1662 float32 values
face (468×3) + pose (33×4) + hands (2×21×3)
Upper-body pose only (legs, head, torso removed)

## Install Dependencies and Activate Environment
```text
conda env create -f environment.yml

conda activate bisp_islr_env
```

## Run video collector
```text
python main.py
```

## User Interface
```text
=== CURRENT DATASET TREE ===
  signer01  [2/5 signs recorded]
     [✓] nima  (reps: 3)
     [✓] salom  (reps: 1)
     [ ] rahmat (reps: 0)
     ...

=== SIGNER MENU ===
Enter a new signer ID (e.g. signer03) or pick an existing one.
Signer ID: signer01

=== SIGN WORD LIST ===
 1. nima
 2. salom
 3. rahmat
 4. yaxshi
[a] Add new word  [b] Back

Select: 1

Press **s** in the camera window to start repetition 1 of **nima**

[Camera shows: "Press 's' to start"]

→ Press **s** → 5-second countdown → records 64 frames

Finished repetition 1 for sign **nima**
[s] Record another    [d] Done → back to list
```
