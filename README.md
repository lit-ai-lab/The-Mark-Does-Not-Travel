# The Mark Does Not Travel: Provenance State-Transition-Based Governance for Synthetic Media Distribution Chains

This repository contains the image dataset used for the scenario experiments in the paper **"The Mark Does Not Travel"** The images, generated using various generative AI tools, are curated to facilitate research on watermark transferability and detection under diverse real-world scenarios.

## 📄 Paper Information
- **Title**: The Mark Does Not Travel: Provenance State-Transition-Based Governance for Synthetic Media Distribution Chains

## 🛠 Tools Used
The following generative AI models were used to build this dataset:

- **ChatGPT**: Sora
- **Gemini**: Nano banana 2
- **Genspark-Flux2**: Flux2
- **Genspark-NanoBanana2**: Nano banana 2
- **Midjourney**: Midjourney v7

## 🛠 Experimental Environment
The experiments were conducted under the following environment and conditions:

- **OS**: Windows 11
- **Browser**: Chrome 146 (x64)
- **Editing Tools**: Windows Photos App (for filtering, blurring, cropping, and composition adjustments)
- **Format Conversion**: [png2jpg.com](https://png2jpg.com/) (PNG to JPG)
- **Platforms**:
  - **1-2-a**: X (formerly Twitter)
  - **1-2-b**: Facebook -> X
- **Verification Tools**:
  - **SynthID Verification**: `@SynthID` within the Gemini app
  - **C2PA Metadata Verification**: [Content Credentials (Verify)](https://verify.contentauthenticity.org/)
  - **XMP Verification**: `check_xmp.py`

## 📊 Dataset Statistics
- **Total Images**: 370
- **Composition**: Scenario-specific data across 5 AI tools and original source images.

## 📂 Data Structure
The dataset is organized as follows:

```text
WM_Scenario_Image_Dataset/
├── [Tool_Name]/           # Name of the AI tool (e.g., ChatGPT, Gemini, Midjourney)
│   ├── original/          # Original images used in the experiments
│   ├── 1-1-a/             # Images for Scenario 1-1-a
│   ├── 1-1-b/             # Images for Scenario 1-1-b
│   │   ...
│   ├── 3-1-a/             
│   │   ├── filter-20/     # Filter intensity 20 applied
│   │   └── filter-80/     # Filter intensity 80 applied
│   └── 3-1-b/
│       ├── blur-20/       # Blur intensity 20 applied
│       └── blur-80/       # Blur intensity 80 applied
```

## 🔬 Scenario Design
Each folder code represents a specific experimental scenario and image transformation method as detailed below:

| Failure Class | Vector Type | Code | Representative Transformation | Covered PST |
| :--- | :--- | :--- | :--- | :--- |
| **System-induced damage** | Model transfer | 1-1-a | Same-model regeneration of the original image using the same generative model | PST5 |
| | | 1-1-b | Cross-model regeneration or inpainting using another AI model | PST5 |
| | Platform transfer | 1-2-a | Upload and download within a single platform, causing recompression, re-encoding, or metadata handling | PST2 |
| | | 1-2-b | Cross-platform reupload between social media, community platforms, or messaging services | PST3 |
| **Non-malicious user transfer** | Copy or save | 2-1-a | Browser save-as, copy-paste, local saving, or screenshot-based acquisition of a displayed image | PST2/PST4 |
| | | 2-1-b | Format conversion, such as saving a PNG image as a JPEG file | PST4 |
| | Share or deliver | 2-2-a | Public resharing through repost, quote-post, platform share, or reupload functions | PST3 |
| | | 2-2-b | Closed-channel delivery through messenger or direct transmission with automatic compression | PST2/PST3 |
| **Non-malicious editing** | Visual adjustment | 3-1-a | Application of platform filters, color correction, contrast change, or style effects | PST4 |
| | | 3-1-b | Blur, denoising, partial masking, or noise-removal effects | PST4 |
| | Composition change | 3-2-a | Cropping, including removal of visible watermark regions | PST4 |
| | | 3-2-b | Resizing, reframing, or layout adjustment | PST2/PST4 |

## 🚀 Getting Started
Due to the large file size, the dataset is distributed via GitHub Releases. To use the dataset, please download `Dataset.zip` from the [Releases] page of this repository and extract it.

## 📝 License
This dataset is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).
